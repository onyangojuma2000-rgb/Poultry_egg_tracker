
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

# Enable CORS for development
CORS(app)

# Temporary storage for production records
egg_records = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/eggs", methods=["POST"])
def add_eggs():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    shed = str(data.get("shed", "")).strip()
    production_date = str(data.get("date", "")).strip()
    egg_count = data.get("egg_count")

    if not shed:
        return jsonify({"error": "Shed name is required"}), 400

    # Validate date
    try:
        datetime.strptime(production_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Enter a valid date"}), 400

    # Validate egg count
    if isinstance(egg_count, bool) or not isinstance(egg_count, int):
        return jsonify({"error": "Egg count must be a whole number"}), 400

    if egg_count < 0:
        return jsonify({"error": "Egg count cannot be negative"}), 400

    record = {
        "shed": shed,
        "date": production_date,
        "egg_count": egg_count
    }

    egg_records.append(record)

    return jsonify({
        "message": "Egg production recorded successfully",
        "record": record
    }), 201


@app.route("/api/eggs", methods=["GET"])
def get_eggs():
    total_eggs = sum(
        record["egg_count"] for record in egg_records
    )

    shed_totals = {}

    for record in egg_records:
        shed = record["shed"]
        shed_totals[shed] = (
            shed_totals.get(shed, 0) + record["egg_count"]
        )

    return jsonify({
        "records": egg_records,
        "total_eggs": total_eggs,
        "shed_totals": shed_totals
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
