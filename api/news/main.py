import requests
import sendEmail
topic="ps5"
url=f"https://newsapi.org/v2/everything?q={topic}&from=2026-01-23&sortBy=publishedAt&apiKey=52459937f26d4595aebf8d1282e8f73c&language=en"

#got the whole data in string
request=requests.get(url)

#got the dict with data
content=request.json()
myArticle = ""

for article in content["articles"][:5]:
    myArticle += article["title"] + "\n"+article["description"]+"\n"+article["url"]+"\n\n"

# for article in content["articles"][:5]:
#     myArticle += f"""
#     <b>{article['title']}</b><br>
#     {article['description']}<br>
#     <a href="{article['url']}">{article['url']}</a><br><br>
#     """

myArticle=myArticle.encode("utf-8")


print(myArticle)

sendEmail.send_email(myArticle)