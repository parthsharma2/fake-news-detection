from newspaper import Article

import keywords
import news
import text_similarity


def calculate(url):
    """Calculate."""
    article = Article(url)
    article.download()
    article.parse()

    source_article = article.text

    kw = keywords.extract(source_article, limit=5)
    news_articles = news.get_news(' '.join(kw))['articles']
    length = 5 if len(news_articles) > 5 else len(news_articles)

    s = []
    for i in range(length):
        article = Article(news_articles[i]['url'])
        article.download()
        article.parse()
        s.append(article.text)

    return text_similarity.check(s, source_article)
