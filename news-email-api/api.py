import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-06&sortBy=publishedAt&apiKey=99e685768c5945748caa5bc63ab676fd"

def get_url():
    request = requests.get(url)
    content = request.json()    
    articles = content["articles"]
    # List of tuples containing URL and title
    body = [(article["url"], article["title"]) for article in articles]
    return body

# Get list of URLs and titles
urls_and_titles = get_url()

# Construct email body
email_body = "\n".join([f"{title}: {url}\n" for url, title in urls_and_titles])


# Send email
send_email(email_body)


