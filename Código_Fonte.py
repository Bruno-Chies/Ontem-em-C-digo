import ssl
import time
from datetime import datetime
import Funcoes

while True:
  feeds = []
  noticias_hoje = []
  try:
    if hasattr(ssl, "_create_unverified_context"):
      ssl._create_default_https_context = ssl._create_unverified_context
    Funcoes.acrescentarblog('https://tecnoblog.net/feed/', feeds)
    Funcoes.acrescentarblog('https://canaltech.com.br/rss/', feeds)
    Funcoes.acrescentarblog('https://www.infoq.com/br/development/', feeds)

    for feed in feeds:
      for noticia in feed.entries:
        data_noticia = Funcoes.obter_data_noticia(noticia)
        if data_noticia == datetime.now().date():
          noticias_hoje.append(noticia)

    for noticia in noticias_hoje:
        data_pub = Funcoes.obter_data_noticia(noticia)
        print(f"Título: {noticia.title}")
        print(f"Link: {noticia.link}")
        print(f"Data de Publicação: {data_pub}")
        print(f"Resumo: {noticia.summary}\n")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")


  time.sleep(3600)