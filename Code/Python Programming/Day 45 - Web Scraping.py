from bs4 import BeautifulSoup
# import lxml
import requests


with open('website_45.html', encoding='utf8') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())
print(soup.a)

anchor_tags = soup.find_all(name='a')
print(anchor_tags)

for tag in anchor_tags:
    print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1', id='name')
print(heading.getText())
print(heading.get('id'))

heading = soup.find(name='h3', class_='heading')
print(heading)
print(heading.getText())
print(heading.get('class'))

name = soup.select_one('#name')
headings = soup.select('.heading')
print(name)
print(headings)


response = requests.get(url='https://news.ycombinator.com/news')
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')
article_texts = []
article_links = []
for article in articles:
    article_text = article.find(name='a')
    article_links.append(article_text.get('href'))
    article_texts.append(article_text.getText())

article_upvote = soup.find_all(name='span', class_='score')
article_upvotes = [int(upvotes.getText().split()[0]) for upvotes in article_upvote]

print(article_texts)
print(article_links)
print(article_upvotes)

largest = max(article_upvotes)
print(largest)
index = article_upvotes.index(largest)
print(index)
print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])



### Project ###
response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/', )
web_text = response.text

soup = BeautifulSoup(web_text, 'html.parser')
movies_list = [movie.getText() for movie in soup.find_all(name='h3', class_='title')][::-1]

with open('top_100_movies.txt', 'w', encoding='utf8') as f:
    for movie in movies_list:
        f.write(f'{movie}\n')