from bs4 import BeautifulSoup
import requests
import json
import time

quotes_data = []

def quotes_scrap():

    for page in range(1, 11):

        url = 'https://quotes.toscrape.com/page/'
        html_data = requests.get(url + str(page))

        # print(html_data) # Check the response from site

        html_scrap = html_data.text # turns 'response' into raw 'html'

        soup = BeautifulSoup(html_scrap, 'html.parser')

        quotes = soup.find_all('div', class_='quote')

        for index, quote in enumerate(quotes):

            para = quote.find('span', class_="text").text
            author = quote.find('small', class_='author').text
            if quote.find('div', class_='tags'):
                tags_a = quote.find_all('a', class_='tag')
                tags = [tag.text for tag in tags_a]

            dict = {
                'SR. NO.' : index,
                'Quote' : para,
                'Author' : author,
                'Tags' : tags
            }

            quotes_data.append(dict)

            time.sleep(60) # pause traffic for 60sec to look like it's not a bot


    with open('./Quotes/Quotes.json', 'w', encoding='utf-8') as file:
        json.dump(quotes_data, file, indent=4, ensure_ascii=False)

    print("Quotes.json Saved.")

if __name__ == '__main__':
    quotes_scrap()





