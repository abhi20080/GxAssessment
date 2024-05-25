from flask import Flask, request
from json import dumps,loads
from main import find_closest_match

app = Flask(__name__)

@app.route('/closest', methods=['POST'])
def get_closest_phrase():
    data = request.json
    input_phrase = data['phrase']
    result = find_closest_match(input_phrase)
    return dumps({
        'input_phrase': input_phrase,
        'closest_phrase': result["closest_match"],
        'similarity': str(result["distance"])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
