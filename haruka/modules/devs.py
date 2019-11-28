import os

from telegram.error import BadRequest, Unauthorized
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html

from haruka import dispatcher, OWNER_ID
from haruka.__main__ import STATS, USER_INFO
from haruka.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from haruka.modules.helper_funcs.extraction import extract_user
from haruka.modules.helper_funcs.filters import CustomFilters

# This module was picked up from Emilia Hikari

@run_async
def reboot(bot: Bot, update: Update):
	msg = update.effective_message
	chat_id = update.effective_chat.id
	update.effective_message.reply_text("Rebooting...", parse_mode=ParseMode.MARKDOWN)
	try:
		os.system("cd /home/ayra/emilia/ && python3.8 -m haruka &")
		os.system('kill %d' % os.getpid())
		update.effective_message.reply_text("Reboot successful!", parse_mode=ParseMode.MARKDOWN)
	except:
		update.effective_message.reply_text("Reboot failed!", parse_mode=ParseMode.MARKDOWN)

@run_async
def executor(bot: Bot, update: Update):
	msg = update.effective_message
	if msg.text:
		args = msg.text.split(None, 1)
		code = args[1]
		chat = msg.chat.id
		try:
			exec(code)
		except Exception as error:
			bot.send_message(chat, "*Failed:* {}".format(error), parse_mode="markdown", reply_to_message_id=msg.message_id)


REBOOT_HANDLER = CommandHandler("reboot", reboot, filters=Filters.user(OWNER_ID))
EXEC_HANDLER = CommandHandler("hitsuki", executor, filters=Filters.user(OWNER_ID))

dispatcher.add_handler(REBOOT_HANDLER)
dispatcher.add_handler(EXEC_HANDLER)