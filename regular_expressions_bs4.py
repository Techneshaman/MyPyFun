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

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = urllib3.connection_from_url(url)
html = response.urlopen('GET', url)
soup = bs4.BeautifulSoup(html.data, 'html.parser')
soup_title = soup.title
soup_links = soup.find_all('a')

print(soup_title)
for item in soup_links:
    print(item)

