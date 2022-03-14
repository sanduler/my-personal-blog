# Name: Ruben Sanduleac
# Date: 03-13-2022
# Description: This python script uses the Flask framework for the personal blog of
import requests
from flask import Flask, render_template

app = Flask(__name__)

url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url_blog)
all_posts = response.json()
print(all_posts)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
