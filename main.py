from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Chatbot WhatsApp - Rafaela Pereira'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Aqui você pode colocar a lógica de resposta com base nos botões
    print("Mensagem recebida:", data)
    return jsonify({"status": "mensagem recebida"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
