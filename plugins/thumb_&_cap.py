from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__请给出标题__\n\n示例：`/set_caption {filename}\n\n💾 大小: {filesize}\n\n⏰ 时长: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ 标题已保存**__")
   
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**😔 您没有任何标题**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**❌️ 标题已删除**__")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**您的标题：-**\n\n`{caption}`")
    else:
       await message.reply_text("__**😔 您没有任何标题**__")


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("😔 __**您没有任何缩略图**__") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ __**缩略图已删除**__")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("请稍候 ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("✅️ __**缩略图已保存**__")
