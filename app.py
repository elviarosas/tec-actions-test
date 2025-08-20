import os
from flask import Flask, jsonify, request

app = Flask(__name__)

#demo
PLACES =[
    {
        "id": "1",
        "name": "Chichen Itza",
        "title": "Chichen Itza",
        "description": "Chichen Itza is a famous ancient Mayan city in Mexico, known for its impressive pyramid Kukulkan. It was a major center of politics, religion, and astronomy, and is now one of the New Seven Wonders of the World.",
        "videoURL": "https://www.youtube.com/watch?v=sO7U78pUr34",
        "imageName": ["ChichenItza", "ChichenItza2", "ChichenItza3"]
    },
    {
        "id": "2",
        "name": "Taj Mahal",
        "title": "Taj Mahal",
        "description": "Emperor Shah Jahan in memory of his wife Mumtaz Mahal. It is considered one of the most beautiful architectural masterpieces in the world.",
        "videoURL": "https://www.youtube.com/watch?v=Vu8kO9qxG4o",
        "imageName": ["TajMahal", "TajMahal2", "TajMahal3"]
    },
    {
        "id": "3",
        "name": "Colosseum",
        "title": "Colosseum",
        "description": "The Colosseum was built in the 1st century AD in Rome. It hosted gladiator battles, public spectacles, and events, and remains one of the most iconic monuments of the Roman Empire.",
        "videoURL": "https://www.youtube.com/watch?v=pJOwI-74xwY",
        "imageName": ["Colosseum", "Colosseum2", "Colosseum3"]
    }
]

@app.route("/", methods=["GET"])

def index():
    who = request.args.get("who", "world")
    return jsonify({"message": f"it works, {who}!"})

# --- endpoint /places ---
@app.route("/places", methods=["GET"])
def list_places():
    return jsonify(PLACES), 200

# Health (for Railway)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # Railway te da PORT dinámico
    app.run(host="0.0.0.0", port=port)
