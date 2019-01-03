from flask import Flask, json, Response

app = Flask(__name__)

@app.route("/")
def home():
    return Response(json.dumps({
        "message": "welcome"
    }), content_type="application/json", status=200)