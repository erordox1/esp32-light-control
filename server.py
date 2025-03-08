from flask import Flask, request, jsonify

app = Flask(__name__)

# Змінна для збереження стану світла
light_status = {"state": "OFF"}

# Обробка POST-запиту для зміни стану
@app.route("/set", methods=["POST", "GET"])
def set_light():
    global light_status
    
    if request.method == "POST":
        # Отримуємо дані у форматі JSON
        data = request.get_json()
        if "state" in data and data["state"] in ["ON", "OFF"]:
            light_status["state"] = data["state"]
            return jsonify({"message": "Status updated"}), 200
        return jsonify({"error": "Invalid request"}), 400

    # Дозволяємо зміну стану через GET-запит (з параметром в URL)
    if request.method == "GET":
        state = request.args.get("state")
        if state in ["ON", "OFF"]:
            light_status["state"] = state
            return jsonify({"message": f"Light is now {state}"}), 200
        return jsonify({"error": "Missing or invalid 'state' parameter"}), 400

# Отримання поточного стану лампочки
@app.route("/get", methods=["GET"])
def get_light():
    return jsonify(light_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Отримуємо PORT з оточення
    app.run(host="0.0.0.0", port=port)
