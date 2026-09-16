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
