import discord
from discord.ext import commands
import requests
import pytz
from discord.ext import tasks, commands
import random
from datetime import datetime
import asyncio

bot = discord.Bot()
intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="a!", intents=intents)

admins = [756509638169460837]

# CHANNELS
fact_channel_id_debug = 1216056844506759278

# Path
facts_md = "src/facts/facts_list.md"
daily_count_file = "src/facts/daily_count.txt"
added_trivia_file = 'src/facts/added_trivia.json'
island_fact_database = 'src/facts/island_fact.json'
new_fact_path = 'src/facts/new_fact.txt'

# Staff Roles
mr_boomsteak = 1210006813945106492
developer = 1214469615808417812
head_of_operations = 1168385225349406771
assistant_director = 1151613202669514813
community_manager = 1175981569656225862
staff_manager = 1175986076125515786
head_administration = 1216518080889622538
senior_administration = 1216518078649860198
official_administration = 1216518079433936975
junior_administration = 1175985559743774791
trial_administration = 1175985971565694987
mr_boomsteaks_controller = 1151613201377677382
management_team = 1175984805620494426
head_of_moderation = 1216518081032093766
senior_moderator = 1175982839481782353
official_moderator = 1151613205089628212
junior_moderator = 1216506577251733615
trial_moderator = 1151613206939324578

# Links
island_base_url = "https://robloxislands.fandom.com"
embed_url = "http://144.76.143.198:8165/getEmbed"