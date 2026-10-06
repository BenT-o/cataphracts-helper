from d20 import RollSyntaxError
from discord.ext import commands
import d20

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, *, expression: str):
        print("Roll Command Received")
        print(f"expression: {expression}")
        try:
            result = d20.roll(expression, allow_comments=True)
            await ctx.reply(
                f"{ctx.author.mention} rolled **{result.total}**\n"
                f"{result}"
            )

        except ValueError as e:
            print(f"ERROR: {e}")
            await ctx.reply(f"ERROR: {e}")

        except RollSyntaxError as e:
            print(f"ERROR: {e}")
            await ctx.reply(f"Syntax Error: `{e}`")

async def setup(bot):
    await bot.add_cog(Dice(bot))