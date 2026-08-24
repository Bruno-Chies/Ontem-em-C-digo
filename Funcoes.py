def obter_data_noticia(noticia):
    from datetime import datetime, timezone, timedelta
    # Tenta pegar a data de publicação padrão
    tempo_parsed = None
    if hasattr(noticia, "published_parsed") and noticia.published_parsed:
        tempo_parsed = noticia.published_parsed
    elif hasattr(noticia, "updated_parsed") and noticia.updated_parsed:
        tempo_parsed = noticia.updated_parsed
        
    if tempo_parsed:
        # 1. Cria o datetime em UTC usando timezone.utc (nativo e seguro)
        dt_utc = datetime(*tempo_parsed[:6], tzinfo=timezone.utc)
        
        # 2. Como o horário oficial do Brasil (Brasília) é UTC-3, 
        # aplicamos o deslocamento fixo diretamente:
        fuso_brasil = timezone(timedelta(hours=-3))
        dt_brasil = dt_utc.astimezone(fuso_brasil)
        
        return dt_brasil.date()
    return None
def acrescentarblog(url_blog, list_feeds):
    import feedparser
    import urllib3
    import requests

    # Desativa os avisos vermelhos de SSL no terminal por usar verify=False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
        resposta = session.get(url_blog, verify=False, allow_redirects=True, timeout=10)
        print(f'Status Code: {resposta.status_code}')

        if resposta.status_code == 200:
            feed = feedparser.parse(resposta.text)
            print(f'Sucesso! Carregou {len(feed.entries)} notícias do {url_blog}.')
            list_feeds.append(feed)
        else:
            print(
                f'O servidor respondeu com {resposta.status_code}. Pode ser bloqueio'
                ' do IP corporativo.'
        )

    except Exception as e:
        print(f'Erro na conexão: {e}')