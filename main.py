import discord
import logging
from discord.ext import tasks
import os
import requests
import random
import datetime, time

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

activity = discord.Activity(name='news', type=discord.ActivityType.watching)

bot = discord.Bot(activity=activity)
id = 1122825721547599882


@bot.event
async def on_ready():
  print(f"{bot.user} is read to go!")
  global startTime
  startTime = time.time()


@bot.slash_command(name="ping", description="Responds with Pong!")
async def ping(ctx):
  uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
  await ctx.respond(
      f"Pong! Latency is {round(bot.latency * 1000)} ms\nUptime: {uptime}")


@bot.slash_command(name="news", description="Respons with current news")
async def news(ctx):
  try:
    response = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&apiKey=41009e7f277149fd8b6d6e3692b7c1ed"
    )
    articles = response.json()["articles"]
    if not articles:
      await ctx.respond("No news articles available at the moment.")
      return

    n = random.randrange(0, min(19, len(articles)))
    article = articles[n]

    title = article["title"]
    snippet = article.get("description", "No description available")
    url = article["url"]
    imgUrl = article.get("urlToImage")
    source = article["source"]["name"]
    author = article.get("author", "Unknown")

    newsEmbed = discord.Embed(title=title,
                              description=f"{snippet}\n[Read More]({url})",
                              color=discord.Color.green())
    if imgUrl:
      newsEmbed.set_image(url=imgUrl)
    newsEmbed.set_footer(text=f"Source: {source}")
    newsEmbed.set_author(name=author)
    await ctx.respond(embed=newsEmbed)
    print(f"News article with the title {title} has been sent.")
  except Exception as e:
    await ctx.respond("An error occurred while fetching news.")
    print(f"Error in news command: {str(e)}")


@bot.slash_command(name="start_news", description="Starts the news loop")
async def start_news(ctx):
  if (ctx.author.id == 389306174119608321) or (
      ctx.author.id == 925231204104568953) or (ctx.author.id
                                               == 577775225723158538):
    await ctx.respond("Starting news loop...")
    print("News Loop Started")
    newsPeriodic.start()
  else:
    await ctx.respond("You are not authorized to use this command.")


@bot.slash_command(name="stop_news", description="Stops the news loop")
async def stop_news(ctx):
  if (ctx.author.id == 389306174119608321) or (
      ctx.author.id == 925231204104568953) or (ctx.author.id
                                               == 577775225723158538):
    await ctx.respond("Stopping news loop...")
    newsPeriodic.stop()
  else:
    await ctx.respond("You are not authorized to use this command.")


@tasks.loop(minutes=0.1)
async def newsPeriodic():
  try:
    response = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&apiKey=41009e7f277149fd8b6d6e3692b7c1ed"
    )
    articles = response.json()["articles"]
    if not articles:
      print("No articles available")
      return

    n = random.randrange(0, min(19, len(articles)))
    article = articles[n]

    title = article["title"]
    snippet = article.get("description", "No description available")
    url = article["url"]
    imgUrl = article.get("urlToImage")
    source = article["source"]["name"]
    author = article.get("author", "Unknown")

    newsEmbed = discord.Embed(title=title,
                              description=f"{snippet}\n[Read More]({url})",
                              color=discord.Color.green())
    if imgUrl:
      newsEmbed.set_image(url=imgUrl)
    newsEmbed.set_footer(text=f"Source: {source}")
    newsEmbed.set_author(name=author)

    channel = bot.get_channel(id)
    if channel is not None:
      await channel.send(embed=newsEmbed)
      print(f"News article with the title {title} has been sent.")
    else:
      print("Channel not found")
  except Exception as e:
    print(f"Error in newsPeriodic: {str(e)}")


bot.run("MTI1MTk0NzQzNzM4MDIwNjc1NQ.GuJvpH.eaTBlodPilO5FCGMW_mfSsvJc1d1P2ReztfI_g")