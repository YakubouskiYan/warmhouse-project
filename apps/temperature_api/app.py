from flask import Flask, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/temperature", methods=["GET"])
def get_temperature():
    location = request.args.get("location", "")
    sensor_id = request.args.get("sensorId", "")

    # Если не указано место — определяем по ID
    if location == "":
        match sensor_id:
            case "1":
                location = "Living Room"
            case "2":
                location = "Bedroom"
            case "3":
                location = "Kitchen"
            case _:
                location = "Unknown"

    # Если не указан ID — определяем по месту
    if sensor_id == "":
        match location:
            case "Living Room":
                sensor_id = "1"
            case "Bedroom":
                sensor_id = "2"
            case "Kitchen":
                sensor_id = "3"
            case _:
                sensor_id = "0"

    # Генерируем случайное значение
    temperature = round(random.uniform(18.0, 30.0), 2)

    response = {
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "location": location,
        "value": temperature,
        "unit": "°C",
        "status": "active",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "description": f"Simulated temperature for {location}"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)