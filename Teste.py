import feedparser
import urllib3
import requests

# Desativa os avisos vermelhos de SSL no terminal por usar verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://canaltech.com.br/rss/'  # Tente usar também /rss/ ou https://www.canaltech.com.br/feed/

# Simulando um navegador completo com cabeçalhos reais
session = requests.Session()
session.headers.update({
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    ),
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    ),
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
})

try:
  resposta = session.get(url, verify=False, allow_redirects=True, timeout=10)
  print(f'Status Code: {resposta.status_code}')

  if resposta.status_code == 200:
    feed = feedparser.parse(resposta.text)
    print(f'Sucesso! Carregou {len(feed.entries)} notícias do Canaltech.')
  else:
    print(
        f'O servidor respondeu com {resposta.status_code}. Pode ser bloqueio'
        ' do IP corporativo.'
    )

except Exception as e:
  print(f'Erro na conexão: {e}')