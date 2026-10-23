import html as html_module
import json
import os
import re
import urllib.request
from pathlib import Path

STATE_FILE = Path("seen_posts.json")

# Only unseen posts newer than this many hours may be sent to Discord.
MAX_POST_AGE_HOURS = 6


def get_required_environment_variable(name):
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(
            f"{name} is not configured. "
            "Please check your GitHub Actions settings."
        )

    return value


def get_page(channel_id):
    url = f"https://www.youtube.com/channel/{channel_id}/community"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return html_module.unescape(
            response.read().decode("utf-8")
        )


def get_community_posts(channel_id):
    page = get_page(channel_id)

    post_pattern = re.compile(
        r'"/post/(Ug[a-zA-Z0-9_-]+)'
    )

    post_ids = []

    for match in post_pattern.finditer(page):
        post_id = match.group(1)

        if post_id not in post_ids:
            post_ids.append(post_id)

    if not post_ids:
        raise RuntimeError(
            "No YouTube Community Post URLs were found. "
            "Make sure the YouTube Channel ID is correct "
            "and the channel has Community Posts."
        )

    posts = []

    for post_id in post_ids:
        positions = [
            match.start()
            for match in re.finditer(re.escape(post_id), page)
        ]

        published_text = None

        for position in positions:
            start = max(0, position - 4000)
            end = min(len(page), position + 4000)

            context = page[start:end]

            time_match = re.search(
                r'"publishedTimeText":\{"runs":\[\{"text":"([^"]+)"',
                context,
            )

            if time_match:
                published_text = time_match.group(1)
                break

        posts.append(
            {
                "id": post_id,
                "url": f"https://www.youtube.com/post/{post_id}",
                "published_text": published_text,
            }
        )

    return posts


def load_seen_posts():
    if not STATE_FILE.exists():
        return set()

    with STATE_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return set(data.get("seen_post_ids", []))


def save_seen_posts(post_ids):
    with STATE_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            {"seen_post_ids": sorted(post_ids)},
            file,
            ensure_ascii=False,
            indent=2,
        )


def is_recent_post(published_text):
    if not published_text:
        return False

    text = published_text.strip().lower()

    if re.fullmatch(r"(a|an|1|\d+) seconds? ago", text):
        return True

    if re.fullmatch(r"(a|an|1|\d+) minutes? ago", text):
        return True

    if text == "an hour ago":
        return True

    match = re.fullmatch(r"(\d+) hours? ago", text)

    if match:
        hours = int(match.group(1))
        return hours <= MAX_POST_AGE_HOURS

    # Posts measured in days, weeks, months, years,
    # or with an unknown time format are treated as old.
    return False


def send_to_discord(webhook_url, message):
    payload = json.dumps(
        {"content": message}
    ).encode("utf-8")

    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "YouTube-Community-Discord-Webhook",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status not in (200, 204):
            raise RuntimeError(
                f"Discord webhook returned HTTP {response.status}"
            )


def main():
    channel_id = get_required_environment_variable(
        "YOUTUBE_CHANNEL_ID"
    )

    webhook_url = get_required_environment_variable(
        "DISCORD_WEBHOOK_URL"
    )

    print(f"Checking YouTube Community posts for: {channel_id}")

    posts = get_community_posts(channel_id)
    seen_posts = load_seen_posts()

    print(f"Found {len(posts)} Community Post(s).")
    print(f"Previously seen: {len(seen_posts)} Post(s).")

    # First run:
    # Save all currently visible posts as the initial baseline
    # so old posts are not sent to Discord.
    if not seen_posts:
        print("No saved history found.")
        print("Establishing current posts as the initial baseline.")

        save_seen_posts({post["id"] for post in posts})

        print("Current Posts saved as seen.")
        print("No Discord messages sent.")
        return

    unseen_posts = [
        post
        for post in posts
        if post["id"] not in seen_posts
    ]

    print(f"Unseen Post(s): {len(unseen_posts)}")

    for post in unseen_posts:
        print()
        print(f"Post: {post['url']}")
        print(f"Published: {post['published_text']}")

        if is_recent_post(post["published_text"]):
            print("Recent unseen Post detected.")
            print("Sending to Discord...")

            send_to_discord(
                webhook_url,
                post["url"],
            )

            print("Sent successfully.")
        else:
            print(
                "Not recent (or publication time is unknown). "
                "Discord notification skipped."
            )

        # Remember the post even if it was old.
        # This prevents old posts that appear later in YouTube's
        # page data from being reconsidered repeatedly.
        seen_posts.add(post["id"])

    save_seen_posts(seen_posts)

    if not unseen_posts:
        print("No new Community Posts.")


if __name__ == "__main__":
    main()
