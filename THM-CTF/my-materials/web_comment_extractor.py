# Download this file 
# pip install requests beautifulsoup4
# usage: $ python3 websites-comment-extractor.py



import requests
from bs4 import BeautifulSoup, Comment

def fetch_and_find_comments(url):
    try:
        # Fetch the HTML content of the given URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html_text = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_text, 'html.parser')

        # Find all comments in the parsed HTML
        comments = soup.findAll(string=lambda text: isinstance(text, Comment))

        # Output the comments
        print('Comments found:')
        for comment in comments:
            print(comment.strip())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the HTML: {e}")

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    fetch_and_find_comments(url)
