
## Configs 

* `BOT_TOKEN`  - Get Bot Token From @BotFather

* `API_ID` - From my.telegram.org 

* `API_HASH` - From my.telegram.org

* `WEBHOOK` - If Your Server Is Need Web Service! Value = `True` Else Value = `False`

* `ADMIN` - AUTH Or Bot Controllers Id's Multiple Id Use Space To Split 

* `DB_URL`  - Mongo Database URL From https://cloud.mongodb.com

* `DB_NAME`  - Your Database Name From Mongodb. 

* `FORCE_SUB` - Your Force Sub Channel Username Without @

* `LOG_CHANNEL` - Bot Logs Sending Channel. If You Don't Need This To Remove This Variable In Your Server

* `START_PIC` - Start Message Photo. You Don't Need This! Just Skip

## Botfather Commands
```
start - 启动机器人活动检查
view_thumb - 查看缩略图
del_thumb - 删除缩略图
set_caption - 设置自定义标题
see_caption - 查看您的自定义标题
del_caption - 删除自定义标题
status - 检查机器人状态（仅限管理员）
```

## Install
```
# 拉取IAN-RENAME-BOT
git clone https://github.com/zbaiicn/YIAN-RENAME-BOT.git

# cd到项目
cd /root/YIAN-RENAME-BOT

# 创建python虚拟环境
python3 -m venv venv

# 激活python虚拟环境
source venv/bin/activate

# 安装项目所需依赖
pip install -r requirements.txt

# 前端运行调试（Ctrl+C 停止）
python bot.py

# 后台运行项目
nohup python bot.py &
```
