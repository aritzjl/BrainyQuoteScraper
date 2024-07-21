from authorquotes import get_all_author_quotes
from author import Author
import json
import utils
from tqdm import tqdm


BASE_URL = 'https://www.brainyquote.com'


def get_data() -> list[dict]:
    authorsListUrl = BASE_URL + '/authors'
    authorsList = []

    soup = utils.get_soup(authorsListUrl)
    authors = soup.find_all('span', class_='authorContentName')

    for author in tqdm(authors, desc="Extracting authors"):
        authorName = author.text
        authorUrl = BASE_URL + author.parent['href']
        authorQuotes = get_all_author_quotes(authorUrl)
        authorsList.append(Author(authorName, authorUrl, authorQuotes))

        if len(authorsList) % 20 == 0:
            subject = "Scraping authors"
            msg = f"Scraped {len(authorsList)} authors"
            utils.notify(subject, msg)

    authors_data = [{'name': author.name,
                     'url': author.url,
                     'quotes': author.quotes}
                    for author in authorsList]
    return authors_data


def main():
    authors_data = get_data()

    with open('authors.json', 'w') as json_file:
        json.dump(authors_data, json_file, indent=4)

    utils.notify("Finished Scraping Quotes",
                 "Scraping authors finished successfully")


if __name__ == "__main__":
    main()
