import requests


def sendMsg(msg):
    BOT_TOKEN = '7088981728:AAHGuOSD-JHpcSVFRLnISn4PFFMVCOTKQcg'
    CHANNEL_ID = '-1002644372555'
    MESSAGE = f"""*📩 NEW MESSAGE*

*Name:* {msg['name']}
*Email:* {msg['email']}
*Subject:* {msg['subject']}
*Message:* {msg['message']}"""

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHANNEL_ID,
        'text': MESSAGE,
        'parse_mode': 'Markdown'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return "✅ Xabar muvaffaqiyatli yuborildi!"
    else:
        return "❌ Xabar yuborishda xatolik. Qaytadan urinib ko'ring"
