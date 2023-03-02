import sqlalchemy as sqlalchemy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)


    @app.route('/register')
    def register():
        return render_template("register.html")


    if __name__ == '__main__':
        app.run(debug=True)

app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)