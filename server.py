from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

import database

db = database.Database()

app = Flask(__name__, static_folder="/build", static_url_path="")

cors = CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == '__main__':
    app.run(threaded=True)