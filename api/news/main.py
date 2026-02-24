import requests
import sendEmail

topic = "gym"

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={topic}&"
    f"from=2026-01-23&"
    f"sortBy=publishedAt&"
    f"language=en&"
    f"apiKey=52459937f26d4595aebf8d1282e8f73c"
)

response = requests.get(url)
content = response.json()

# Build HTML email body
myArticle = f"""
<h2>📰 Latest {topic.capitalize()} News</h2>
<p>Here is some political news my script fetched for you.\n I didn't make the UI so i cant deploy it but i gave it topic and and your email, idk what it'll send you</p>
<hr>
"""

for article in content["articles"][:5]:
    myArticle += f"""
    <h3>{article['title']}</h3>
    <p>{article.get('description', 'No description available.')}</p>
    <a href="{article['url']}">Read full article</a>
    <hr>
    """

sendEmail.send_email(myArticle)