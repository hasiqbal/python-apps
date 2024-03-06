import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-05&sortBy=publishedAt&apiKey=99e685768c5945748caa5bc63ab676fd"

def get_url():

    request = requests.get(url)
    content = request.json()
    articles = content["articles"]
    body = [article["url"] for article in articles]
    return body
    
urls = get_url()
email = '\n'.join(urls)  

send_email(email) 

