# AI 安裝助手提示詞

[English](AI_SETUP_PROMPT.md) | [繁體中文](AI_SETUP_PROMPT.zh-TW.md)

## 如何使用這份提示詞

1. 複製下方「AI 提示詞」區塊中的全部內容。
2. 打開你平常使用的 AI 助手。
3. 開啟一個新的對話。
4. 將提示詞完整貼給 AI。
5. 按照 AI 的指示，一次完成一個步驟。
6. 如果不知道該按哪裡，可以詢問 AI，或提供你目前畫面的截圖。

> ⚠️ 請勿將 Discord Webhook URL、密碼、Access Token 或其他秘密資訊提供給 AI。

## 複製以下提示詞

```text
我想安裝開源專案「YouTube Community Posts to Discord」。

專案網址：
https://github.com/MuShuangLi/youtube-community-posts-to-discord

我幾乎沒有 GitHub 或程式設計的使用經驗。

請從頭到尾協助我完成這個專案的安裝與設定。

開始以前，如果你能夠存取這個 GitHub Repository，請先閱讀專案目前的 README 與安裝說明。

如果你無法存取這個 Repository 或 README，請直接告訴我，並請我提供相關 README 內容或畫面截圖。不要自行猜測這個專案的設定方式。

協助我的過程中，請遵守以下規則：

1. 一次只能帶我完成「一個步驟」。

2. 告訴我一個步驟之後，請停止並等待。我確認完成、提出問題或提供截圖後，你才能繼續下一步。

3. 不要假設我了解 GitHub 或程式設計相關術語。

4. Repository、Fork、GitHub Actions、Workflow、Secret、Variable、Webhook、Channel ID 等術語第一次出現時，請用適合完全新手理解的方式簡短解釋它是什麼。

5. 每一個步驟都請清楚告訴我：
   - 現在應該在哪一個網站
   - 應該進入哪一個頁面
   - 應該點哪一個按鈕或選單
   - 完成後應該看到什麼

6. 如果我的 GitHub、Discord 或 YouTube 畫面與 README 的說明不同，請根據我提供的截圖或描述協助我尋找正確的位置。不要捏造畫面上不存在的按鈕。

7. 絕對不要要求我把 Discord Webhook URL、密碼、Access Token、GitHub Secret 或其他秘密資訊貼到對話中。

8. 如果我提供截圖，請注意截圖中是否意外包含秘密資訊。如果有，請提醒我哪些資訊需要保護，以及是否需要重新產生或撤銷相關憑證。

9. Discord Webhook URL 必須儲存在 GitHub Actions Repository Secret，而且名稱必須完全是：

DISCORD_WEBHOOK_URL

10. YouTube Channel ID 必須儲存在 GitHub Actions Repository Variable，而且名稱必須完全是：

YOUTUBE_CHANNEL_ID

11. 不要叫我把以上兩個值直接寫進 check_posts.py 或 main.yml。

12. 除非目前 Repository 的程式或說明確實存在需要修正的錯誤，否則不要修改 check_posts.py 或 .github/workflows/main.yml。

13. 請協助我確認 GitHub Actions 的 Workflow permissions，確保 Workflow 可以更新 seen_posts.json。

14. 請向我解釋：第一次成功執行 Workflow 的用途是建立最初的「已看過貼文」紀錄，因此不應該把目前所有舊的 YouTube 社群貼文全部發送到 Discord。

15. 第一次執行成功後，請帶我實際發布一篇新的 YouTube 社群貼文進行測試，並確認 Discord 只收到這篇新貼文的一次通知。

16. 如果過程中發生錯誤，請先帶我查看 GitHub Actions 的執行紀錄與錯誤訊息，再決定是否需要修改程式。

17. 不要一次修改很多不同的東西。一次只診斷並處理一個問題。

18. 如果專案 README 的說明與目前 GitHub、Discord 或 YouTube 的實際介面不一致，請明確告訴我哪裡不一致，不要在沒有說明的情況下自行改變操作流程。

19. 全部設定完成後，請協助我確認：
   - Workflow 可以成功執行
   - seen_posts.json 有正常更新
   - 舊貼文不會被當成新貼文發送
   - 新貼文會被發送到我指定的 Discord 頻道
   - GitHub Actions 的自動排程有正常啟用

現在請先用完全不需要程式設計背景也能理解的方式，簡單告訴我這個專案是做什麼的。

接著只告訴我「第一個設定步驟」。

說完第一個步驟後請停止，等待我的回覆，不要繼續第二步。
```

## 重要提醒

AI 助手也可能犯錯，而且 GitHub、Discord 與 YouTube 的介面未來可能改版。

如果 AI 提供的操作方式與本專案目前的說明不一致，請優先重新確認本 Repository 最新版本的文件，並要求 AI 根據目前的文件重新判斷。

請勿在 AI 對話、GitHub Issues、留言、公開程式碼或截圖中公開你的 Discord Webhook URL 或其他秘密憑證。
