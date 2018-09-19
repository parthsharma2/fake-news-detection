from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import Similarity

from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cosine

import string


def tokenize(text):
    """
    Tokenizes a string.

    Parameters
    ----------
    text: string
        A string to be tokenized

    Returns
    ----------
    list
        A list of tokens

    """
    return [w.lower() for w in word_tokenize(text)]


def check(docs, target):
    """
    Calculate the similarity between target and docs.

    Parameters
    ----------
    docs: list
        A list of strings to be compared against
    target: string
        The target string to be compared

    Returns
    -------
    float
        The percentage similarity

    """
    stemmer = PorterStemmer()

    tok_docs = [tokenize(text) for text in docs]
    stem_docs = [[stemmer.stem(word) for word in doc] for doc in tok_docs]

    dictionary = Dictionary(stem_docs)
    corpus = [dictionary.doc2bow(doc) for doc in stem_docs]
    tfidf = TfidfModel(corpus)
    sims = Similarity('/tmp/sims.index', tfidf[corpus],
                      num_features=len(dictionary))

    query = [stemmer.stem(word) for word in tokenize(target)]
    query_bow = dictionary.doc2bow(query)
    query_tfidf = tfidf[query_bow]

    return sum(sims[query_tfidf]) / len(sims[query_tfidf])


def cosine_similarity(docs, target):
    docs += [target]

    stemmer = PorterStemmer()
    stop_words = stopwords.words('english')

    translator = str.maketrans('', '', string.punctuation + "‘")

    tok_docs = [[stemmer.stem(i.lower()) for i in tokenize(d.translate(translator)) if i.lower() not in stop_words] for d in docs]
    mod_docs = [''.join(d) for d in tok_docs]

    tf_idf = TfidfVectorizer().fit_transform(mod_docs)

    result = [cosine(tf_idf[i].todense(), tf_idf[len(mod_docs) - 2].todense()) for i in range(len(mod_docs) - 1)]

    return sum(result) / len(result) if len(result) != 0 else 0
