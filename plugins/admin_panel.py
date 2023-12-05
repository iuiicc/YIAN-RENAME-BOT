from config import Config
from helper.database import db
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import os, sys, time, asyncio, logging, datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 获取机器人状态信息的命令处理器
@Client.on_message(filters.command(["stats", "status"]) & filters.user(Config.ADMIN))
async def get_stats(bot, message):
    total_users = await db.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - bot.uptime))    
    start_t = time.time()
    st = await message.reply('**正在获取详情...**')    
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await st.edit(text=f"**--机器人状态--** \n\n**⌚️ 机器人运行时间:** {uptime} \n**🐌 当前延迟:** `{time_taken_s:.3f} 毫秒` \n**👭 总用户数:** `{total_users}`")

# 重新启动机器人的命令处理器
@Client.on_message(filters.private & filters.command("restart") & filters.user(Config.ADMIN))
async def restart_bot(b, m):
    await m.reply_text("🔄__正在重新启动...__")
    os.execl(sys.executable, sys.executable, *sys.argv)

# 广播消息的命令处理器
@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMIN) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    await bot.send_message(Config.LOG_CHANNEL, f"{m.from_user.mention} 或 {m.from_user.id} 开始了广播...")
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("广播开始..!") 
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await db.total_users_count()
    async for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
           success += 1
        else:
           failed += 1
        if sts == 400:
           await db.delete_user(user['_id'])
        done += 1
        if not done % 20:
           await sts_msg.edit(f"广播进度: \n总用户数 {total_users} \n完成: {done} / {total_users}\n成功: {success}\n失败: {failed}")
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"广播完成: \n完成于 `{completed_in}`.\n\n总用户数 {total_users}\n完成: {done} / {total_users}\n成功: {success}\n失败: {failed}")

# 向用户发送消息的异步函数
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : 用户停用")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : 用户阻止了机器人")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : 无效的用户ID")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500
