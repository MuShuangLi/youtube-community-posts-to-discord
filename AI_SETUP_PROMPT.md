# AI Setup Assistant Prompt

[English](AI_SETUP_PROMPT.md) | [繁體中文](AI_SETUP_PROMPT.zh-TW.md)

## How to use this prompt

1. Copy everything inside the prompt below.
2. Open the AI assistant you normally use.
3. Paste the prompt into a new conversation.
4. Follow the instructions one step at a time.
5. If you are unsure about something, ask questions or provide a screenshot of what you see.

> ⚠️ Never send your Discord Webhook URL, passwords, access tokens, or other secret information to an AI assistant.

## Copy this prompt

```text id="mdvzra"
I want to set up the open-source project "YouTube Community Posts to Discord."

Project repository:
https://github.com/MuShuangLi/youtube-community-posts-to-discord

I have little or no experience with GitHub or programming.

Please help me set up this project from beginning to end.

Before we begin, read the project's README and installation instructions if you are able to access the repository.

If you cannot access the repository or its README, tell me that clearly and ask me to provide the relevant README content or screenshots. Do not guess the project's setup instructions.

Please follow these rules while helping me:

1. Guide me through only ONE step at a time.

2. After giving me a step, STOP and wait for me to confirm that I completed it or provide a screenshot before continuing.

3. Do not assume I understand GitHub or programming terminology.

4. When terms such as Repository, Fork, GitHub Actions, Workflow, Secret, Variable, Webhook, or Channel ID appear for the first time, explain them briefly in beginner-friendly language.

5. Tell me exactly which website or page I should be on, what button or menu I should look for, and what I should expect to see.

6. If my GitHub, Discord, or YouTube interface looks different from the instructions, use the screenshot or description I provide to help me locate the correct option. Do not invent buttons that are not visible.

7. Never ask me to paste or reveal my Discord Webhook URL, password, access token, GitHub Secret, or other secret information into the conversation.

8. If I show a screenshot, check whether it accidentally contains secret information before discussing it. If it does, tell me what should be regenerated or secured.

9. The Discord Webhook URL must be stored in a GitHub Actions repository secret named exactly:

DISCORD_WEBHOOK_URL

10. The YouTube Channel ID must be stored in a GitHub Actions repository variable named exactly:

YOUTUBE_CHANNEL_ID

11. Do not tell me to put either value directly into check_posts.py or main.yml.

12. Do not modify check_posts.py or .github/workflows/main.yml unless the repository's current instructions or code actually require a fix.

13. Help me verify GitHub Actions Workflow permissions so the workflow can update seen_posts.json.

14. Explain that the first successful workflow run establishes the initial seen-post history and should NOT send all existing old YouTube Community Posts to Discord.

15. After the initial run succeeds, help me test the project by publishing a new YouTube Community Post and checking whether Discord receives exactly one notification for that new post.

16. If an error occurs, help me inspect the GitHub Actions log before suggesting code changes.

17. Do not make multiple unrelated changes at once. Diagnose one problem at a time.

18. If the project documentation and the current website interface disagree, tell me about the discrepancy instead of silently changing the procedure.

19. When the setup is complete, help me verify that:
- the workflow runs successfully,
- seen_posts.json is being updated,
- old posts are not being sent as new notifications,
- new posts are sent to the intended Discord channel,
- and the automatic schedule is enabled.

Start by explaining, in simple terms, what this project does.

Then give me ONLY the first setup step and wait for my response.
```

## Important

AI assistants can make mistakes, and GitHub, Discord, or YouTube may change their interfaces over time.

If the AI's instructions conflict with this repository's current documentation, check the repository documentation first and ask the AI to re-evaluate the discrepancy.

Never share your Discord Webhook URL or other secret credentials in screenshots, public Issues, comments, or AI conversations.
