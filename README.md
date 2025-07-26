# 📰 Potato News — Discord News Bot

This is a simple and functional Discord bot that fetches the latest news and shares it in a Discord server. I built it to keep my community updated with real-time headlines — no need to go check any apps, the news comes to you.

---

##  What It Does

- Responds to `/news` with the latest top headlines
- `/start_news` begins an auto-posting loop for regular news updates
- `/stop_news` halts the auto-news feed
- Lightweight, fast, and no bloat

The idea was to keep the bot minimal but reliable — it only does one job, but does it well.

---

##  Why I Built This

In my own Discord server, I realized people talk a lot about current affairs but never really go look up the news themselves. So I decided to write a bot that brings the headlines to the chat automatically. It started as an experiment, but now it runs on multiple servers.

Also, I wanted to try working with:
- Slash commands
- Async event handling
- Logging (which you can see in `discord.log`)
- Scheduling tasks inside Discord bots

---

##  Commands

| Command         | Description                   |
|----------------|-------------------------------|
| `/news`         | Get the current top headlines |
| `/start_news`   | Start auto-posting news loop  |
| `/stop_news`    | Stop the news loop            |
| `/ping`         | Basic bot ping test           |

---

##  Built With

- Python 3
- `discord.py` (latest fork with slash command support)
- `requests` for news fetching
- AsyncIO for background looping
- Logging for debugging (see `discord.log`)

---

##  Learnings

This bot helped me understand:
- Discord’s bot architecture
- How to use slash commands
- Writing clean async Python
- The importance of logging and debugging

---

##  Notes

- You’ll need your own **Discord Bot Token** and **News API Key**.
- The bot is tested and works in production on live servers.
- Doesn’t spam. Clean, single-post-per-interval design.

---

##  Contact Me

If you want to talk bots, code, or want me to help you set it up in your server:

- 📧 agrawalvaradraj2007@gmail.com  
- 🐙 [GitHub @Varadraj75](https://github.com/Varadraj75)

---

##  Final Thought

I built this because it was **fun** and I wanted to **make something real**.  
That’s what coding is about.

Thanks for reading.
