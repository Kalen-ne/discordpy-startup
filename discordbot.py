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

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        reply = (f"{message.author.mention}呼ばれたのでRIOT歌いますｗｗｗｗC o m e　i n t o　t h e　w o r l d \n 降　り　立　つ　姿　は \n 絶　大　な　輝　き　の \n f a n t a s t i c　a r t \n 至　高　の　音　楽　を　味　わ　え　と \n L e t　m e　s h o w　y o u \n 酔　い　し　れ　れ　ば　い　い \n 僕　ら　の　音　は \n 世　界　へ　と　憑　依　す   る")
        await message.hannel.send(reply)

@bot.command(name="riot")
async def riot(ctx):
    await ctx.send(f"C o m e　i n t o　t h e　w o r l d \n 降　り　立　つ　姿　は \n 絶　大　な　輝　き　の \n f a n t a s t i c　a r t \n 至　高　の　音　楽　を　味　わ　え　と \n L e t　m e　s h o w　y o u \n 酔　い　し　れ　れ　ば　い　い \n 僕　ら　の　音　は \n 世　界　へ　と　憑　依　す   る")

@bot.command(name="opera")
async def opera(ctx):
    await ctx.send(f"ｲｸｰｵｰｸｰwwwｲｸｰｾｰﾝｰwwwﾂﾑｲﾀﾞｰwwwｷｾｰｷｰﾆｨｨｨｨｨwww(ｽﾃｪｯﾌﾟwﾊﾞｲwｽﾃｪｯﾌﾟwww)ﾃﾞｪｪｪﾝｾｰﾂｰﾊｰwwwｺｺｶｰﾗｧｧｧwwwwｳﾏｰﾚｰﾀｰwwww")

@bot.command(name="unstoppable")
async def unstoppable(ctx):
    await ctx.send(f"ウザったいとジレったいが甘えて\nJust 承認欲求 every day 止まらない\n僕と僕は共犯者さ\n偽物と踊れ踊れ(Lullaby)\n迷いと不安が舌を出して\nコチラを指さし嘲る\nAre you enjoying？Are you excited？\n…Yes？そう見えるの？\nじゃあ…それでいい")

@bot.command(name="atoz")
async def atoz(ctx):
    await ctx.send(f"ｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwwwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwwwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwwwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwwwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwwwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwwwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾃｰwﾝｰwｶｰwｦｰwｴｰﾄｩｰｯｾﾞwｴｰﾄｩｰｯｾﾞwﾂｰwﾅｰwｲｰwﾃﾞｰwｱｯﾊﾟﾚﾅwｼﾞﾝｾｪｲwwｺｯｺﾝﾄｳｻﾞｧｲﾏｧﾃﾞwｱｲｯwwﾕﾒｯwwｻｧｻｧｹﾞﾏｧｯｽwww")

@bot.command(name="kiseki")
async def kiseki(ctx):
    await ctx.send(f"ｱ-ﾘｨｨｨwwwｶﾞﾄｫｫｫwww' ﾏﾜﾙwwwﾁｷｭｳwwwｱ-ﾅ-ｧﾀｧﾄｫｫｫ↑ﾜﾀｼｨ↓ﾊｽｽﾑｩｩｩwwwﾆｷﾞﾙｩﾃｪwwwﾊﾅﾚｪｪｪﾃﾓｫwwwｵﾜﾗﾅｨwwwｷｽﾞﾅｶﾞｱﾙｩ↑wwwwwﾀﾞﾝwﾀﾞﾝwﾀﾞﾝwﾀﾞﾝwﾀﾞﾝwﾀﾞﾝwﾄｩwﾃｨﾝ↑wwwww")

@bot.command(name="yakitori")
async def yakitori(ctx):
    await ctx.send(f"ﾏﾘﾅｰwwwwﾏﾘﾅｰwwwwwwLALAN(ﾕｳｾﾝ)wwwﾗﾝwﾗﾝwﾗﾝwLALAN(ﾀﾞｲｱﾙｱｯﾌﾟ)wwwwﾗﾝwwﾗﾝwwﾗﾝwwLALAN(ﾑｾﾝ)wwwwwﾗﾝwwwﾗﾝwwwﾗﾝwwwLALAN(ﾐﾀｹ)wwwwwwﾗﾝwwwwﾗﾝwwwwﾗﾝwwww")

@bot.command(name="riot2")
async def riot2(ctx):
    await ctx.send(f"┻┳|ﾁﾗｯ\n┳┻|∧\n┻┳|･ω･)\n┳┻|⊂ﾉ\n┻┳|Ｊ\n┳┻|\n┻┳|ｳｽﾞｳｽﾞ\n┳┻|∧\n┻┳|･ω･)\n┳┻|⊂ﾉ\n┻┳|Ｊ\n┳┻|\n┻┳|ｽｯ\n┳┻|∧\n┻┳│･ -・)\n┳┻|⊂ﾉ\n┻┳|Ｊ\n┳┻|\n┻┳|\n┳┻|∧\n┻┳|º дº)< C o m e  t o t h e  w o r l d\n┳┻|⊂ﾉ　      降 り 立 つ 姿 は \n┻┳|Ｊ")

@bot.command(name="arisa")
async def arisa(ctx):
    await ctx.send(f"ちょままちょまままっ！ｗｗｗｗｗｗｗｗｗｗｗｗちょまままままま！(戸山香澄を叩く音)ちょままァ！ちょままァァｧｧ！ちょまままァァｧｧ！ｗｗｗｗｗちょままーーー！！(戸山香澄を叩く音)ちょままままままままｗｗｗｗ")

@bot.command(name="confict")
async def confict(ctx):
    await ctx.send(f"ズォールヒ～～↑ｗｗｗｗヴィヤーンタースｗｗｗｗｗワース フェスツｗｗｗｗｗｗｗルオルｗｗｗｗｗプローイユクｗｗｗｗｗｗｗダルフェ スォーイヴォーｗｗｗｗｗスウェンネｗｗｗｗヤットゥ ヴ ヒェンヴガｒジョｊゴアｊガオガオッガｗｗｗじゃｇｊｊ")
@bot.command(name="USSR")
async def USSR(ctx):
    await ctx.send(f"Союз нерушимый республик свободных\n Сплотила навеки Великая Русь.\n Да здравствует созданный волей народов\n Единый, могучий Советский Союз!")

bot.run(token)
