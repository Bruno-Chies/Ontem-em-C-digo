import feedparser
import ssl
import time
from datetime import datetime

noticias_hoje = []

if hasattr(ssl, "_create_unverified_context"):
  ssl._create_default_https_context = ssl._create_unverified_context
feed = feedparser.parse('https://tecnoblog.net/feed/')
for noticia in feed.entries:
  data_noticia = datetime(*noticia.published_parsed[:6]).date()
  if data_noticia == datetime.now().date():
    noticias_hoje.append(noticia)
    for noticia in noticias_hoje:
        print(f"Título: {noticia.title}")
        print(f"Link: {noticia.link}")
        print(f"Data de Publicação: {data_noticia}")
        print(f"Resumo: {noticia.summary}\n")



time.sleep(3600)