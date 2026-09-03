from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

# CREATE APP
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")  # WTForms  REQUIRED A SECRET KEY TO USE CSRF
# CKEDITOR OBJECT
ckeditor = CKEditor(app)

# ATTACHING BOOTSTRAP 5 TO THE APP
Bootstrap5(app)


# Create Database
class Base(DeclarativeBase):
    pass


# SQLAlchemy object
db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///post.db"

# initialize the app with the extension
db.init_app(app)


# CREATING FORM FOR THE BLOG
class MyForm(FlaskForm):
    blog_post_title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    your_name = StringField("Your Name", validators=[DataRequired()])
    blog_image_url = StringField("Blog Name Url", validators=[DataRequired()])
    blog_content = CKEditorField("Blog Contend", validators=[DataRequired()])
    submit = SubmitField("Publish")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# DATABASE CREATED
with app.app_context():
    db.create_all()


# QUERY ALL POSTS FORM THE DATABASE
@app.route("/")
def get_all_posts():

    posts = []

    # GETTING ALL POSTS FROM THE DB
    all_posts = db.session.execute(db.select(BlogPost)).scalars().all()

    for post in all_posts:
        posts.append(post)

    return render_template(template_name_or_list="index.html", all_posts=posts)


@app.route("/show_post/<post_id>")
def show_post(post_id):

    requested_post = db.get_or_404(BlogPost, post_id)


    return render_template(template_name_or_list="post.html", post=requested_post)


# ADD NEW POST ROUTE
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    is_edit = False
    # FLASK-FORM OBJECT
    form = MyForm()

    if form.validate_on_submit():
        # GETTING THE DATE (MONT,DAY OF THE MONTH, YEAR)
        date = datetime.now()
        formated_date = date.strftime("%B %d, %Y")
        # SAVING THE NEW POST TO THE DATABASE
        new_post_to_save = BlogPost(title=form.blog_post_title.data, subtitle=form.subtitle.data,
                                    date=formated_date, body=form.blog_content.data, author=form.your_name.data,
                                    img_url=form.blog_image_url.data)
        db.session.add(new_post_to_save)
        db.session.commit()


        return redirect(url_for("get_all_posts"))

    return render_template(template_name_or_list="make-post.html", form=form, is_edit=is_edit)


# EDIT POST ROUTE
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):


    is_edit = True
    post_to_edit = db.get_or_404(BlogPost, post_id)
    edit_post_form = MyForm(blog_post_title=post_to_edit.title, subtitle=post_to_edit.subtitle,
                            your_name=post_to_edit.author, blog_image_url=post_to_edit.img_url,
                            blog_content=post_to_edit.body)

    # SAVING THE EDITED POST TO THE DATABASE
    if edit_post_form.validate_on_submit():

        post_to_edit.title = edit_post_form.blog_post_title.data
        post_to_edit.subtitle = edit_post_form.subtitle.data
        post_to_edit.img_url = edit_post_form.blog_image_url.data
        post_to_edit.author = edit_post_form.your_name.data
        post_to_edit.body = edit_post_form.blog_content.data

        db.session.commit()
        return redirect(url_for("show_post", post_id=post_to_edit.id))

    return render_template(template_name_or_list="make-post.html", is_edit=is_edit, form=edit_post_form)


@app.route("/delete/<post_id>")
def delete(post_id):

    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect(url_for('get_all_posts'))


# ABOUT ROUTE
@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")


# CONTACT ROUTE
@app.route("/contact")
def contact():
    return render_template(template_name_or_list="contact.html")


# REST API

# GET ALL BLOG POSTS
@app.route("/api/posts", methods=["GET"])
def api_get_posts():
    all_posts = db.session.execute(db.select(BlogPost)).scalars().all()

    all_posts_list = []

    for post in all_posts:
        post_dict = {

            "id": post.id,
            "title": post.title,
            "subtitle": post.subtitle,
            "date": post.date,
            "body": post.body,
            "author": post.author,
            "img_url": post.img_url

        }
        all_posts_list.append(post_dict)
    return jsonify(all_posts_list)


# GET A SINGLE POST
@app.route("/api/posts/<post_id>", methods=["GET"])
def api_get_post(post_id):

    post = db.get_or_404(BlogPost, post_id)

    post_dict = {

        "id": post.id,
        "title": post.title,
        "subtitle": post.subtitle,
        "date": post.date,
        "body": post.body,
        "author": post.author,
        "img_url": post.img_url

    }

    return jsonify(post_dict)


# ADD POST
@app.route("/api/posts/add-post", methods=["POST"])
def api_add_post():

    title = request.args.get('title')
    subtitle = request.args.get('subtitle')
    body = request.args.get('body')
    author = request.args.get('author')
    img_url = request.args.get('img_url')

    # GETTING THE DATE (MONT,DAY OF THE MONTH, YEAR)
    date = datetime.now()
    formated_date = date.strftime("%B %d, %Y")

    # ADDING NEW POST TO THE DATABASE
    new_post_to_add = BlogPost(title=title, subtitle=subtitle, body=body, author=author, img_url=img_url,
                               date=formated_date)
    db.session.add(new_post_to_add)
    db.session.commit()

    post_dict = {

        "title": title,
        "subtitle": subtitle,
        "date": formated_date,
        "body": body,
        "author": author,
        "img_url": img_url

    }

    return jsonify(response={"Successfully Added": post_dict})


# UPDATE/EDIT POST
@app.route("/api/posts/<post_id>", methods=['PATCH'])
def api_update_post(post_id):

    post = db.get_or_404(BlogPost, post_id)

    if request.args.get('title'):
        post.title = request.args.get('title')

    if request.args.get('subtitle'):
        post.subtitle = request.args.get('subtitle')
    if request.args.get('author'):
        post.author = request.args.get('author')
    if request.args.get('body'):
        post.body = request.args.get('body')
    if request.args.get('img_url'):
        post.img_url = request.args.get('img_url')
    db.session.commit()

    post_dict = {

        "title": post.title,
        "subtitle": post.subtitle,
        "body": post.body,
        "author": post.author,
        "img_url": post.img_url

    }

    return jsonify(Response={"Success Post Updated": post_dict})


# DELETE A POST
@app.route("/api/posts/delete-post/<post_id>", methods=["DELETE"])
def api_delete_post(post_id):

    api_key = request.args.get('api_key')  # HELPS TO ADD A LAYER OF SECURITY

    delete_post = db.session.get(entity=BlogPost, ident=post_id)  # IF THE post_id IS NOT IN THE DB RETURN A NONE

    if api_key == os.environ.get("API_KEY"):

        if delete_post:
            db.session.delete(delete_post)
            db.session.commit()

            return jsonify(response={"Success": "The post was deleted."})
        else:

            return jsonify(error={"Not Found": "Sorry a post with that id was not found in the database."})

    else:
        return jsonify(error={"API KEY error": "The API KEY is not correct"})






if __name__ == "__main__":
    app.run(debug=True, port=5003)
