import feedparser
import ssl
import time
from datetime import datetime

noticias_hoje = []
feeds = []

if hasattr(ssl, "_create_unverified_context"):
  ssl._create_default_https_context = ssl._create_unverified_context
feed_tecnoblog= feedparser.parse('https://tecnoblog.net/feed/')
feed_canaltech = feedparser.parse('https://canaltech.com.br/feed/')
feeds.append(feed_tecnoblog)
feeds.append(feed_canaltech)

for feed in feeds:
  for noticia in feed.entries:
    data_noticia = datetime(*noticia.published_parsed[:6]).date()
  if data_noticia == datetime.now().date():
    noticias_hoje.append(noticia)

for noticia in noticias_hoje:
    data_pub = datetime(*noticia.published_parsed[:6]).date()
    print(f"Título: {noticia.title}")
    print(f"Link: {noticia.link}")
    print(f"Data de Publicação: {data_pub}")
    print(f"Resumo: {noticia.summary}\n")



time.sleep(3600)