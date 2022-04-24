import discord
import os
from discord.ext import commands
from replit import db
from myhoster import keep_alive

TOKEN = os.environ["TOKEN"]

client = commands.Bot(command_prefix="./", allowed_mentions=discord.AllowedMentions(replied_user=False), activity=discord.Activity(type=discord.ActivityType.listening, name="./help"))

client.remove_command("help")

@client.event
async def on_ready():
    print("BOT IS READY")

@client.command(pass_context = True)
async def help(ctx):
    myembed = discord.Embed(title = "Help", color = discord.Color.blue())
    myembed.add_field(name="./init", value="Creates counter", inline=False)
    myembed.add_field(name="./plus (or) ./+", value="Adds to counter", inline=False)
    myembed.add_field(name="./minus (or) ./-", value="Removes from counter", inline=False)
    myembed.add_field(name="./counter (or) ./c", value="Displays counter", inline=False)
    myembed.add_field(name="./delete (or) ./del", value="Deletes counter", inline=False)
    await ctx.reply(embed=myembed)

@client.command(name="init")
async def init(ctx, arg=None):
    if arg is None:
        await ctx.reply("No name entered!")
    else:
        db[f"{arg}"] = "0"
        myembed = discord.Embed(title = "Init", description = "Counter created", color = discord.Color.blue())
        await ctx.reply(embed=myembed)

@client.command(name="plus", aliases=["+"])
async def plus(ctx, name, arg=1):
    ck = int(db[f"{name}"]) + arg
    db[f"{name}"] = f"{ck}"
    await counter(ctx, name)

@client.command(name="minus", aliases=["-"])
async def minus(ctx, name, arg=1):
    ck = int(db[f"{name}"]) - arg
    db[f"{name}"] = f"{ck}"
    await counter(ctx, name)

@client.command(name="counter", aliases=["c"])
async def counter(ctx, cname=None):
    if not db.keys():
        await ctx.reply("Empty!")
    elif cname is None:
        myembed = discord.Embed(title="Counter List", color = discord.Color.blue())
        for n in db.keys():
            myembed.add_field(name = f"{n}", value = db[f"{n}"], inline=False)
            await ctx.reply(embed=myembed)
    else:
        myembed = discord.Embed(title = f"{cname}", description = db[f"{cname}"], color = discord.Color.blue())
        await ctx.reply(embed=myembed)

@client.command(name="delete", aliases=["del"])
async def delete(ctx, arg=None):
    if arg is None:
        await ctx.reply("No name entered!")
    else:
        del db[f"{arg}"]
        myembed = discord.Embed(title = "Delete", description = "Counter deleted", color = discord.Color.blue())
        await ctx.reply(embed=myembed)

keep_alive()
client.run(TOKEN)
