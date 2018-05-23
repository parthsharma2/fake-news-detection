from configparser import ConfigParser
from newsapi import NewsApiClient

config = ConfigParser()
config.read('../config.ini')

NEWS_API = config.get('news_api', 'api')

news_client = NewsApiClient(api_key=NEWS_API)


def get_news(keywords, news='all'):
    """
    Retrieve news articles containing keywords.

    Parameters
    ----------
    keywords: string
        A string containing all keywords that are to be contained in the news
    news: string
        Optional argument to define whether to fetch 'all' news articles or
        only 'top' headlines.
        Takes value 'top' or 'all'

    Returns
    -------
    dict
        A dict of news articles

    """
    if news is 'all':
        return news_client.get_everything(q=keywords)
    elif news is 'top':
        return news_client.get_top_headlines(q=keywords)
    else:
        raise AttributeError("Optional argument news expected 'top' or 'all'")
