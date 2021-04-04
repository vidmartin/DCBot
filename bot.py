import discord
from discord.ext import commands
import logging
import requests as r
import traceback
from json import loads

TOKEN = "ODE4ODk5MjkxMDQ4Mzc4NDIx.YEexZQ.KnLZNtYCxu-pwBQzqWAx7oRGoQo"
debug = False

DELETE_TIME = 20.0
ADMIN = 470490558713036801

if debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


bot = commands.Bot(command_prefix="-", owner_id=ADMIN, intents=discord.Intents.all())


# Nickname changer
@bot.command(name="nick")
@commands.guild_only()
async def change_nick(ctx: commands.context, target: discord.Member, *, nick: str = None):
    nick = nick.strip()
    if len(nick) > 32:
        await ctx.send("Přezdívka může mít maximálně 32 charakterů", delete_after=DELETE_TIME)
        return
    before = target.display_name
    try:
        await target.edit(nick=nick, reason="Změnil {0.author.name} v kanálu {0.channel.name}".format(ctx))
    except discord.Forbidden:
        await ctx.send("Nemám právo měnit tuto přezdívku")
    else:
        await ctx.send("Změněno z '{0}' na '{1}' uživatelem `{2}`".format(before, nick, ctx.author.name))

@change_nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Uživatel nebyl nalezen")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Příkaz se zadává ve formátu `-nick cíl 'přezdívka'`")
    else:
        await ctx.send("neočekávaná chyba <@470490558713036801>")
        traceback.print_exc()


@bot.command(name="among")
async def among_get_active(ctx: commands.context):
    url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=945360"
    info = r.get(url)
    if info.status_code != 200:
        await ctx.send("Chyba při získávání informací od Steamu")
        return
    info = loads(info.text)
    stats = info["response"]
    await ctx.send("Among Us právě hraje {0} hráčů".format(stats["player_count"]))
    return


@bot.command(name="exit")
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Jdu spát")
    for guild in bot.guilds:
        if guild.voice_client:
            await guild.voice_client.disconnect()
            guild.voice_client.cleanup()
    await bot.close()
    exit(1)


@bot.event
async def on_ready():
    logging.info("I'm ready! {0.name}".format(bot.user))
    for guild in await bot.fetch_guilds().flatten():
        logging.info("Connected to {0}".format(guild.name))

    admin: discord.User = await bot.fetch_user(bot.owner_id)
    logging.info("Owner is: {0}".format(admin.name))
    logging.info("---------\nINFO:root:Ready")


@bot.event
@commands.has_role(770453970165694545)
async def on_member_update(before: discord.Member, after: discord.Member):
    if before == discord.Status.offline and after.status is not before.status:
        await after.add_roles(None, reason="Viditelný status")
    elif



async def on_message(self, message: discord.Message):

    await self.Voter.handle_message(message)
    await self.Monika.handleMessage(message)
    await self.Player.handle_message(message)

    return


async def check_activity(self, message: discord.Message) -> None:

    if self.klacek_role in message.author.roles and message.author.status == discord.Status.offline and self.active_role in message.author.roles:
        await message.author.remove_roles(self.active_role, reason="Neviditelný status")
        return
    elif self.klacek_role in message.author.roles and message.author.status == discord.Status.online and self.active_role not in message.author.roles:
        await message.author.add_roles(self.active_role, reason="Viditelný status")
        return
    return

bot.run(TOKEN)
