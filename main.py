import requests

# Teu token do bot
TOKEN = '8142431348:AAFV6uxsLAEfmZtmsIfwQR3saWht1k_UjfE'
# Teu ID do Telegram
CHAT_ID = 6021407119

# Mensagem de teste
mensagem = "🚀 Bot funcionando, Mario! Recebeu esse sinal?"

# URL de envio
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

# Enviar requisição
res = requests.get(url, params=params)

# Printar resposta no log
print("Resposta:", res.json())
