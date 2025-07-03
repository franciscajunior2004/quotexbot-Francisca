from telegram import Bot

# Configurações
TOKEN = '8142431348:AAFV6uxsLAEfmZtmsIfwQR3saWht1k_UjfE'
CHAT_ID = 6021407119  # Seu ID do Telegram

bot = Bot(token=TOKEN)

# Enviar mensagem simples de teste
bot.send_message(chat_id=CHAT_ID, text="✅ Bot conectado com sucesso, Mario!")
