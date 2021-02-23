import discord

import brain
import formating
from settings import settings
from commands import commands, run_command

# Set up client for bot
client = discord.Client()

# Bot token
key = ""

# Get token for bot
with open(".token") as f:
	key = f.read()

# Set bot status to online
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online)
	print("The bot is ready")

"""
Every message we need to check that it is not from us, and if it is not we need
to then run the command if it is a command and then check if we are getting
pinged, if we are then we need to send a message and then we need to note down
the message send if it is not any of those things and then store it and choose
whether to respond
"""
@client.event
async def on_message(message):
	# Check if the message is from the bot itself
	if message.author == client.user:
		return

	# Check if message is a command
	if message.content.split(" ")[0].strip() in commands:
		# TODO: run command
		return
	"""
	TODO: Setup this
	"""


# Run the bot
client.run(key)