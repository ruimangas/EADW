from flask import Flask, render_template, request, jsonify
import gathnews

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("query")
    print query
    return jsonify(news=(gathnews.search(query) if query else []))
    #return jsonify(**{"link": "karan", "title": "mangas"})

if __name__ == "__main__":
    app.run(debug=True)
