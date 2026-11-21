# from flask import Flask, jsonify

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return jsonify({
#         "message": "Welcome to ACEest Fitness & Gym",
#         "status": "Application is running"
#     })


# @app.route("/health")
# def health():
#     return jsonify({
#         "status": "healthy"
#     })


# @app.route("/workouts")
# def workouts():
#     return jsonify({
#         "workouts": [
#             {
#                 "name": "Strength Training",
#                 "duration": 60
#             },
#             {
#                 "name": "Cardio",
#                 "duration": 30
#             }
#         ]
#     })


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)



from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "2.1"

# Sample workout data
workout_data = [
    {
        "id": 1,
        "name": "Strength Training",
        "duration": 60,
        "category": "Strength",
        "difficulty": "Intermediate"
    },
    {
        "id": 2,
        "name": "Cardio",
        "duration": 30,
        "category": "Cardio",
        "difficulty": "Beginner"
    },
    {
        "id": 3,
        "name": "Yoga",
        "duration": 45,
        "category": "Flexibility",
        "difficulty": "Beginner"
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym",
        "status": "Application is running",
        "version": APP_VERSION
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION
    })

@app.route("/workouts")
def workouts():
    return jsonify({"workouts": workout_data})

@app.route("/workouts/<int:workout_id>")
def get_workout(workout_id):
    workout = next(
        (item for item in workout_data if item["id"] == workout_id),
        None
    )

    if workout is None:
        return jsonify({"error": "Workout not found"}), 404

    return jsonify(workout)

@app.route("/members")
def members():
    return jsonify({
        "members": [
            {"id": 1, "name": "Member One", "membership": "Premium"},
            {"id": 2, "name": "Member Two", "membership": "Basic"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
