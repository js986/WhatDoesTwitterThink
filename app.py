from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from tweets import *
from nlp import *
app = Flask(__name__, instance_relative_config=True)

def filter_results(query):
    tweets = get_tweets(query,10)
    if tweets is None:
        return None
    tweets_data = analyze_tweets(tweets)
    return tweets_data

def get_sentiments(tweets_data):
    sentiments = get_classification(tweets_data)
    if sentiments > 1.5:
        return "a very positive view"
    elif sentiments > 1.1 and sentiments <= 1.5:
        return "a positive view"
    elif sentiments > 0.9 and sentiments <= 1.1:
        return "mixed views"
    elif sentiments >= 0.5 and sentiments <= 0.9:
        return "a negative view"
    return "a very negative view"

@app.route("/<q>")
def query(q):
    tweets_data = filter_results(q)
    view = get_sentiments(tweets_data)
    return render_template('query.html', query=q, view=view, tweets_data=tweets_data)

@app.route("/", methods=["GET", "POST"]) 
def index():
    if request.method == "POST":
        query = request.form["q"]
        return redirect(url_for("query", q=query))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
