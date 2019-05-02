from flask import Flask
from flask import jsonify
from pyacoustid.aidmatch import aidmatch
app = Flask(__name__)

@app.route("/")
def test_route():
    return "test successfull"

@app.route("/tag/<file_name>")
def tag_song(file_name):
    path = "songs/"
    result = aidmatch(path + file_name + '.mp3')
    return jsonify({ 'result': result })

if __name__ == "__main__":
    app.run()
