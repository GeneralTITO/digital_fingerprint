import logging
from telegram import Update
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from utils.verifications import load_verification
import asyncio

def run_bot():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=" Bem-vindo ao Bot de Controle de Ponto! 🤖✨Estarei mantendo você informado sobre os horários de entrada e saída dos funcionários.",
        )

    async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args[0] == "3771":
            
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text='ahhhhh lelek'
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text="Sorry, invalid password."
            )

    async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sorry, I didn't understand that command.",
        )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = (
        ApplicationBuilder()
        .token("6885228761:AAFRuATzqp429hCusBVOYfwDfIkZuqAc-sY")
        .build()
    )

    start_handler = CommandHandler("start", start)
    enviar_handler = CommandHandler("todas", start)
    caps_handler = CommandHandler("caps", caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(enviar_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
