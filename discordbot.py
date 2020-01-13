from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(name="riot")
async def riot(ctx):
    await ctx.send(f"C o m e　i n t o　t h e　w o r l d \n 降　り　立　つ　姿　は \n 絶　大　な　輝　き　の \n f a n t a s t i c　a r t \n 至　高　の　音　楽　を　味　わ　え　と \n L e t　m e　s h o w　y o u \n 酔　い　し　れ　れ　ば　い　い \n 僕　ら　の　音　は \n 世　界　へ　と　憑　依　す   る")
    

bot.run(token)
