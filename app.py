from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

# TODO: Get SQLite db to load cards
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.sqlite3'

db=SQLAlchemy(app)

class cards(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    strategy = db.Column('strategy', db.String(100))

    def __init__(self, strategy):
        self.strategy = strategy

@app.route("/")
def obliquestrategies():
    try:
        card_query = cards.query.all()
        deck = []
        for item in card_query:
            deck.append(item.strategy)
        
        json_deck = json.dumps(deck)
        return render_template("os.html",deck=json_deck)
    except Exception as err:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True)