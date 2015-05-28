from flask import Flask,render_template,request,redirect,session,url_for,flash
from flask.ext.pymongo import PyMongo
from bson import ObjectId
from domain import post
from passlib.apps import custom_app_context as pwd_context
import json
import re

app = Flask(__name__)
app.secret_key = "thisisverysecret"
mongo = PyMongo(app)

'''Index Page
Returns all the posts available
Might add more restrictions as we go forward
'''
@app.route('/')
def index():
    posts = mongo.db.posts.find()
    return render_template('index.html',posts=posts)

@app.route('/search', methods = ['GET'])
def search():
    search_str = request.args.get('search')
    search_regex = re.compile(search_str, re.IGNORECASE)
    posts = mongo.db.posts.find({'title' : { '$regex': search_regex}})
    return render_template('search.html',posts=posts)

'''Create a post
No Validations has been added so far. 
That will be the next step
'''
@app.route('/posts/', methods=['POST','GET'])
def add_post():
    if request.method == 'GET':
        if session.get('logged_in'):
            return show_the_post_form()
        else:
            return redirect(url_for('login'))
    else:
        if session.get('logged_in'):
            blog_post = post.Post(request.form['title'],request.form['content'],request.form['tags'].split(' '),request.form['author'])
            mongo.db.posts.insert(json.loads(blog_post.get_json_string()))
            return redirect('/')
        else:
            return redirect(url_for('login'))

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return show_the_login_form()
    else:
        user = mongo.db.users.find_one_or_404({'user_name' : request.form['username']})
        password = request.form['pswd']
        salted_password = password + user['salt']
        if pwd_context.verify(salted_password,user['password']):
            print 'logged IN'
            session['logged_in'] = True
            return redirect('/')
        else:
            return redirect(url_for('login'))

@app.route('/logout/',methods=['GET'])
def logout():
        session['logged_in'] = False
        return redirect('/')

''' Who Am I or Traditionally called as About page
Need to add content
CMS like wp does not entice me
'''
@app.route('/whoami/')
def about_me():
    return '$whoami'

'''View a post
How can I get rid of mongo id's in URL???
Something to think about
'''
@app.route('/posts/<post_id>')
def posts(post_id):
    post = mongo.db.posts.find_one_or_404({'_id':ObjectId(post_id)})
    return render_template('view.html', post = post)

def show_the_login_form():
    return render_template('login.html')

def show_the_post_form():
    return render_template('post.html',session=session)

if __name__ == '__main__':
    app.run(debug=True)



