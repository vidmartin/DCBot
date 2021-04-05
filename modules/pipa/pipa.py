import discord
from discord.ext import commands

ALKOHOL = ["pivo", "pívo", "pivsoň", "piva", "pivečka", "pivu", "pivem", "pullitřík", "půllitřík", "půllitr",
                  "pivko", "rum", "vodka", "vodku"]


class Hostinsky(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if "čus" in message.content.lower():
            await message.channel.send("Čest práci soudruhu <@" + str(message.author.id) + ">")

        for key in ALKOHOL:
            if key in message.content.lower():
                await message.channel.send("Už se to nese!! 🍺")

        await self.bot.process_commands(message)

    @commands.command(name="jelimán")
    @commands.is_owner()
    @commands.guild_only()
    async def give_technik(self, ctx: commands.Context):
        role = self.bot.get_guild(765898623610912809).get_role(783695649488633877)
        try:
            await ctx.author.add_roles(role, reason="Je to borec a tuhle roli si kurva zaslouží!!!")
        except discord.NotFound:
            await ctx.send("Musíš si o ní napsat na správným serveru")