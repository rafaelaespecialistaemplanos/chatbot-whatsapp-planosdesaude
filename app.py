from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Chatbot de planos de saúde está rodando!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Mensagem recebida:", data)
    return jsonify(status="mensagem recebida"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)