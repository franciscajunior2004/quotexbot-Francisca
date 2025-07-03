import time
from datetime import datetime
import random

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
    return sinais, total >= 2  # pelo menos 2 estratégias concordam

# Simulador de envio de sinal
def enviar_sinal(sinais, probabilidade):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    direcao = random.choice(["CALL", "PUT"])
    print(f"\n📡 SINAL GERADO [{agora}]")
    print(f"🎯 Direção: {direcao}")
    print(f"📊 Estratégias alinhadas: {', '.join([k for k,v in sinais.items() if v])}")
    print(f"✅ Probabilidade: {probabilidade}%")

# Loop principal
while True:
    sinais, confirmado = verificar_confluencia()
    if confirmado:
        probabilidade = random.randint(98, 100)
        enviar_sinal(sinais, probabilidade)
    else:
        print("⏳ Nenhum sinal confiável. Aguardando...")
    time.sleep(300)  # Espera 5 minutos (M5)
