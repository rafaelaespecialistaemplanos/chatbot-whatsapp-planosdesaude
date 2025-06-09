
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ZAPI_URL = "https://v5.chatpro.com.br/chatpro-xyz123/send-button-message"  # Substitua pelo seu endpoint real da Z-API
ZAPI_API_KEY = "SUA_CHAVE_DA_ZAPI"  # Substitua pela sua chave real da API da Z-API

def enviar_mensagem_com_botoes(numero, texto, botoes):
    payload = {
        "number": numero,
        "message": texto,
        "buttons": botoes
    }
    headers = {
        "Content-Type": "application/json",
        "apikey": ZAPI_API_KEY
    }
    response = requests.post(ZAPI_URL, json=payload, headers=headers)
    print("Resposta do envio:", response.status_code, response.text)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Recebido:", data)

    try:
        mensagem = data["message"]["text"]["body"]
        numero = data["message"]["from"]

        if mensagem.lower() == "olá":
            texto = "Olá! Sou o assistente virtual de Rafaela Pereira, sua especialista em planos de saúde. Como posso te ajudar hoje?"
            botoes = [
                {"buttonText": {"displayText": "Quero uma cotação"}},
                {"buttonText": {"displayText": "Tenho dúvidas sobre um plano"}},
                {"buttonText": {"displayText": "Preciso de suporte"}},
                {"buttonText": {"displayText": "Outro assunto"}}
            ]
            enviar_mensagem_com_botoes(numero, texto, botoes)
    except Exception as e:
        print(f"Erro no webhook: {e}")

    return jsonify({"status": "mensagem recebida"})

if __name__ == '__main__':
    app.run(debug=True)
