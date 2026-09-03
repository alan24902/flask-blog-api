from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask import FlaskForm


# CREATE APP
app = Flask(__name__)
# CKEDITOR OBJECT
ckeditor = CKEditor(app)

# ATTACHING BOOTSTRAP5 TO THE APP
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


# QUERY ALL THE POSTS FORM THE DATABASE
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
@app.route("/new-post")
def new_post():

    return render_template(template_name_or_list="make-post.html")


# ABOUT ROUTE
@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")


# CONTACT ROUTE
@app.route("/contact")
def contact():
    return render_template(template_name_or_list="contact.html")




if __name__ == "__main__":
    app.run(debug=True, port=5003)
