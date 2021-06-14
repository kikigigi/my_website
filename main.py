from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
#from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
#from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)