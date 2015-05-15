from flask import Flask,render_template,request,redirect,url_for
from flask.ext.pymongo import PyMongo
from bson import ObjectId
from domain import post
import json

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
    posts = mongo.db.posts.find()
    return render_template('index.html',posts=posts)

@app.route('/posts/', methods=['POST','GET'])
def add_post():
    if request.method == 'GET':
        return show_the_post_form()
    else:
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        author = request.form['author']
        all_tags = tags.split(' ')
        blog_post = post.Post(title,content,all_tags,author)
        mongo.db.posts.insert(json.loads(blog_post.get_json_string()))
        return redirect('/')


@app.route('/whoami/')
def about_me():
    return '$whoami'

@app.route('/posts/<post_id>')
def posts(post_id):
    post = mongo.db.posts.find_one_or_404({'_id':ObjectId(post_id)})
    posts = []
    posts.append(post)
    return render_template('index.html', posts = posts)

def show_the_post_form():
    return render_template('post.html')

if __name__ == '__main__':

    app.run(debug=True)



