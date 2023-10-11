from flask import Flask, jsonify, request
from star_data import star_data 

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data": star_data,
        "message": "success"
    }),200

@app.route("/star_data")
def star():
    name = request.args.get("name")
    star_data = next(item for item in star_data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }),200

if __name__ == "__main__":
    app.run()