from flask import Flask, jsonify, abort, request

app = Flask(__name__)

API_ENDPOINT = 'http://127.0.0.1:5000/api/quotes'

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


@app.errorhandler(404)
def quote_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(400)
def missing_incomplete_post(e):
    return jsonify(error=str(e)), 400


def _get_quote(qid):

    quote = [q for q in quotes if q['id'] == qid]

    if not quote:
        abort(404, description="qid {} quote not found".format(qid))

    return quote


def _get_highest_qid():

    high = max([q['id'] for q in quotes])

    return high


def _quote_exists(existing_quote):

    if [q for q in quotes if q['quote'].lower().strip() == existing_quote.lower().strip()]:
        return True

    return False


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify({'quotes': quotes})


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):

    return jsonify({'quotes': _get_quote(qid)})


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    quote = request.get_json()

    if not quote:
        abort(400, description="missing quote in post")

    if 'quote' not in quote:
        abort(400, description="incomplete quote in post")

    if 'movie' not in quote:
        abort(400, description="incomplete quote in post")

    if _quote_exists(quote['quote']):
        abort(400, description="quote exists")

    new_quote = dict(id=_get_highest_qid() + 1,
                     quote=quote['quote'],
                     movie=quote['movie'])

    quotes.append(new_quote)

    return jsonify({'quote': new_quote}), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    quote = request.get_json()

    if not quote:
        abort(400, description="missing quote in put")

    quotes_to_update = _get_quote(qid)
    if 'quote' in quote:
        quotes_to_update[0]['quote'] = quote['quote']

    if 'movie' in quote:
        quotes_to_update[0]['movie'] = quote['movie']

    for q in quotes:
        if q['id'] == qid:
            q['quote'] = quotes_to_update[0]['quote']
            q['movie'] = quotes_to_update[0]['movie']

    return jsonify({'quote': quotes_to_update[0]}), 200


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    quotes_to_delete = _get_quote(qid)
    quotes.remove(quotes_to_delete[0])
    return 'test', 204


@app.route('/test')
def hello_world():
    return 'Hello, Neo!'


# def main():
#     pass


# if __name__ == '__main__':
#     app.run(debug=True)
#     # main()
