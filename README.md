# chatbot-whatsapp-planosdesaude

Chatbot para atendimento automatizado via WhatsApp, voltado para clientes de planos de saúde, utilizando Z-API.

## 🚀 Como usar

1. **Clone este repositório** ou envie os arquivos para seu GitHub.
2. Crie uma conta no [Render](https://render.com) e conecte seu repositório.
3. Configure o deploy como **Web Service** com:
   - Runtime: Python 3
   - Start command: `python main.py`
4. No painel da Z-API, insira o link do webhook:
   `https://seu-projeto-no-render.onrender.com/webhook`
5. Pronto! O bot responderá automaticamente via WhatsApp.

## 🧩 Estrutura do Projeto

- `main.py` – Código principal do Flask (recebe e responde mensagens)
- `.env.example` – Exemplo de configuração com token da Z-API
- `README.md` – Instruções de uso

## 🛠 Requisitos

- Conta no [Render](https://render.com)
- Conta na [Z-API](https://www.z-api.io/)
- Python 3.10+

