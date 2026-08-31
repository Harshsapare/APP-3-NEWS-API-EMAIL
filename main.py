import requests
from send_email import send_email

api_key = "9766c399c522419b9bc95edcc281db1f"
url = ("https://newsapi.org/v2/everything?"
       "q=tesla&from=2026-07-31&sortBy=publishedAt"
       "&apiKey=9766c399c522419b9bc95edcc281db1f")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)