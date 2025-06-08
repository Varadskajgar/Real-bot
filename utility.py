import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def announce(self, ctx, channel: discord.TextChannel):
        embed = discord.Embed(
            title="🏆 FREE FIRE TOURNAMENT ANNOUNCEMENT 🏆",
            description=(
                "**🔥 FREE & PAID EVENTS ARE HERE! 🔥**\n\n"
                "🎯 **FREE TOURNAMENTS**\n"
                "➤ No Entry Fee!\n"
                "➤ Open to all players.\n\n"
                "💰 **PAID TOURNAMENTS**\n"
                "➤ Entry Fee: ₹5 only\n"
                "➤ Win ₹10 (double reward!)\n\n"
                "🎮 **HOW TO JOIN?**\n"
                "Click the **Join Tournament** button below!\n"
                "We’ll DM you all match details after joining.\n\n"
                "⚔️ Fight Hard, Win Big!"
            ),
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow()
        )

        join_button = discord.ui.Button(
            label="🎯 Join Tournament",
            style=discord.ButtonStyle.green,
            custom_id="join_tournament"
        )

        view = discord.ui.View()
        view.add_item(join_button)

        await channel.send(embed=embed, view=view)
        await ctx.send(f"✅ Tournament announcement sent to {channel.mention}")

    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Utility(bot))
