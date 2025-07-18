import requests
api = "f7612506d4614c3da0af80ad8ac837fd"
query = input("what type of news you intrested today?\n")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-25&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for article in articles:
     print(article["title"])
     print(article["url"])
     print("\n******************************************************************************************************\n")