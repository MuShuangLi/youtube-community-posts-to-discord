# YouTube 社群貼文自動通知到 Discord
🌏 **English users: [Click here to view the English README](README.md)**

## 🧭 完全不懂 GitHub 或程式設計？

**沒關係，你不需要先學會寫程式。**

如果你不知道 GitHub、Fork、Webhook、Secret 或 GitHub Actions 是什麼，可以讓 AI 助手一步一步帶你完成設定。

👉 **[點這裡取得「AI 安裝助手提示詞」](AI_SETUP_PROMPT.zh-TW.md)**

把裡面的提示詞複製給你平常使用的 AI 助手，AI 會一次帶你完成一個步驟。

> 🔐 AI 不需要知道你的 Discord Webhook URL、密碼或其他秘密資訊。請勿將這些資訊提供給 AI。

---
自動偵測新的 **YouTube 社群貼文（Community Post）**，並透過 **GitHub Actions** 與 **Discord Webhook**，將新貼文的連結自動發送到指定的 Discord 頻道。

不需要額外安裝 Discord Bot，也不需要讓自己的電腦 24 小時保持開機。

## 功能特色

- 🆓 完全免費
- 🤖 使用 GitHub Actions 自動執行
- 💬 不需要額外安裝 Discord Bot
- 🔗 自動將新的 YouTube 社群貼文連結發送到 Discord
- 🛡️ 過濾 YouTube 頁面資料中偶爾重新出現的舊貼文，降低誤判
- 🔁 記錄已偵測過的貼文，避免重複通知
- 🖥️ 不需要讓自己的電腦保持開機
- 🔐 Discord Webhook 網址透過 GitHub Secrets 安全保存，不會直接寫在程式碼中
- ⏱️ 預設每 5 分鐘自動檢查一次新的 YouTube 社群貼文
- 🔑 不需要 YouTube API Key

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
```

程式會記錄之前已經偵測過的 YouTube 社群貼文，並定期檢查 YouTube 頻道。

只有同時符合以下條件的貼文，才會發送到 Discord：

1. 這篇 YouTube 社群貼文以前沒有被偵測過。
2. 這篇貼文的發布時間足夠接近目前時間，可以判定為近期發布的新貼文。

這可以避免 YouTube 偶爾將以前的舊貼文重新出現在頁面資料中時，被程式誤認為剛發布的新貼文。

## 使用需求

你需要：

- 一個 GitHub 帳號
- 一個可以發布社群貼文的 YouTube 頻道
- 一個你有權限建立 Webhook 的 Discord 伺服器
- 你的 YouTube 頻道 ID（Channel ID）

**不需要：**

- 自己架設伺服器
- 讓電腦 24 小時開機
- 建立 Discord Bot
- YouTube API Key

## 安裝教學

不需要下載程式，也不需要自己架設伺服器。完成以下設定後，GitHub Actions 就會自動執行程式。

### 1. Fork 這個 Repository

點擊本頁右上方的 **Fork**，將這個 Repository 複製到你自己的 GitHub 帳號。

後續所有設定都請在你自己 Fork 出來的 Repository 中進行。

> ⚠️ 請勿直接在原始 Repository 中填入自己的 Discord Webhook 或其他個人設定。

### 2. 取得你的 YouTube Channel ID

你需要的是以 `UC` 開頭的 YouTube Channel ID，例如：

```text
UCxxxxxxxxxxxxxxxxxxxxxx
```

這不是你的 `@頻道名稱`。

你可以在：

**YouTube Studio → 設定 → 頻道 → 進階設定**

找到你的 **頻道 ID（Channel ID）**。

請先把這串 ID 複製起來，稍後會用到。

### 3. 建立 Discord Webhook

在 Discord 中進入你希望收到 YouTube 社群貼文通知的頻道。

進入：

**編輯頻道 → 整合 → Webhooks → 建立 Webhook**

你可以自行設定 Webhook 的名稱與頭像。

確認 Webhook 指向正確的 Discord 頻道後，選擇：

**Copy Webhook URL／複製 Webhook 網址**

請先保存這個網址，稍後會用到。

> ⚠️ **Discord Webhook URL 屬於私密資訊。**
>
> 任何取得這個網址的人都可能透過 Webhook 向你的 Discord 頻道發送訊息。
>
> 請勿將 Webhook URL 貼在公開的程式碼、README、Issue、留言或其他公開位置。

### 4. 設定 YouTube Channel ID

進入你剛才 Fork 出來的 GitHub Repository。

前往：

**Settings → Secrets and variables → Actions**

切換到：

**Variables**

選擇：

**New repository variable**

Name 填入：

```text
YOUTUBE_CHANNEL_ID
```

Value 填入你自己的 YouTube Channel ID，例如：

```text
UCxxxxxxxxxxxxxxxxxxxxxx
```

完成後儲存。

YouTube Channel ID 本身不是密碼，因此使用 GitHub Repository Variable 保存即可。

### 5. 設定 Discord Webhook

仍然前往：

**Settings → Secrets and variables → Actions**

這次切換到：

**Secrets**

選擇：

**New repository secret**

Name 填入：

```text
DISCORD_WEBHOOK_URL
```

Secret 填入：

```text
你的 Discord Webhook URL
```

然後儲存。

GitHub Secret 儲存後不會再次直接顯示完整內容。

因此你不需要、也不應該把 Discord Webhook URL 寫進 `check_posts.py` 或 `main.yml`。

### 6. 開啟 GitHub Actions 寫入權限

程式需要建立並更新：

```text
seen_posts.json
```

這個檔案用來記錄已經偵測過的 YouTube 社群貼文，避免同一篇貼文重複通知。

前往：

**Settings → Actions → General**

往下找到：

**Workflow permissions**

選擇：

**Read and write permissions**

然後按：

**Save**

不需要勾選：

**Allow GitHub Actions to create and approve pull requests**

### 7. 第一次手動執行

完成上述設定後，進入 Repository 上方的：

**Actions**

選擇：

**YouTube Community Posts to Discord**

然後點：

**Run workflow → Run workflow**

等待 Workflow 執行完成。

正常情況下會看到綠色的成功標記。

#### 第一次執行為什麼不會收到 Discord 通知？

這是刻意設計的安全機制。

第一次執行時，程式會讀取目前能偵測到的 YouTube 社群貼文，並建立：

```text
seen_posts.json
```

目前已存在的貼文會全部被設定成「已看過」。

因此：

**第一次執行不會把你以前發布的所有舊貼文一次全部丟進 Discord。**

這是正常行為，不代表程式沒有成功。

### 8. 測試新貼文通知

第一次執行成功後，可以在自己的 YouTube 頻道發布一篇新的社群貼文。

接著有兩種測試方式。

#### 方法 A：等待自動檢查

什麼都不用做，等待 GitHub Actions 自己執行。

#### 方法 B：立即手動測試

進入：

**Actions → YouTube Community Posts to Discord → Run workflow**

手動執行一次。

如果一切正常，Discord 指定頻道會收到類似：

```text
https://www.youtube.com/post/...
```

也就是你剛剛發布的 YouTube 社群貼文連結。

### 9. 自動執行

設定完成後，平常不需要再手動執行 Workflow。

GitHub Actions 預設會：

**每 5 分鐘檢查一次新的 YouTube 社群貼文。**

因此：

- 不需要讓自己的電腦保持開機
- 不需要開著 Discord
- 不需要開著 YouTube
- 不需要自己執行 Python
- 不需要另外架設伺服器

> GitHub Actions 的排程不是即時通知系統。
>
> 設定為每 5 分鐘檢查，不代表一定會精確在每個第 00、05、10、15 分鐘執行。GitHub 忙碌時可能稍微延遲。

## 判斷新貼文的方式

YouTube Community 頁面的資料並不一定每次都會以完全相同的順序或內容出現。

有時候較舊的社群貼文可能突然重新出現在頁面資料中。

因此，本程式不會單純使用「這個 Post ID 以前沒看過」來判斷它是不是新貼文。

程式會同時檢查：

1. Post ID 是否曾經被偵測過。
2. YouTube 提供的貼文發布時間。
3. 貼文是否仍屬於近期發布的內容。

只有符合條件的新貼文才會送到 Discord。

目前預設只會將 **6 小時內發布，而且以前沒有偵測過的貼文**視為可以通知的新貼文。

如果 YouTube 無法提供可靠的發布時間，程式會選擇 **不發送通知**，以降低舊貼文被誤發到 Discord 的機率。

## 常見情況

### 編輯已發布的 YouTube Post

編輯原本的社群貼文不會再次發送 Discord 通知。

因為編輯後仍然是同一個 Post ID，而程式已經記錄這個 ID。

### 刪除 YouTube Post

刪除一篇已發布的貼文不會影響之後的新貼文偵測。

它的 Post ID 仍然會保留在 `seen_posts.json` 的歷史記錄中。

### 刪除後重新發布

如果刪除一篇貼文後重新發布，YouTube 會為重新發布的貼文建立新的 Post ID。

因此重新發布的貼文會被視為一篇新的貼文，並可能再次發送 Discord 通知。

Discord 中原本舊貼文的通知不會自動刪除。

### Discord 收到舊貼文

YouTube 有時可能會在 Community 頁面資料中重新出現較舊的貼文。

本程式會利用發布時間進行過濾。

例如：

```text
27 seconds ago
```

會被視為近期貼文。

而：

```text
4 months ago
```

則不會發送到 Discord。

被判定為舊貼文後，它仍會被加入已看過記錄，避免之後重複判斷。

## 安全提醒

- 請勿公開你的 `DISCORD_WEBHOOK_URL`
- 請勿直接把 Webhook URL 寫進程式碼
- 請使用 GitHub Secrets 保存 Discord Webhook URL
- 如果 Webhook URL 不小心公開，請立即在 Discord 中刪除／重新建立該 Webhook
- `YOUTUBE_CHANNEL_ID` 本身不是密碼，可以使用 GitHub Repository Variable 保存

## 語言

- [English](README.md)
- [繁體中文](README.zh-TW.md)

歡迎透過 Pull Request 協助新增其他語言的翻譯。

## 授權

本專案採用 **MIT License**。

你可以依照 MIT License 的條款自由使用、複製、修改與散布本專案。

實際授權條款以英文 [`LICENSE`](LICENSE) 文件為準。
