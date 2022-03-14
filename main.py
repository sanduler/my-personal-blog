# Name: Ruben Sanduleac
# Date: 03-13-2022
# Description: This python script uses the Flask framework for the personal blog of
import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post_objects = []
url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url_blog)
all_posts = response.json()
# print(all_posts)

for post in all_posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
