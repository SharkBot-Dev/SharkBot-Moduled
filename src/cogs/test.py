import discord
from discord.ext import commands
from bot import SharkBot
from error.ModuleNotEnabled import ModuleNotEnabled

class TestCog(commands.Cog):
    def __init__(self, bot: SharkBot):
        self.bot = bot

        # モジュール設定
        self.module_name = "test"
        self.module_description = "テストモジュール"

    async def cog_check(self, ctx: commands.Context):
        is_enabled = await self.bot.module_manager.is_enabled(self.module_name)
        if not is_enabled:
            raise ModuleNotEnabled(self.module_name)
        
        return True

    async def cog_command_error(self, ctx: commands.Context, error):
        if isinstance(error, ModuleNotEnabled):
            return

    @commands.command(name="test")
    async def test(self, ctx: commands.Context):
        await ctx.reply('✅')

async def setup(bot):
    await bot.add_cog(TestCog(bot))