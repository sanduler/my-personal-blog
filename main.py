# Name: Ruben Sanduleac
# Date: 03-13-2022
# Description: This python script uses the Flask framework for the personal blog of
import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

# create a new list of post as objects from post class
post_objects = []
# get the endpoint url
url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
# get the response from the url
response = requests.get(url_blog)
# get all the posts as a json dictionary
all_posts = response.json()
# use a for loop to loop through all the posts and send them to the Post class while creating them as objects
# for each post ==> each post == object
for post in all_posts:
    # create an object for each post
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    # append the post object to the list
    post_objects.append(post_obj)


# get the home page
@app.route('/')
def home():
    # return the all the post objects back to the html page
    return render_template("index.html", all_posts=post_objects)


# rederect to page based on the post id --> post/{id}
@app.route("/post/<int:index>")
def show_post(index):
    # set the requested_post to none
    requested_post = None
    # loop through the list of post objects
    for blog_post in post_objects:
        # when the id matches the selected index by the user the requested_post is set to the correct blog post
        if blog_post.id == index:
            requested_post = blog_post
    # requested blog post is sent back to the post html
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
