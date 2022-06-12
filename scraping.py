import bs4
import requests

if __name__ == '__main__':
    result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
    #print(result.text)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    site_title = soup.select('title')[0].getText()
    print(site_title)
    site_p = soup.select('p')
    #print(site_p[0].getText())
    toctext = soup.select('.toctext')
    print(f'{toctext} \n')
    for item in soup.select('.toctext'):
        print(item.text)