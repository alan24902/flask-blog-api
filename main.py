from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

# Create app
app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, port=5003)
