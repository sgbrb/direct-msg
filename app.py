from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")

# Histórico de comentários respondidos (para não responder duas vezes)
ARQUIVO_HISTORICO = "comentarios_respondidos.json"

def carregar_historico():
    try:
        with open(ARQUIVO_HISTORICO, "r") as f:
            return set(json.load(f))
    except:
        return set()

def salvar_historico(historico):
    with open(ARQUIVO_HISTORICO, "w") as f:
        json.dump(list(historico), f)

# --- Rota de verificação do Webhook ---
@app.route('/webhook', methods=['GET'])
def verify():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        return challenge, 200
    return 'Invalid token', 403

# --- Rota que recebe as notificações ---
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if not data:
        return 'Invalid payload', 400
    if data.get("object") == "instagram":
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                if change.get("field") == "comments":
                    comentario = change.get("value", {})
                    comment_id = comentario.get("id")
                    texto = comentario.get("text", "")
                    
                    print(f"💬 Comentário recebido: '{texto}' (ID: {comment_id})")
                    
                    # Aqui você pode adicionar a lógica de palavra-chave
                    # Por enquanto, responde qualquer comentário
                    
                    if comment_id:
                        enviar_dm(comment_id, texto)
    
    return 'EVENT_RECEIVED', 200

def enviar_dm(comment_id, texto_comentario):
    """Envia uma mensagem privada (DM) para quem comentou."""
    url = f"https://graph.facebook.com/v21.0/{comment_id}/private_replies"
    
    mensagem = (
    f"Olá! Obrigado pelo interesse! 😊\n\n"
    f"Recebi seu comentário: '{texto_comentario}'\n\n"
    f"Em breve entraremos em contato com mais informações."
)
    
    params = {
        "message": mensagem,
        "access_token": PAGE_ACCESS_TOKEN
    }
    
    try:
        resp = requests.post(url, params=params, timeout=30)
        print(f"📤 Resposta da API: {resp.status_code} - {resp.text}")
        if resp.status_code == 200:
            print(f"✅ DM enviada com sucesso!")
        else:
            print(f"❌ Erro ao enviar DM: {resp.text}")
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
