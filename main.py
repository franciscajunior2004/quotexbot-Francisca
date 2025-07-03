import time
import random
from datetime import datetime
from telegram import Bot

# === CONFIGURAÇÕES ===
TOKEN = '8142431348:AAFV6uxsLAEfmZtmsIfwQR3saWht1k_UjfE'
CHAT_ID = 6021407119  # ID do teu Telegram @FranciscajuniorId

bot = Bot(token=TOKEN)

# Estratégias simuladas
def estrategia_rsi():
    return random.choice([True, False])

def estrategia_engolfo():
    return random.choice([True, False])

def estrategia_mm20():
    return random.choice([True, False])

# Verifica confluência de sinais
def verificar_confluencia():
    sinais = {
        "RSI": estrategia_rsi(),
        "Engolfo": estrategia_engolfo(),
        "MM20": estrategia_mm20()
    }
    total = sum(sinais.values())
    return sinais, total >= 2

# Enviar sinal via Telegram
def enviar_sinal(sinais, probabilidade):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    direcao = random.choice(["CALL", "PUT"])
    texto = f"""
📡 *SINAL GERADO* [{agora}]
🎯 *Direção:* {direcao}
📊 *Estratégias:* {', '.join([k for k,v in sinais.items() if v])}
✅ *Chance de acerto:* {probabilidade}%
"""
    bot.send_message(chat_id=CHAT_ID, text=texto, parse_mode="Markdown")

# Loop principal
while True:
    sinais, confirmado = verificar_confluencia()
    if confirmado:
        probabilidade = random.randint(98, 100)
        enviar_sinal(sinais, probabilidade)
    else:
        print("⏳ Nenhum sinal confiável. Aguardando...")
    time.sleep(300)  # Espera 5 minutos
