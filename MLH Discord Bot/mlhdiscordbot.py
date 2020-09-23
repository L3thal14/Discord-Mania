## Author: Karthik R
## Date: 15-08-2020

import os
import discord
from dotenv import load_dotenv
from bs4 import BeautifulSoup,element
import requests
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
URL = 'https://mlh.io/seasons/2021/events'

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='upcoming')
async def scrape_cases(ctx):

    res = '\n' + '**' + 'UPCOMING EVENTS' + '**' + '\n\n'

    source = requests.get(URL).text

    soup = BeautifulSoup(source,'lxml')

    upcomingevents = soup.findAll("div", {"class": "row"})
    for upcomingevents[2] in upcomingevents:
        upcoming = upcomingevents[2].find_all("div", {"class": "event-wrapper"})
        for upcomingevents[2] in upcoming:
            res += 'Hackathon Name: ' + upcomingevents[2].h3.text + '\n' + 'Dates: ' + upcomingevents[2].p.text + '\n' + 'Website: ' + '<' + upcomingevents[2].a.get("href") + '>' + '\n'
    await ctx.send(res)

@bot.command(name='past')
async def scrape_cases(ctx):

    resp = '\n' + '**' + 'PAST EVENTS' + '**' + '\n\n' 

    source = requests.get(URL).text

    soup = BeautifulSoup(source,'lxml')

    pastevents = soup.findAll("div", {"class": "row"})
    for pastevents[1] in pastevents:
        past = pastevents[1].find_all("div", {"class": "event-wrapper"})
        for pastevents[1] in past:
            resp += 'Hackathon Name: ' + pastevents[1].h3.text + '\n' + 'Dates: ' + pastevents[1].p.text + '\n' + 'Website: ' + '<' +  pastevents[1].a.get("href") + '>' + '\n'
    await ctx.send(resp)
@bot.command(name='help')
async def scrape_cases(ctx):
    response = '**' + 'COMMANDS LIST' + '**' + '\n' + '```' +  '!upcoming : Get Information about Upcoming Hackathons' + '```' + '```' + '!past : Get Information about Past Hackathons' + '```' + '\n' + '**' + 'Author : Karthik R' + '\n' + 'Github : ' + '<' + 'https://github.com/L3thal14' + '>'  + '**'

    await ctx.send(response)
bot.run('') # Add Discord Bot authentication Token from Discord Developer Portal