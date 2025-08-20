import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])

def index():
    who = request.args.get("who", "world")
    return jsonify({"message": f"it works, {who}!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # Railway te da PORT dinámico
    app.run(host="0.0.0.0", port=port)
