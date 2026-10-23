# YouTube Community Posts to Discord

[English](README.md) | [繁體中文](README.zh-TW.md)

Automatically send new **YouTube Community Post** links to a Discord channel using **GitHub Actions** and a **Discord Webhook**.

No Discord bot or always-on computer is required.

## Features

- 🆓 Free to use
- 🤖 Fully automated with GitHub Actions
- 💬 No Discord bot required
- 🔗 Sends new YouTube Community Post links to Discord
- 🛡️ Filters out old posts that may unexpectedly appear in YouTube's Community page data
- 🔁 Prevents duplicate notifications
- 🖥️ Your computer does not need to stay on
- 🔐 Discord Webhook URL is stored securely using GitHub Secrets
- ⏱️ Checks for new Community Posts every 5 minutes

## How It Works

```text
YouTube Community Post
        ↓
GitHub Actions
        ↓
Check for new posts
        ↓
Filter old / previously seen posts
        ↓
Discord Webhook
        ↓
Discord Channel
