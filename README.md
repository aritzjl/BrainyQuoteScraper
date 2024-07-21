# BrainyQuote Scraper

This project is a web scraper designed to extract quotes from the [BrainyQuote](https://www.brainyquote.com/) website. The scraper collects quotes from various authors and stores them in a JSON file. Additionally, it includes functionality to send notifications via email during the scraping process.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Details](#detailed-description)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the BrainyQuote Scraper, follow these steps:

1. **Clone the repository:**
    
    ```bash
    git clone https://github.com/yourusername/brainyquote-scraper.git
    cd brainyquote-scraper
    ```
    
2. **Install the required dependencies:**
    
    ```bash
    pip install -r requirements.txt
    ```
    

## Usage

1. **Configure email notifications:**
    
    Set the environment create a file `config.py`with the following format:

    ```python
    EMAIL_SENDER="example@gmail.com"
    EMAIL_PASSWORD="xxxxxxx"
    ```
    
2. **Run the scraper:**
    
    Use the provided `run.sh` script to run the scraper in the background.
    
    ```bash
    chmod +x run.sh
    ./run.sh
    ```
    
3. **Check the output:**
    
    The scraped quotes will be stored in `authors.json`. Check `scraper.log` for logs related to the scraping process.
    

### Detailed Description

- **main.py**: The entry point of the application. It coordinates the scraping process and handles the data storage.
- **authorquotes.py**: Contains functions to scrape quotes from an author's page.
- **author.py**: Defines the `Author` class, which encapsulates an author's name, URL, and their quotes.
- **utils.py**: Contains utility functions for web scraping, sending email notifications, and random sleep to mimic human browsing.
- **run.sh**: Script to run the scraper in the background and log the output.

## Configuration

- **Email Notifications**: Configure email notifications by setting `EMAIL_SENDER` and `EMAIL_PASSWORD` variables at `config.py`.
- **Random Sleep**: The `random_sleep` function in `utils.py` introduces random delays to mimic human behavior and avoid getting blocked by the website.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.
