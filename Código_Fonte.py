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
    if len(feeds) > 1:
      print(f"Canaltech carregou: {len(feeds[1].entries)} notícias")
    else:
      print("Canaltech não retornou dados.")

    Funcoes.acrescentarblog('https://canaltech.com.br/feed/', feeds)
    if len(feeds) > 1:
      print(f"Canaltech carregou: {len(feeds[1].entries)} notícias")
    else:
      print("Canaltech não retornou dados.")

    Funcoes.acrescentarblog('https://www.infoq.com/br/feed/', feeds)
    if len(feeds) > 2:
      print(f"InfoQ carregou: {len(feeds[2].entries)} notícias")
    else:
      print("InfoQ não retornou dados.")

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