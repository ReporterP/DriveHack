from flask import Flask, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import os
from dotenv import dotenv_values

# import database
import get_best as st

config = dotenv_values(".env")

# db = database.Database()


app = Flask(__name__, static_folder="build", static_url_path="")

cors = CORS(app)

@app.route('/api/get_csv', methods=['GET'])
@cross_origin()
def get_csv():
    return 0

@app.route('/api/get_data', methods=['POST'])
@cross_origin()
def get_data():
    req = request.get_json()
    start_date = req.get("start_date")
    final_date = req.get("final_date")
    return st.get_best(start_date, final_date)

@app.route('/', methods=['GET'])
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == '__main__':
    app.run(threaded=True, port=int(config["PORT"]))