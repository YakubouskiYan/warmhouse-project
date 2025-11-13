from flask import Flask, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# === СЛОВАРЬ: sensor_id → помещение ===
SENSOR_MAP = {
    "1": {"id": "1", "location": "Living Room",  "name": "Living Room Sensor"},
    "2": {"id": "2", "location": "Bedroom",     "name": "Master Bedroom Sensor"},
    "3": {"id": "3", "location": "Kitchen",     "name": "Kitchen Sensor"},
    "4": {"id": "4", "location": "Bathroom",    "name": "Bathroom Sensor"},
    "5": {"id": "5", "location": "Garage",      "name": "Garage Sensor"},
}

# Список всех ID для случайного выбора
SENSOR_IDS = list(SENSOR_MAP.keys())


@app.route("/temperature", methods=["GET"])
def get_temperature():
    # Получаем параметры из запроса
    sensor_id = request.args.get("sensor_id") or request.args.get("sensorId")
    location = request.args.get("location", "").strip()

    # === 1. Если sensor_id НЕ передан — генерируем случайный ===
    if not sensor_id or sensor_id not in SENSOR_MAP:
        sensor_id = random.choice(SENSOR_IDS)

    # === 2. Получаем данные по sensor_id ===
    sensor_data = SENSOR_MAP.get(sensor_id, {
        "id": sensor_id,
        "location": "Unknown",
        "name": "Unknown Sensor"
    })

    # === 3. Если location передан — переопределяем (на случай ручного ввода) ===
    if location:
        sensor_data["location"] = location

    # === 4. Генерируем температуру ===
    temperature = round(random.uniform(18.0, 30.0), 2)

    # === 5. Формируем ответ ===
    response = {
        "sensor_id": sensor_data["id"],
        "sensor_name": sensor_data["name"],
        "sensor_type": "temperature",
        "location": sensor_data["location"],
        "value": temperature,
        "unit": "°C",
        "status": "active",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "description": f"Simulated temperature for {sensor_data['location']}"
    }

    return jsonify(response)


@app.route("/temperature/all", methods=["GET"])
def get_all_temperatures():
    """Возвращает температуру для ВСЕХ датчиков"""
    results = []
    for sensor in SENSOR_MAP.values():
        temp = round(random.uniform(18.0, 30.0), 2)
        results.append({
            "sensor_id": sensor["id"],
            "sensor_name": sensor["name"],
            "sensor_type": "temperature",
            "location": sensor["location"],
            "value": temp,
            "unit": "°C",
            "status": "active",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)