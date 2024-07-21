#  get-author-quotes.py

"""This module is used to extract quotes from a
specific author from the brainyquote website.
"""

import utils
#  from tqdm import tqdm


def get_total_pages(authorUrl) -> int:
    soup = utils.get_soup(authorUrl)
    pages = soup.find_all('a', class_='page-link')
    totalPages = 0
    for page in pages:
        if page.text.isdigit():
            totalPages = int(page.text)
    return totalPages


def get_quotes(pageUrl) -> list:
    """Obtain all quotes from a page.

    Args:
        url (str): Url of the page to extract quotes from.

    Returns:
        list: List of all quotes found in the page.
    """
    quotesFound = []

    soup = utils.get_soup(pageUrl)
    quotes = soup.find_all('a', class_='b-qt')

    #  for quote in tqdm(quotes, desc="Extracting quotes"):
    for quote in quotes:
        quotesFound.append(quote.text.strip())

    return quotesFound


def get_author_quotes(authorUrl) -> list:
    """Obtain all quotes from an author.

    Args:
        authorUrl (str): Url of the author to extract quotes from.

    Returns:
        list: List of all quotes found from the author.
    """

    totalPages = get_total_pages(authorUrl)

    # Get quotes from each page
    quotes = []
    for page in range(1, totalPages + 1):
        url = authorUrl + f'_{page}'
        url = url.replace('_1', '')
        quotes.extend(get_quotes(url))
        utils.random_sleep()

    return quotes


def get_all_author_quotes(authorUrl: str) -> list:
    return get_author_quotes(authorUrl)
