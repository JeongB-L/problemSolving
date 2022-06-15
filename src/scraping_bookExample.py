#   goal: get the titles of every book with a 2 star rating
import requests
import bs4
if __name__ == '__main__':
    #base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    #base_url.format('20')
    #res = requests.get(base_url.format(1))
    #   soup is basically decoding the res
    #soup = bs4.BeautifulSoup(res.text, 'lxml')
    #products = soup.select(".product_pod")
    #example = products[0]
    #   in can be used as boolean operator
    #a = 'star-rating Three' in str(example)
    #   use the dot to fill out the space
    #print(example.select("a"))
    #   empty list is returned when the string is not returned\
    #print(example.select('a')[1]['title'])
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    two_star_titles = []
    for n in range(1, 51):
        scrape_url = base_url.format(n)
        res = requests.get(scrape_url)

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        books = soup.select(".product_pod")

        for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                book_title = book.select('a')[1]['title']
                two_star_titles.append(book_title)
                print(book_title)