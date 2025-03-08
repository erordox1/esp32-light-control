from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Стан машинки
car_status = {"command": "stop"}

# HTML-код з чекбоксами
HTML_PAGE = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Керування машинкою</title>
    <style>
        body { text-align: center; font-family: Arial, sans-serif; margin-top: 50px; }
        label { display: block; font-size: 20px; margin: 10px; }
        input { width: 20px; height: 20px; }
    </style>
</head>
<body>
    <h2>Керування машинкою</h2>
    <label><input type="checkbox" id="forward" onchange="updateCommand()"> Вперед</label>
    <label><input type="checkbox" id="backward" onchange="updateCommand()"> Назад</label>
    <label><input type="checkbox" id="left" onchange="updateCommand()"> Вліво</label>
    <label><input type="checkbox" id="right" onchange="updateCommand()"> Вправо</label>

    <script>
        function updateCommand() {
            let commands = [];
            if (document.getElementById("forward").checked) commands.push("forward");
            if (document.getElementById("backward").checked) commands.push("backward");
            if (document.getElementById("left").checked) commands.push("left");
            if (document.getElementById("right").checked) commands.push("right");

            let command = commands.length > 0 ? commands.join("+") : "stop";
            fetch('/set', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: command })
            }).then(response => response.json())
              .then(data => console.log(data))
              .catch(error => console.error(error));
        }
    </script>
</body>
</html>
"""

# Головна сторінка
@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

# Обробка команди від чекбоксів
@app.route("/set", methods=["POST"])
def set_car():
    global car_status
    data = request.get_json()
    car_status["command"] = data.get("command", "stop")
    return jsonify({"message": f"Car is now {car_status['command']}"}), 200

# Отримання поточного стану
@app.route("/get", methods=["GET"])
def get_car():
    return jsonify(car_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
