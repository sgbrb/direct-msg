from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# --- CONFIGURAÇÕES ---
# Certifique-se de que estas variáveis estão definidas no Railway (Passo 4)
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN") 
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")
PAGE_ID = os.environ.get("PAGE_ID") # O ID da sua página do Facebook vinculada

# Mapeamento de Mensagens (igual ao que fizemos antes)
MENSAGENS_POR_POST = {
    # "17912345678901234": {
    #     "palavra_chave": "EU QUERO",
    #     "mensagem": "Olá! Aqui estão as informações do Apartamento Vista Mar..."
    # },
}
RESPOSTA_PADRAO = "Olá! Obrigado pelo interesse. Me chama no WhatsApp para mais detalhes: (48) 99101-4563"

# 1. Endpoint de Verificação (A Meta acessa isso uma vez para validar)
@app.route('/webhook', methods=['GET'])
def verify():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode == 'subscribe' and token == VERIFY_TOKEN:
        return challenge, 200
    return 'Invalid token', 403

# 2. Endpoint de Notificação (A Meta acessa isso sempre que alguém comenta)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # ... (Lógica para extrair comment_id, media_id, texto) ...

    return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)))