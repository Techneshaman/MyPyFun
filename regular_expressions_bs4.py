import wikipedia
import urllib3
import bs4
import re

# text1 = wikipedia.summary('krakow')
# regexp1 = " \(.*?\)"
# regexp2 = " (\(.*?\))"
# print("Before: \n")
# print(re.split(regexp2, text1))
# print("\nAfter:\n")
# print(re.sub(regexp2, "", text1))

url = 'http://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
response = urllib3.connection_from_url(url)
html = response.urlopen('GET', url)
soup = bs4.BeautifulSoup(html.data, 'html.parser')
soup_title = soup.title
soup_tables = soup.find_all('table')


class HTMLTableParser():
    def __init__(self, input_table):
        self.input_table = input_table

    def get_table(self):
        print("NEW TABLE")
        table_soup = bs4.BeautifulSoup(str(self.input_table), 'html.parser')
        rows_list_iter = table_soup.find_all('tr')
        print('Rows in table:', len(list(rows_list_iter)))
        for item in rows_list_iter:
            print("NEXT LINE")
            for child in item.children:
                if child !='\n':
                    print("NEXT CELL:", child.text)
        print("\n\n\n")

print(soup_title)
for item in soup_tables:
    parser = HTMLTableParser(item)
    parser.get_table()