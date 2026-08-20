
def obter_data_noticia(noticia):
    from datetime import datetime
    # Tenta pegar a data de publicação padrão
    if hasattr(noticia, "published_parsed") and noticia.published_parsed:
        return datetime(*noticia.published_parsed[:6]).date()
    
    # Se não existir, tenta a data de atualização
    if hasattr(noticia, "updated_parsed") and noticia.updated_parsed:
        return datetime(*noticia.updated_parsed[:6]).date()
        
    return None
def acrescentarblog(url_blog, list_feeds):
    import feedparser
    list_feeds.append(feedparser.parse(url_blog))