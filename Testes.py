
import feedparser
import requests
list_feeds = []
    # Simula um navegador comum para evitar bloqueios de bot
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
resposta = requests.get('https://tecnoblog.net/feed/', headers=headers, verify=False)
if resposta.status_code == 200:
    list_feeds.append(feedparser.parse(resposta.text))
else:
    print(f"Erro ao acessar o feed. Status code: {resposta.status_code}")