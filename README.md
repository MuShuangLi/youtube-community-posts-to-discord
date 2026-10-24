# Automatic notifications for YouTube social media posts to Discord
🌏 **繁體中文使用者：[點這裡查看繁體中文說明](README.zh-TW.md)**

## 🧭 New to GitHub or programming?

**No problem. You do not need to learn programming first.**

If you are unfamiliar with GitHub, Forks, Webhooks, Secrets, or GitHub Actions, you can ask an AI assistant to guide you through the setup one step at a time.

👉 **[Click here to get the AI Setup Assistant Prompt](AI_SETUP_PROMPT.md)**

Copy the prompt and paste it into the AI assistant you normally use. The AI will guide you through one step at a time.

> 🔐 The AI does not need your Discord Webhook URL, passwords, or other secret information. Do not share these with an AI assistant.
---
Automatically detect new **YouTube Community Posts** and send their links to a specified Discord channel using **GitHub Actions** and a **Discord Webhook**.

No Discord bot, always-on computer, or self-hosted server is required.

## Features

- 🆓 Completely free to use
- 🤖 Fully automated with GitHub Actions
- 💬 No Discord bot required
- 🔗 Automatically sends new YouTube Community Post links to Discord
- 🛡️ Filters out older posts that may unexpectedly reappear in YouTube's page data
- 🔁 Keeps track of detected posts to prevent duplicate notifications
- 🖥️ Your computer does not need to stay on
- 🔐 Discord Webhook URL is securely stored using GitHub Secrets instead of being written directly into the code
- ⏱️ GitHub Actions is scheduled to check for new YouTube community posts every 5 minutes
- 🔑 No YouTube API Key required
> ⚠️ GitHub Actions scheduling may be delayed, so the actual check interval is not guaranteed to be 5 minutes.

## How It Works

```text
YouTube Community Post
        ↓
GitHub Actions
        ↓
Check for new Community Posts
        ↓
Filter old / previously detected posts
        ↓
Discord Webhook
        ↓
Your Discord channel
```

The program keeps track of previously detected YouTube Community Posts and periodically checks your YouTube channel.

A post is sent to Discord only when both of the following conditions are met:

1. The YouTube Community Post has not been detected before.
2. Its publication time indicates that it was published recently.

This helps prevent older YouTube posts from being incorrectly treated as newly published posts when they unexpectedly reappear in YouTube's page data.

## Requirements

You need:

- A GitHub account
- A YouTube channel that can publish Community Posts
- A Discord server where you have permission to create a Webhook
- Your YouTube Channel ID

**You do not need:**

- A self-hosted server
- An always-on computer
- A Discord bot
- A YouTube API key

## Installation

You do not need to download or host the program yourself. Once the following setup is complete, GitHub Actions will run it automatically.

### 1. Fork This Repository

Click **Fork** near the top-right of this page to copy this repository to your own GitHub account.

All further configuration should be performed inside your own forked repository.

> ⚠️ Do not add your Discord Webhook URL or other personal configuration directly to the original repository.

### 2. Get Your YouTube Channel ID

You need your YouTube Channel ID beginning with `UC`, for example:

```text
UCxxxxxxxxxxxxxxxxxxxxxx
```

This is **not** your `@channelhandle`.

You can find it in:

**YouTube Studio → Settings → Channel → Advanced settings**

Look for your **Channel ID**.

Copy the ID. You will need it later.

### 3. Create a Discord Webhook

In Discord, open the channel where you want to receive YouTube Community Post notifications.

Go to:

**Edit Channel → Integrations → Webhooks → Create Webhook**

You can choose your own Webhook name and avatar.

Make sure the Webhook points to the correct Discord channel, then select:

**Copy Webhook URL**

Save this URL for the next steps.

> ⚠️ **Your Discord Webhook URL is sensitive information.**
>
> Anyone who obtains the URL may be able to send messages to your Discord channel through the Webhook.
>
> Do not post your Webhook URL in public code, README files, Issues, comments, or any other public location.

### 4. Configure Your YouTube Channel ID

Open the GitHub repository that you forked earlier.

Go to:

**Settings → Secrets and variables → Actions**

Switch to:

**Variables**

Select:

**New repository variable**

For Name, enter:

```text
YOUTUBE_CHANNEL_ID
```

For Value, enter your own YouTube Channel ID, for example:

```text
UCxxxxxxxxxxxxxxxxxxxxxx
```

Save the variable.

A YouTube Channel ID is not a secret, so it can safely be stored as a GitHub Repository Variable.

### 5. Configure Your Discord Webhook

Go to:

**Settings → Secrets and variables → Actions**

This time, switch to:

**Secrets**

Select:

**New repository secret**

For Name, enter:

```text
DISCORD_WEBHOOK_URL
```

For Secret, enter:

```text
Your Discord Webhook URL
```

Then save it.

After a GitHub Secret is saved, GitHub will not display its full value again.

You do not need—and should not—write your Discord Webhook URL directly into `check_posts.py` or `main.yml`.

### 6. Enable GitHub Actions Write Permission

The program needs to create and update:

```text
seen_posts.json
```

This file keeps track of YouTube Community Posts that have already been detected and prevents duplicate notifications.

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

### 7. Run the Workflow for the First Time

After completing the configuration above, open the **Actions** tab at the top of your repository.

Select:

**YouTube Community Posts to Discord**

Then click:

**Run workflow → Run workflow**

Wait for the workflow to finish.

Under normal conditions, you should see a green success indicator.

#### Why Doesn't the First Run Send Anything to Discord?

This is an intentional safety feature.

On the first run, the program detects the YouTube Community Posts that are currently visible and creates:

```text
seen_posts.json
```

All currently existing posts are recorded as already seen.

Therefore:

**The first run will not send all of your old YouTube Community Posts to Discord.**

This is expected behavior and does not mean the program failed.

> ⚠️ **Note: If your YouTube channel has never published a Community Post**
>
> The first run may fail because no Community Post URL can be found.
>
> If this happens, first go to YouTube and publish one **public Community Post**.
>
> After publishing it, wait about **5 minutes**, then return to:
>
> **GitHub Repository → Actions → YouTube Community Posts to Discord**
>
> Click:
>
> **Run workflow → Run workflow**
>
> to run the workflow again.
>
> If the same error still appears after waiting, please check:
>
> - Whether the YouTube channel has enabled the **Community** page.
> - Whether the Community Post you just published is set to **Public**.
> - Whether the post can still be viewed while you are signed out of that YouTube account.
>
> If all of the above are correct but the same error still occurs, first check the error log under **Check YouTube Community Posts** in GitHub Actions before troubleshooting further.

### 8. Test a New Post Notification

After the first run succeeds, publish a new Community Post on your YouTube channel.

You can test it in either of the following ways.

#### Option A: Wait for the Automatic Check

You do not need to do anything. Wait for GitHub Actions to run automatically.

#### Option B: Run an Immediate Manual Test

Go to:

**Actions → YouTube Community Posts to Discord → Run workflow**

Run the workflow manually.

If everything is working correctly, your selected Discord channel should receive a link similar to:

```text
https://www.youtube.com/post/...
```

This should be the YouTube Community Post you just published.

### 9. Automatic Operation

After setup is complete, you normally do not need to run the workflow manually.

By default, GitHub Actions will:

**Check for new YouTube Community Posts every 5 minutes.**

This means:

- Your computer does not need to stay on
- Discord does not need to stay open
- YouTube does not need to stay open
- You do not need to run Python yourself
- You do not need to host your own server

> GitHub Actions scheduling is not a real-time notification system.
>
> A 5-minute schedule does not guarantee execution exactly at minutes 00, 05, 10, 15, and so on. Runs may occasionally be delayed depending on GitHub's scheduling availability.

## How New Posts Are Detected

The data returned by YouTube's Community page does not always contain exactly the same posts or appear in exactly the same order.

Older Community Posts may sometimes unexpectedly reappear in the page data.

For this reason, the program does not determine whether a post is new solely by checking whether its Post ID has been seen before.

It checks:

1. Whether the Post ID has previously been detected.
2. The publication time provided by YouTube.
3. Whether the post is recent enough to be considered newly published.

Only posts that meet the required conditions are sent to Discord.

By default, the program considers a post eligible for notification only when it was published **within the last 6 hours and has not been detected before**.

If YouTube does not provide a reliable publication time, the program chooses **not to send the notification** in order to reduce the risk of sending an old post to Discord.

## Common Situations

### Editing an Existing YouTube Post

Editing an existing Community Post will not send another Discord notification.

The edited post keeps the same Post ID, and that ID has already been recorded by the program.

### Deleting a YouTube Post

Deleting a previously published post does not affect the detection of future posts.

Its Post ID remains in the historical records stored in `seen_posts.json`.

### Deleting and Reposting

If you delete a post and publish it again, YouTube creates a new Post ID for the newly published post.

The repost may therefore be treated as a new post and may generate another Discord notification.

The previous Discord notification is not automatically deleted.

### An Old Post Appears Again

YouTube may occasionally return an older Community Post that was not present in an earlier check.

The program uses the publication time to filter these posts.

For example:

```text
27 seconds ago
```

is considered recent.

However:

```text
4 months ago
```

will not be sent to Discord.

After an old post is identified, it is still added to the seen-post history so that it does not need to be reconsidered repeatedly.

## Security Notes

- Never publicly share your `DISCORD_WEBHOOK_URL`
- Do not write your Webhook URL directly into the source code
- Store your Discord Webhook URL using GitHub Secrets
- If your Webhook URL is accidentally exposed, delete or regenerate the Webhook in Discord immediately
- `YOUTUBE_CHANNEL_ID` is not a secret and can be stored as a GitHub Repository Variable

## Languages

- [English](README.md)
- [繁體中文](README.zh-TW.md)

Additional translations are welcome through pull requests.

## License

This project is licensed under the **MIT License**.

You may use, copy, modify, and distribute this project under the terms of the MIT License.

See the [`LICENSE`](LICENSE) file for the full license text.
