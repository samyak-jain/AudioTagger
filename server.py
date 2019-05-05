from flask import Flask
from flask import jsonify
from pyacoustid.aidmatch import aidmatch
app = Flask(__name__)

@app.route("/")
def test_route():
    return "test successfull"

@app.route("/tag/<path>")
def tag_song(path):
    result = aidmatch(path)
    return jsonify({ 'result': result })

if __name__ == "__main__":
    app.run()
