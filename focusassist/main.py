import discord
import sqlite3
import datetime as dt
import requests
import math
import asyncio
import os
from discord.ext import commands
from myhoster import keepalive

client = commands.Bot(command_prefix="./", allowed_mentions=discord.AllowedMentions(replied_user=False), activity=discord.Activity(type=discord.ActivityType.listening, name="./help"))
client.remove_command("help")
RANKS = ("Noob", "Trainee", "Pro", "Expert", "Elite", "Veteran", "Master", "Legend")
FOCUSING = {}

def returnexp(exp):
    global RANKS
    r = exp // 3600
    if r < 1:
        return RANKS[0]
    elif r < 2:
        return RANKS[1]
    elif r < 5:
        return RANKS[2]
    elif r < 10:
        return RANKS[3]
    elif r < 20:
        return RANKS[4]
    elif r < 30:
        return RANKS[5]
    elif r < 50:
        return RANKS[6]
    else:
        return RANKS[7]

@client.event
async def on_ready():
    print("BOT IS READY")

@client.command(pass_context = True)
async def help(ctx):
    myembed = discord.Embed(title = "Help", color = discord.Color.blue())
    myembed.add_field(name="./create", value="Creates an account", inline=False)
    myembed.add_field(name="./profile (or) ./p", value="Displays your account", inline=False)
    myembed.add_field(name="./startrun (or) ./sr", value="Starts timer for current work session", inline=False)
    myembed.add_field(name="./stoprun (or) ./str", value="Stops timer for current work session and displays session report", inline=False)
    myembed.add_field(name="./timer <arg> (or) ./t <arg>", value="""When <arg> is a postive integer, sets a countdown timer for <arg> minutes
    When <arg> is the string 'stop', stops the ongoing timer""", inline=False)
    myembed.add_field(name="./todo (or) ./td", value="Displays your to-do list", inline=False)
    myembed.add_field(name="./todoadd <task> <pos> (or) ./tda <task> <pos>", value="""Adds task your to-do list
    <task> is the name of the task within double quotes
    <pos> is the position at which you want to insert the task""", inline=False)
    myembed.add_field(name="./tododel <pos> (or) ./tdd <pos>", value="""Deletes a task from your to-do list
    <pos> is the position of the task to be deleted""", inline=False)
    myembed.add_field(name="./inspire (or) ./in", value="Provides inspirational quotes", inline=False)
    myembed.add_field(name="./delete", value="Deletes your account if you want to start over", inline=False)
    await ctx.reply(embed=myembed)

@client.command()
async def create(ctx):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    # make a new user
    cur.execute("INSERT INTO users (username, guildname, exp) values(?, ?, '0');", (ctx.author.name, ctx.author.guild.name))
    print("USER PROFILE CREATED SUCCESSFULLY")
    db.commit()
    db.close()
    await ctx.reply("Created! Use ./profile (or) ./p to see your profile!")

@client.command(name="profile", aliases=["p"])
async def profile(ctx):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    # retrieve user
    rows = cur.execute("SELECT id, username, guildname, exp FROM users WHERE username = ?;", (ctx.author.name,)).fetchall()
    print(f"PROFILE RETRIEVED")
    myembed = discord.Embed(title = f"{ctx.author.display_name}'s profile", description = f"{rows[0][2]}", color = discord.Color.blue())
    myembed.add_field(name="Name", value=f"{ctx.author.display_name}")
    myembed.add_field(name="Rank", value=f"{returnexp(int(rows[0][3]))}")
    myembed.add_field(name="Time", value=f"{int(int(rows[0][3])//3600)}:{int((int(rows[0][3])%3600)//60)}:{math.trunc(int(rows[0][3])%60)}")
    cur.close()
    db.close()
    await ctx.reply(embed = myembed)

@client.command(name="startrun", aliases=["sr"])
async def startrun(ctx):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    rows = cur.execute("SELECT username, starttime FROM focusing WHERE username = ?;", (ctx.author.name,)).fetchall()
    # check if run already started
    if rows:
        print("ERROR: WORK SESSION ALREADY IN PROGRESS")
        await ctx.reply("ERROR: Work session already in progress")
    else:
        # start a new work session
        cur.execute("INSERT INTO focusing (username, starttime) VALUES (?, ?);", (ctx.author.name, ctx.message.created_at))
        print(f"RUN STARTED")
        db.commit()
        cur.close()
        db.close()
        myembed = discord.Embed(title = f"Work Session", description = f"{ctx.author.guild}", color = discord.Color.blue())
        myembed.add_field(name=f"{ctx.author.display_name}", value="Started working")
        await ctx.reply(embed = myembed)

@client.command(name="stoprun", aliases=["str"])
async def stoprun(ctx):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    rows = cur.execute("SELECT username, starttime FROM focusing WHERE username = ?;", (ctx.author.name,)).fetchall()
    started = dt.datetime.strptime(rows[0][1], f'%Y-%m-%d %H:%M:%S.%f')
    tchange = (ctx.message.created_at - started).total_seconds()
    rows = cur.execute("SELECT username, exp FROM users WHERE username = ?;", (ctx.author.name,)).fetchall()
    cur.execute("UPDATE users SET exp = ? where username = ?;", (f"{round(int(rows[0][1]) + ((ctx.message.created_at - started).total_seconds()))}", ctx.author.name))
    db.commit()
    cur.execute("DELETE FROM focusing WHERE username = ?;", (ctx.author.name,))
    db.commit()
    print("RUN STOPPED")
    myembed = discord.Embed(title = f"Work Session", description = f"{ctx.author.guild}", color = discord.Color.blue())
    myembed.add_field(name=f"{ctx.author.display_name}'s Report", value=f"Worked for {int(tchange // 60)}:{(tchange % 60):.2f}")
    cur.close()
    db.close()
    await ctx.reply(embed=myembed)

@client.command(name = "timer", aliases = ["t"])
async def timer(ctx, mins):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    if ctx.author.name not in FOCUSING:
        FOCUSING[ctx.author.name] = False
    try:
        # var to keep track of time
        seconds = int(mins) * 60
        # handle negative and zero time
        if int(mins) <= 0:
            await ctx.reply("ERROR: Enter a positive integer no. of minutes!")
            print("ERROR: INVALID NUMBER OF MINUTES!")
        else:
            # check if run already started
            rows = cur.execute("SELECT username, starttime FROM focusing WHERE username = ?;", (ctx.author.name,)).fetchall()
            if rows:
                print("ERROR: WORK SESSION ALREADY IN PROGRESS")
                await ctx.reply("ERROR: Work session already in progress")
            else:
                # start a new work session
                cur.execute("INSERT INTO focusing (username, starttime) VALUES (?, ?);", (ctx.author.name, mins))
                db.commit()
                # message to user for starting timer
                myembed = discord.Embed(title = f"Work Session", description = f"{ctx.author.guild}", color = discord.Color.blue())
                myembed.add_field(name=f"{ctx.author.display_name}", value=f"Started timer for {int(mins) // 60}h:{(int(mins) % 60)}m")
                await ctx.reply(embed=myembed)
                print(f"TIMER STARTED")
                # var to count the seconds remaining
                seconds = int(mins) * 60
                FOCUSING[ctx.author.name] = True
                # loop runs every second
                while FOCUSING[ctx.author.name] == True:
                    seconds -= 1
                    if seconds <= 0:
                        FOCUSING[ctx.author.name] = False
                    # to ping the user periodically
                    elif seconds % 2700 == 0:
                        await ctx.send(f"{ctx.author.mention} you have {seconds // 3600}h:{seconds // 60}m left. Good work!")
                    await asyncio.sleep(1)
                # to update time spent into the db
                rows = cur.execute("SELECT username, exp FROM users WHERE username = ?;", (ctx.author.name,)).fetchall() 
                rows2 = cur.execute("SELECT username, starttime FROM focusing WHERE username = ?;", (ctx.author.name,)).fetchall()
                cur.execute("UPDATE users SET exp = ? where username = ?;", ((int(rows[0][1]) + (int(rows2[0][1]) * 60) - seconds), ctx.author.name))
                db.commit()
                cur.execute("DELETE FROM focusing WHERE username = ?;", (ctx.author.name,))
                db.commit()
                # to tell the user that timer is over
                myembed2 = discord.Embed(title = f"Work Session", description = f"{ctx.author.guild}", color = discord.Color.blue())
                myembed2.add_field(name=f"{ctx.author.display_name}'s Report", value=f"Worked for {((int(mins) * 60) - seconds) // 60} mins")
                await ctx.reply(embed=myembed2)
                print(f"TIMER STOPPED")
    except ValueError:
        # when user wants to stop
        if mins == "stop":
            FOCUSING[ctx.author.name] = False
        else:
            await ctx.reply("ERROR: Argument must be positive integer or string 'stop'")
            print("ERROR: INVALID ARG TYPE!")
        cur.close()
        db.close()

@client.command(name="todo", aliases=["td"])
async def todo(ctx):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    rows = cur.execute("SELECT taskid, task FROM todo WHERE username = ? ORDER BY taskid ASC;", (ctx.author.name,)).fetchall()
    if not rows:
        await ctx.reply("To-do list is empty! Add a task first")
        print("Empty to-do list")
    else:
        listformat = ""
        for row in rows:
            listformat += f"{row[0]}) {row[1]}\n"
        myembed = discord.Embed(title=f"{ctx.author.display_name}'s To-do List", description=f"`{listformat}`", color=discord.Color.blue())
        await ctx.reply(embed=myembed)
    cur.close()
    db.close()

@client.command(name="todoadd", aliases=["tda"])
async def todoadd(ctx, taskstr, pos):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    try:
        pos = int(pos)
        if pos <= 0:
            await ctx.reply("ERROR: Enter the position as a positive integer")
        else:
            cur.execute("INSERT INTO todo (taskid, task, username) VALUES (?, ?, ?);", (pos, taskstr, ctx.author.name))
            db.commit()
            await ctx.reply("Added task successfully! Use ./todo or ./td to view")
            print("Added task successfully!")
    except ValueError:
        print("ERROR: INT EXPECTED")
        await ctx.reply("ERROR: Enter the position as a positive integer")
    cur.close()
    db.close()

@client.command(name="tododel", aliases=["tdd"])
async def tododel(ctx, pos):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    try:
        pos = int(pos)
        if pos <= 0:
            await ctx.reply("ERROR: Enter the position as a positive integer")
        else:
            newnum = 0
            rows = cur.execute("SELECT taskid, task FROM todo WHERE taskid > ? AND username = ?;", (pos, ctx.author.name)).fetchall()
            # print(rows)
            if not rows:
                cur.execute("DELETE FROM todo WHERE taskid = ? AND username = ?;", (pos, ctx.author.name))
                db.commit()
            else:
                cur.execute("DELETE FROM todo WHERE taskid >= ? AND username = ?;", (pos, ctx.author.name))
                db.commit()
                for row in rows:
                    cur.execute("INSERT INTO todo (taskid, task, username) VALUES (?, ?, ?)", (pos + newnum, row[1], ctx.author.name))
                    db.commit()
                    newnum += 1
            await ctx.reply("Deleted task successfully! Use ./todo or ./td to view")
            print("Deleted task successfully!")
    except ValueError:
        print("ERROR: INT EXPECTED")
        await ctx.reply("ERROR: Enter the position as a positive integer")
    cur.close()
    db.close()

@client.command(name="inspire", aliases=["in"])
async def inspire(ctx):
    web_response = requests.get("https://zenquotes.io/api/random/")
    if web_response.status_code != 200:
        print("ERROR: QUOTE REQUEST FAILED")
        await ctx.reply("ERROR: Quote request failed")
    myembed = discord.Embed(title="Inspiration", description="Provided by [ZenQuotes](https://zenquotes.io/)", color=discord.Color.blue())
    myembed.add_field(name=f"{ctx.author.guild}" , value=f"*{web_response.json()[0]['q']}\n - {web_response.json()[0]['a']}*")
    await ctx.reply(embed=myembed)

@client.command()
async def delete(ctx):
    db = sqlite3.connect("bot3.db")
    cur = db.cursor()
    rows = cur.execute("DELETE FROM users WHERE username = ?;", (ctx.author.name,))
    print("USER PROFILE DELETED SUCCESSFULLY")
    db.commit()
    cur.close()
    db.close()
    await ctx.reply("Deleted! Use ./create to see start over!")

keepalive()
client.run(os.environ["BotToken"])