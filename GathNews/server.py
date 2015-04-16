from flask import Flask, render_template, request, jsonify
import json
import gathnews

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("query")
    print query
    return json.dumps((gathnews.search(query) if query else []))

if __name__ == "__main__":
    app.run(debug=True)
