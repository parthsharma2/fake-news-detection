from summa import keywords


def extract(text, limit=-1):
    """
    Extract keywords from text.

    Parameters
    ----------
    text: string
        A string from which keywords are to be extracted
    limit: int
        An optional argument to specify number of keywords to be extracted

    Returns
    -------
    list
        A list of keywords

    """
    if limit is -1:
        return keywords.keywords(text).split('\n')
    else:
        return keywords.keywords(text).split('\n')[:limit]
