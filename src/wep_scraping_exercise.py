import requests
import bs4
if __name__ == '__main__':
    #   TASK: Use requests library and BeautifulSoup to connect
    #   to http://quotes.toscrape.com/ and get the HMTL text from the homepage.

    base_url = 'http://quotes.toscrape.com/'
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #print(soup)

    #   TASK: Get the names of all the authors on the first page.
    list_of_authors = []
    authors = soup.select('.author')
    for author in authors:
        list_of_authors.append(author.text)
        #print(author.text)

    #   TASK: Create a list of al quotes on the first page
    list_of_quotes = []
    quotes = soup.select('.text')
    counter = 0
    for quote in quotes:
        list_of_quotes.append(quote.text)
        #print(quote.text)

    #   TASK: Inspect the site and use Beautiful Soup to extract the top ten tags
    #   from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
    #   HINT: Keep in mind there are also tags underneath each quote,
    #   try to find a class only present in the top right tags, perhaps check the span.
    list_of_tags = []
    tags = soup.select(".tag-item")
    for tag in tags:
        list_of_tags.append(tag.text.replace('\n', ''))

    #   TASK: Notice how there is more than one page,
    #   and subsequent pages look like this http://quotes.toscrape.com/page/2/.
    #   Use what you know about for loops and string concatenation
    #   to loop through all the pages and get all the unique authors on the website.
    #   Keep in mind there are many ways to achieve this,
    #   also note that you will need to somehow figure out how to check that your loop is on the last page with quotes.
    #   For debugging purposes, I will let you know that there are only 10 pages,
    #   so the last page is http://quotes.toscrape.com/page/10/,
    #   but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand,
    #   perhaps use try/except for this, its up to you!
    unique_authors = set()
    base_url = 'http://quotes.toscrape.com/page/{}/'
    for page_number in range(1, 11):
        new_base_url = base_url.format(page_number)
        res = requests.get(new_base_url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        authors = soup.select('.author')
        for author in authors:
            unique_authors.add(author.text)
    print(unique_authors)


