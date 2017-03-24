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

url = 'http://www.gazeta.pl/0,0.html'
response = urllib3.connection_from_url(url)
html = response.urlopen('GET', url)
soup = bs4.BeautifulSoup(html.data, 'html.parser')
soup_title = soup.title
soup_text = soup.find_all('p')

for paragraph in soup_text:
    print(type(paragraph))
    if paragraph.a is not None:
        print(paragraph.a['href'])
        link = paragraph.a['href']
        regexp_html = ".*?\.html"
        if re.match(regexp_html, link) is not None:
            start_position_for_fit = re.match(regexp_html, link).span()[0]
            end_position_for_fit = re.match(regexp_html, link).span()[1]
            print(link[start_position_for_fit: end_position_for_fit])
            website = link.split('/')[2]
            print(website)
    print("TEXT:", paragraph.text)

print(soup_title)
