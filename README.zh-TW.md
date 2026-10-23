# YouTube 社群貼文自動通知到 Discord

[English](README.md) | [繁體中文](README.zh-TW.md)

自動偵測新的 **YouTube 社群貼文（Community Post）**，並透過 **GitHub Actions** 與 **Discord Webhook**，將新貼文的連結自動發送到指定的 Discord 頻道。

不需要額外安裝 Discord Bot，也不需要讓自己的電腦 24 小時保持開機。

## 功能特色

- 🆓 完全免費
- 🤖 使用 GitHub Actions 自動執行
- 💬 不需要額外安裝 Discord Bot
- 🔗 自動將新的 YouTube 社群貼文連結發送到 Discord
- 🛡️ 過濾 YouTube 頁面資料中偶爾重新出現的舊貼文，避免誤判
- 🔁 記錄已偵測過的貼文，避免重複通知
- 🖥️ 不需要讓自己的電腦保持開機
- 🔐 Discord Webhook 網址透過 GitHub Secrets 安全保存，不會直接寫在程式碼中
- ⏱️ 每 5 分鐘自動檢查一次新的 YouTube 社群貼文

## 運作方式

```text
YouTube 社群貼文
        ↓
GitHub Actions
        ↓
檢查新的社群貼文
        ↓
過濾舊貼文／已偵測過的貼文
        ↓
Discord Webhook
        ↓
指定的 Discord 頻道
