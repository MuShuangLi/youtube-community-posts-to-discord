# YouTube Community Posts to Discord

[English](README.md) | [繁體中文](README.zh-TW.md)

Automatically detect new **YouTube Community Posts** and send their links to a specified Discord channel using **GitHub Actions** and a **Discord Webhook**.

No Discord bot, self-hosted server, or always-on computer is required.

## Features

- 🆓 Free to use
- 🤖 Fully automated with GitHub Actions
- 💬 No Discord bot required
- 🔗 Automatically sends new YouTube Community Post links to Discord
- 🛡️ Filters old posts that may unexpectedly reappear in YouTube's Community page data
- 🔁 Keeps track of previously detected posts to prevent duplicate notifications
- 🖥️ Your computer does not need to stay on
- 🔐 Discord Webhook URL is securely stored using GitHub Secrets
- ⏱️ Checks for new YouTube Community Posts every 5 minutes

## How It Works

```text
YouTube Community Post
        ↓
GitHub Actions
        ↓
Check for new Community Posts
        ↓
Filter old / previously seen posts
        ↓
Discord Webhook
        ↓
Specified Discord Channel
```

The program keeps track of previously detected YouTube Community Posts and periodically checks the YouTube channel for new posts.

A post is sent to Discord only when:

1. The YouTube Community Post has not been detected before.
2. Its publication time indicates that it was published recently.

This helps prevent older YouTube posts from being incorrectly detected as new when they unexpectedly reappear in the Community page data.

## Requirements

You will need:

- A GitHub account
- A YouTube channel with Community Posts
- A Discord server where you have permission to create a Webhook
- Your YouTube Channel ID

**You do not need:**

- A self-hosted server
- An always-on computer
- A Discord bot
- A YouTube API Key

# Installation

You do not need to download or host the program yourself. Once the following settings are configured, GitHub Actions will run it automatically.

## 1. Fork this Repository

Click **Fork** near the top-right of this page to create a copy of this repository under your own GitHub account.

All of the following configuration steps should be performed in **your own forked repository**.

> ⚠️ Do not enter your Discord Webhook or other personal configuration into the original repository.

## 2. Find Your YouTube Channel ID

You need your YouTube Channel ID, which normally begins with `UC`.

For example:

```text
UCxxxxxxxxxxxxxxxxxxxxxx
```

This is **not** the same as your `@channelname`.

You can find it in:

**YouTube Studio → Settings → Channel → Advanced settings**

Find **Channel ID** and copy it. You will need it later.

## 3. Create a Discord Webhook

In Discord, open the channel where you want YouTube Community Post notifications to appear.

Go to:

**Edit Channel → Integrations → Webhooks → Create Webhook**

You can choose any name and avatar for the Webhook.

Make sure the Webhook is connected to the correct Discord channel, then select:

**Copy Webhook URL**

Keep this URL available for the next steps.

> ⚠️ **Your Discord Webhook URL is sensitive information.**
>
> Anyone who obtains this URL may be able to send messages to the Discord channel through the Webhook.
>
> Do not post your Webhook URL in public source code, README files, Issues, comments, or other public locations.

## 4. Configure Your YouTube Channel ID

Open the GitHub repository that you forked earlier.

Go to:

**Settings → Secrets and variables → Actions**

Open the:

**Variables**

tab and select:

**New repository variable**

Set the Name to:

```text
YOUTUBE_CHANNEL_ID
```

Set the Value to your YouTube Channel ID, for example:

```text
UCxxxxxxxxxxxxxxxxxxxxxx
```

Save the variable.

A YouTube Channel ID is not a secret, so it can safely be stored as a GitHub Repository Variable.

## 5. Configure Your Discord Webhook

Go to:

**Settings → Secrets and variables → Actions**

This time, open the:

**Secrets**

tab and select:

**New repository secret**

Set the Name to:

```text
DISCORD_WEBHOOK_URL
```

Set the Secret to:

```text
Your Discord Webhook URL
```

Save the secret.

GitHub will not display the full Secret again after it has been saved.

You do not need — and should not — put your Discord Webhook URL directly inside `check_posts.py` or `main.yml`.

## 6. Enable GitHub Actions Write Permission

The program needs to create and update:

```text
seen_posts.json
```

This file stores the Community Post IDs that have already been detected and prevents duplicate notifications.

Go to:

**Settings → Actions → General**

Scroll down to:

**Workflow permissions**

Select:

**Read and write permissions**

Then click:

**Save**

You do **not** need to enable:

**Allow GitHub Actions to create and approve pull requests**

## 7. Run the Workflow for the First Time

After completing the configuration above, open the:

**Actions**

tab in your repository.

Select:

**YouTube Community Posts to Discord**

Then click:

**Run workflow → Run workflow**

Wait for the Workflow to finish.

If everything is configured correctly, the run should finish successfully with a green check mark.

### Why didn't I receive a Discord notification on the first run?

This is intentional.

During the first run, the program detects the Community Posts that are currently visible on your YouTube channel and creates:

```text
seen_posts.json
```

Those existing posts are saved as already seen.

Therefore:

**The first run will not send all of your old Community Posts to Discord.**

This is expected behavior and does not mean the program failed.

## 8. Test a New Community Post

After the first run succeeds, publish a new Community Post on your YouTube channel.

There are two ways to test it.

### Option A: Wait for the automatic check

You do not need to do anything. Wait for GitHub Actions to run automatically.

### Option B: Run it immediately

Go to:

**Actions → YouTube Community Posts to Discord → Run workflow**

and manually run the Workflow once.

If everything is working correctly, your specified Discord channel should receive a link similar to:

```text
https://www.youtube.com/post/...
```

This should be the Community Post you just published.

## 9. Automatic Checks

After setup is complete, you normally do not need to manually run the Workflow again.

By default, GitHub Actions checks for new YouTube Community Posts:

**Every 5 minutes.**

This means:

- Your computer does not need to stay on
- Discord does not need to stay open
- YouTube does not need to stay open
- You do not need to manually run Python
- You do not need to host your own server

> GitHub Actions scheduled workflows are not a real-time notification system.
>
> A 5-minute schedule does not guarantee execution at the exact 00, 05, 10, 15, etc. minute marks. GitHub may occasionally delay scheduled runs.

# How New Posts Are Detected

The data returned by YouTube's Community page is not always presented in exactly the same order or with exactly the same set of posts.

Older Community Posts may occasionally reappear in the page data.

For this reason, the program does **not** simply assume that every previously unseen Post ID is a newly published post.

The program checks:

1. Whether the Post ID has been detected before.
2. The publication time provided by YouTube.
3. Whether the post is recent enough to be considered newly published.

By default, only posts that are both **previously unseen and published within the last 6 hours** are eligible to be sent to Discord.

If YouTube does not provide a reliable publication time, the program chooses **not to send the post** in order to reduce the risk of sending an old post by mistake.

# Common Situations

## Editing an Existing YouTube Post

Editing an existing Community Post does not cause another Discord notification.

The edited post keeps the same Post ID, and that ID has already been recorded as seen.

## Deleting a YouTube Post

Deleting a published Community Post does not affect future post detection.

Its Post ID remains in the `seen_posts.json` history.

## Deleting and Reposting

If you delete a Community Post and publish it again, YouTube creates a new Post ID for the newly published post.

The repost may therefore be detected as a new Community Post and sent to Discord again.

The old Discord notification is not automatically deleted.

## Discord Receives an Old Post

YouTube may occasionally cause an older Community Post to appear in the Community page data again.

The program uses the publication time to filter these posts.

For example:

```text
27 seconds ago
```

is treated as recent.

However:

```text
4 months ago
```

is treated as old and will not be sent to Discord.

After an old post is detected and rejected, its ID is still saved as seen so it does not need to be reconsidered repeatedly.

# Security

- Never publicly share your `DISCORD_WEBHOOK_URL`
- Never hard-code your Webhook URL into the source code
- Store your Discord Webhook URL using GitHub Secrets
- If your Webhook URL is accidentally exposed, delete or regenerate the Webhook in Discord immediately
- `YOUTUBE_CHANNEL_ID` is not a secret and can be stored as a GitHub Repository Variable

# Languages

- [English](README.md)
- [繁體中文](README.zh-TW.md)

Additional translations are welcome through Pull Requests.

# License

This project is licensed under the **MIT License**.

You may use, copy, modify, and distribute this project according to the terms of the MIT License.

See [`LICENSE`](LICENSE) for the full license text.
