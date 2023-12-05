## 演示
https://t.me/@YIAN_RENAME_BOT

## 配置

* `BOT_TOKEN` - 从 @BotFather 获取机器人令牌

* `API_ID` - 从 my.telegram.org 获取

* `API_HASH` - 从 my.telegram.org 获取

* `WEBHOOK` - 如果您的服务器需要 Web 服务，则值为 True，否则值为 False

* `ADMIN` - 管理员的 ID，多个 ID 请使用空格分隔

* `DB_URL` - 从 https://cloud.mongodb.com 获取的 MongoDB 数据库 URL

* `DB_NAME` - 从 MongoDB 获取的数据库名称

* `FORCE_SUB` - 强制订阅频道的用户名，不需要 @

* `LOG_CHANNEL` - 用于发送机器人日志的频道。如果您不需要，请在您的服务器中删除此变量

* `START_PIC` - 启动消息照片。如果您不需要，可以跳过此项

## Botfather 命令
```
start - 启动机器人活动检查
view_thumb - 查看缩略图
del_thumb - 删除缩略图
set_caption - 设置自定义标题
see_caption - 查看您的自定义标题
del_caption - 删除自定义标题
status - 检查机器人状态（仅限管理员）
```

## 安装
```
# 拉取YIAN-RENAME-BOT
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
