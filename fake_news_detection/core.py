from newspaper import Article
from newsapi.newsapi_exception import NewsAPIException

import keywords
import news
import text_similarity


def calculate(url):
    """
    Calculates text similarity.

    Parameters
    ----------
    url: string
        The url to check for similarity

    Returns
    ----------
    float
        Percentage of similarity

    """
    article = Article(url)
    article.download()
    article.parse()

    source_article_body = article.text
    source_article_headline = article.title

    kw = keywords.extract(source_article_body, limit=5)
    try:
        news_articles = news.get_news(' '.join(kw))['articles']
    except NewsAPIException as e:
        return 0.0
    length = 5 if len(news_articles) > 5 else len(news_articles)

    body = []
    headlines = []
    for i in range(length):
        article = Article(news_articles[i]['url'])
        article.download()
        article.parse()
        body.append(article.text)
        headlines.append(article.title)

    body_sim = text_similarity.cosine_similarity(body, source_article_body)
    headline_sim = text_similarity.cosine_similarity(headlines, source_article_headline)

    return (body_sim + headline_sim) / 2 * 100
