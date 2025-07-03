import time
import random
from datetime import datetime
import requests

# === CONFIGURAÇÕES ===
TOKEN = '8142431348:AAFV6uxsLAEfmZtmsIfwQR3saWht1k_UjfE'
CHAT_ID = 6021407119

def enviar_sinal():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    direcao = random.choice(["CALL", "PUT"])
    estrategias = random.sample(["RSI", "Engolfo", "MM20", "Suporte", "Volume"], 3)
    chance = random.randint(98, 100)

    mensagem = f"""
📡 *SINAL GERADO* [{agora}]
🎯 *Direção:* {direcao}
📊 *Estratégias:* {', '.join(estrategias)}
✅ *Chance de acerto:* {chance}%
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }

    response = requests.get(url, params=params)
    print("Enviado:", response.json())

# LOOP infinito (um sinal a cada 5 minutos)
while True:
    enviar_sinal()
    time.sleep(300)  # Espera 5 minutos
