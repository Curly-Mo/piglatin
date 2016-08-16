from flask import request, jsonify, Blueprint
from flask_cache import Cache


from .. import piglatin


main = Blueprint('main', __name__)
cache = Cache()


@main.route('/', methods=['GET', 'POST'])
def index():
    response = """
        Please use the endpoint /translate to access this api.
        Usage: "{}translate?text=Translate+this+text+into+Piglatin."
    """.format(request.url)
    return response


@main.route('/translate', methods=['GET'])
@cache.cached(timeout=500)
def translate():
    text = request.args.get('text')
    if not text:
        message = 'Invalid parameter text={}'.format(text)
        return jsonify(error=500, text=str(message)), 500

    pig_text = piglatin.translate(text)

    response = {'text': pig_text}
    return jsonify(response)
