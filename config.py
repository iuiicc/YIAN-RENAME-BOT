import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # 客户端配置
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # 数据库配置
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # 其他配置
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ))

    # web响应配置     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))



class Txt(object):
    # 文本配置的一部分
    START_TXT = """<b>嗨 {} 👋，
这是一个高级且功能强大的重命名机器人。
使用这个机器人，您可以重命名和更改文件的缩略图。
您还可以将视频转换为文件，文件转换为视频。
此外，该机器人还支持自定义缩略图和自定义标题。
此机器人由 @ovoozo 制作 💞</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 我的名字: {}
├🖥️ 开发者: <a href=https://t.me/@ovoozo>ovoozo</a> 
├✏️ 语言: <a href=https://www.python.org>Python 3</a>
├💾 数据库: <a href=https://cloud.mongodb.com>MongoDB</a>
├📊 构建版本: <a href=https://github.com/zbaiicn/YIAN-RENAME-BOT>Yian Renamer V3.2.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>如何设置缩略图</u></b>
  
<b>•»</b> /start 启动机器人并发送任何照片以自动设置缩略图。
<b>•»</b> /del_thumb 使用此命令删除您的旧缩略图。
<b>•»</b> /view_thumb 使用此命令查看您当前的缩略图。
📑 <b><u>如何设置自定义标题</u></b>
<b>•»</b> /set_caption - 使用此命令设置自定义标题。
<b>•»</b> /see_caption - 使用此命令查看您的自定义标题。
<b>•»</b> /del_caption - 使用此命令删除您的自定义标题。
示例：/set_caption 📕 文件名: {filename}
💾 大小: {filesize}
⏰ 持续时间: {duration}
✏️ <b><u>如何重命名文件</u></b>
<b>•»</b> 发送任何文件并键入新文件名，选择格式 [document, video, audio]。           
ℹ️ 任何其他帮助联系： <a href=https://t.me/@ovoozo> 项目作者</a>
"""


    DEV_TXT = """<b><u>ovoozo</b></u>
» 项目代码 : <a href=https://github.com/zbaiicn/YIAN-RENAME-BOT>Yian Renamer Bot</a>
» 如何制作 : <a https://github.com/zbaiicn/YIAN-RENAME-BOT>Yian Renamer Bot</a>
• ❣️ <a href=https://github.com/zbaiicn>zbaiicn</a>"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰进度条❱━➣
┣⪼ 🗃️ 大小: {1} | {2}
┣⪼ ⏳️ 已完成: {0}%
┣⪼ 🚀 速度: {3}/s
┣⪼ ⏰️ 预计剩余时间: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
