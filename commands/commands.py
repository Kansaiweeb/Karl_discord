from commands.cogs.music import Music
from commands.cogs.social import Social


def setup(bot):
    bot.add_cog(Music(bot))
    bot.add_cog(Social(bot))
