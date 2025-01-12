from discord import Embed
from discord.ext.commands import Bot, Context, command
from os import listdir
import json

from helpers.ui import UI

def get_max_page(total: int, batch: int):
    max_page = 1
    for index in range(total):
        if (index + 1) % batch == 0:
            max_page += 1

    return max_page

def load_setting_file():
    with open('storage/setting.json') as file:
        return json.load(file)

def get_pinned_galery_channel(bot: Bot):
    data = load_setting_file()
    return bot.get_channel(data['pinned-gallery-channel'])

def get_bot_dev_channel(bot: Bot):
    data = load_setting_file()
    return bot.get_channel(data['bot-dev-channel'])

def get_anonymous_channel(bot: Bot):
    data = load_setting_file()
    return bot.get_channel(data['anonymous-channel'])

def get_ruang_pribadi_channel(bot: Bot):
    data = load_setting_file()
    return bot.get_channel(data['ruang-pribadi-channel'])

def get_auto_voice_category(bot: Bot):
    data = load_setting_file()
    return bot.get_channel(data['auto-voice-category'])

@command(name='loadall')
async def loadall(ctx: Context):
    async with ctx.typing():
        for filename in listdir('./cogs'):  
            if filename.endswith('.py'):
                try: ctx.bot.load_extension(f'cogs.{filename[:-3]}')
                except: pass
        
    await ctx.send(embed=UI.success_embed("Semua cogs sudah berhasil Dimuat"))

@command(name='unloadall')
async def unloadall(ctx: Context):
    async with ctx.typing():
        for filename in listdir('./cogs'):  
            if filename.endswith('.py'):
                try: ctx.bot.unload_extension(f'cogs.{filename[:-3]}')
                except: pass

    await ctx.send(embed=UI.success_embed("Semua cogs sudah berhasil dilepas"))
