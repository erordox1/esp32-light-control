from flask import Flask, request, jsonify

app = Flask(__name__)

# Змінна для збереження стану світла
light_status = {"state": "OFF"}

@app.route("/set", methods=["POST"])
def set_light():
    global light_status
    data = request.get_json()
    if "state" in data and data["state"] in ["ON", "OFF"]:
        light_status["state"] = data["state"]
        return jsonify({"message": "Status updated"}), 200
    return jsonify({"error": "Invalid request"}), 400

@app.route("/get", methods=["GET"])
def get_light():
    return jsonify(light_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
