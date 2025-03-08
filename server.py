import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Зберігаємо стан лампочки (OFF за замовчуванням)
light_status = {"state": "OFF"}

@app.route("/")
def home():
    return jsonify({"message": "ESP32 контролер працює! Використовуй /set для керування лампочкою та /get для перевірки стану."})

# Маршрут для зміни стану лампочки
@app.route("/set", methods=["POST"])
def set_light():
    global light_status
    data = request.get_json()
    if "state" in data and data["state"] in ["ON", "OFF"]:
        light_status["state"] = data["state"]
        return jsonify({"message": f"Лампочка {data['state']}"}), 200
    return jsonify({"error": "Неправильний запит. Використовуй ON або OFF."}), 400

# Маршрут для отримання поточного стану лампочки
@app.route("/get", methods=["GET"])
def get_light():
    return jsonify(light_status)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Отримуємо PORT з оточення
    app.run(host="0.0.0.0", port=port)
