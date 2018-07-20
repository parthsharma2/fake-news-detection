from newspaper import Article

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
    news_articles = news.get_news(' '.join(kw))['articles']
    length = 5 if len(news_articles) > 5 else len(news_articles)

    body = []
    headlines = []
    for i in range(length):
        article = Article(news_articles[i]['url'])
        article.download()
        article.parse()
        body.append(article.text)
        headlines.append(article.title)

    body_sim = text_similarity.check(body, source_article_body)
    headline_sim = text_similarity.check(headlines, source_article_headline)

    return (body_sim + headline_sim) / 2 * 100
