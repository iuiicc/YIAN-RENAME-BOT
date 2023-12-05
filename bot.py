from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()     
        print(f"{me.first_name} 已启动.....✨️")
        for id in Config.ADMIN:
            try: await self.send_message(id, f"**__{me.first_name}  已启动.....✨️__**")                                
            except: pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Shanghai"))
                date = curr.strftime('%Y年%m月%d日')
                time = curr.strftime('%p %I:%M:%S')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} 已重启 !!**\n\n📅 日期 : `{date}`\n⏰ 时间 : `{time}`\n🌐 时区 : `Asia/Shanghai`\n\n🉐 版本 : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("请确保此用户是您日志频道的管理员")

Bot().run()

