#A Discord bot designed by William Castello starting in July 2023. This is a passion project and is not designed to be a super in depth or high tech bot.
#Instead the main idea behind this bot is that I want to do stuff with my friends in discord, and an AIO bot is far easier to use than a ton of bots used for a ton of reasons. 
import discord
from discord.ext import commands, tasks 


#bot setup parameters:
bot_token = "YOUR TOKEN HERE" #The bot's "password" so to speak
text_channel_id = 1234 #This is the ID associated with the text testing channel in my server
voice_channel_id = 1234 #This is the ID associated with the voice testing channel in my server
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) #creates a prefix of "!" and allows for bot.commands instead of needing commands.command. 


#Commands and Connections:#
#First connection event designed to announce connection + version info
@bot.event
async def on_ready():
    print("Online") #prints to command line 
    channel = bot.get_channel(text_channel_id) #accesses the correct channel
    await channel.send ("Hello! Uni-Bot is now online.\nVersion Info: Beta 1") #sends a message into the channel which was picked above


#!repeat command designed to repeat user input. 
@bot.command()
async def repeat(ctx, arg): #defines the command used to make the users repeat after the user typing. 
    await ctx.send(arg) #repeats what was said by the user, using the syntax !repeat "yourtexthere", then it will print out who said it. 


#!quote command designed to quote whatever the user types to the bot.
@bot.command()
async def quote (ctx,arg):
    whosaid = str (ctx.author)
    await ctx.send("'" + arg + "'\n-" + whosaid) #quotes what was said by the user, using the syntax !quote "yourtexthere", then it will print out who said it. 

@bot.command()
async def join (ctx): #command to join the VC
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send(str(ctx.author) + " you are not in a voice channel! Join one and then try again. ")

@bot.command() 
async def leave (ctx): #command to leave the VC
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Uni-Bot has left the voice channel.")
    else:
        await ctx.send ("Uni-Bot is not connected a voice channel!")

@bot.command() #work in progress count command for levels associated with how much someone speaks.
async def count(ctx):
    who = ctx.message.author
    num = 0
    for i in range(num):
        if num == 10:
            await ctx.send(str(ctx.author)+" has spoken 10 times")
        if (ctx.message.author == who) & (num < 10):
            num = num + 1
        else:
            num = num
        


    



bot.run(bot_token)