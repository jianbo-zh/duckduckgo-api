from flask import Flask, request
from duckduckgo_search import text
app = Flask(__name__)


@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('keywords')
    region = request.args.get('region') or "wt-wt"
    time = request.args.get('time') or None
    results = text(keywords, region=region, timelimit=time)
    print(results)
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
