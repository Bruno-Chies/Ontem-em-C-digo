import feedparser
import requests

# Testando com a do TudoCelular ou Tecnoblog para validar o código
url = 'https://www.tudocelular.com/feed'

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}

resposta = requests.get(url, headers=headers, verify=False)

if resposta.status_code == 200:
  feed = feedparser.parse(resposta.text)
  print(f'Sucesso! Carregou {len(feed.entries)} notícias.')
else:
  print(f'Erro: {resposta.status_code}')