import requests

api_key = "9766c399c522419b9bc95edcc281db1f"
url = ("https://newsapi.org/v2/everything?"
       "q=tesla&from=2026-07-31&sortBy=publishedAt"
       "&apiKey=9766c399c522419b9bc95edcc281db1f")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])