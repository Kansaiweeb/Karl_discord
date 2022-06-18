from discord.ext import commands
import discord
from time import sleep


class Social(commands.Cog):

    __slots__ = ('bot',)

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rockandstone', aliases=['rocknstone', 'r&s'], description="ROCK AND STONE")
    async def rock_and_stone(self, ctx):
        # await ctx.trigger_typing()
        # await ctx.send("МЕДУЗАЛУПА")
        voice_channel = ctx.author.voice.channel
        channel = None
        if voice_channel is not None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="F:/ffmpeg/ffmpeg.exe", source="https://static.wikia.nocookie.net/deeprockgalactic_gamepedia_en/images/8/83/Saluting2_4.ogg"))
            # Sleep while audio is playing.
            while vc.is_playing():
                sleep(1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()