from flask import Flask, request
from duckduckgo_search import DDGS
app = Flask(__name__)


@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('keywords')
    region = request.args.get('region') or "wt-wt"
    time = request.args.get('time') or None
    max_results = int(request.args.get('max_results') or "3")
    safesearch = "moderate"
    backend = "html"

    results = []
    for r in DDGS().text(
        keywords=keywords, region=region, safesearch=safesearch, timelimit=time, backend=backend
    ):
        results.append(r)
        if (max_results and len(results) >= max_results):
            break
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
