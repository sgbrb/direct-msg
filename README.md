# direct-msg

Webhook Flask para automação de respostas no Instagram Direct.

## 🎯 Sobre

Aplicação Python que recebe notificações de comentários no Instagram via
Webhook da Meta, processa o texto e envia automaticamente uma mensagem
privada (DM) para o autor do comentário.

O projeto foi desenvolvido para automatizar o atendimento inicial em
páginas comerciais — quem comenta em um post recebe uma resposta direta
com informações e contato.

### Como funciona

1. A Meta envia um POST para `/webhook` a cada novo comentário no post
2. O servidor extrai o `comment_id` e o texto do comentário
3. Envia uma DM via Graph API (`/private_replies`)
4. Loga o status no console

## 🛠️ Stack

- **Python 3**
- **Flask** — servidor HTTP e roteamento do webhook
- **requests** — cliente HTTP para a Graph API da Meta
- **gunicorn** — servidor WSGI para produção
- **Meta Graph API v21.0** — envio das DMs

## 🏗️ Estrutura
direct-msg/
├── app.py # Servidor Flask + lógica do webhook
├── Procfile # Comando de deploy (gunicorn)
└── requirements.txt # Dependências
## ▶️ Como rodar localmente

```bash
git clone https://github.com/sgbrb/direct-msg.git
cd direct-msg
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py

⚙️ Variáveis de ambiente
Variável	Descrição
VERIFY_TOKEN	Token usado na verificação inicial do webhook
PAGE_ACCESS_TOKEN	Token de acesso da página do Instagram
PAGE_ID	ID da página
🌐 Configurando o Webhook na Meta
Crie um app em developers.facebook.com

Adicione o produto Webhooks

Configure a URL: https://seu-dominio/webhook

Use o mesmo valor em Verify Token que está no .env

Assine o evento comments do objeto instagram

🚀 Deploy
O projeto inclui um Procfile com web: gunicorn app:app, pronto para
deploy em Heroku, Railway, Render ou qualquer plataforma que suporte
buildpacks Python.

📚 O que aprendi
Ciclo de vida de webhooks da Meta (GET de verificação + POST de eventos)

Autenticação com Page Access Token na Graph API

Uso do endpoint /private_replies para envio de DMs vinculadas a comentários

Configuração de deploy com gunicorn + Procfile

📄 Licença

MIT
