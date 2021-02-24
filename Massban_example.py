# WARNING!
# DO NOT use this script for malicious purposes!
# Author:Alpha®#0001

import discord
import asyncio
from discord.ext import commands

token = 'YOUR BOTS TOKEN'

client = discord.Client()

client = commands.Bot(command_prefix = ';')



@client.event
async def on_ready():
    print('Bot is online')
    
    
    
    
# Mass Banning Users that have a specific role
@client.command()
@commands.is_owner()
async def massroleban(ctx,rolename: discord.Role):
    for role in rolename.members:
        try:
            await role.ban(reason="Any reason", delete_message_days=7)
            await ctx.send(f"All users with {rolename} have been banned")
        except:
            pass

        
        
#Mass Banning all discord server Users
@client.command()
@commands.is_owner()
async def massban(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban(reason="Any reason", delete_message_days=7)
            await ctx.send(f"All users have been banned")
        except:
            pass
        
        
client.run(token)
