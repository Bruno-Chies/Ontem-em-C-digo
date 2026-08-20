import feedparser

# Testa baixar direto, sem envolver a sua função nem listas complexas
url = 'https://tecnoblog.net/feed/'
print(f"Testando baixar direto: {url}")

feed = feedparser.parse(url)

print(f"Objeto retornado: {feed}")
print(f"Quantidade de entries: {len(feed.entries)}")