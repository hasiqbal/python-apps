import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-05&sortBy=publishedAt&apiKey=99e685768c5945748caa5bc63ab676fd"

request = requests.get(url)
content = request.json()
articles = content["articles"]
for article in articles:
    print(article["title"])