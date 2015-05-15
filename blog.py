from flask import Flask,render_template,request,redirect,session,url_for
from flask.ext.pymongo import PyMongo
from bson import ObjectId
from domain import post
import json

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
            redirect(url_for('login'))

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return show_the_login_form()
    else:
        session['logged_in'] = True
        return redirect('/')

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
    posts = []
    posts.append(post)
    return render_template('index.html', posts = posts)

def show_the_login_form():
    return render_template('login.html')

def show_the_post_form():
    return render_template('post.html',session=session)

if __name__ == '__main__':
    app.run(debug=True)



