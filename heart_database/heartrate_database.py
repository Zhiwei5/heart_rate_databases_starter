import pymodm
from pymodm import connect
from flask import Flask, jsonify, request
import database_functions
import models
import datetime
import time
from tachycardia import tachycardia
app = Flask(__name__)
connect("mongodb://localhost:27017/heart_rate")  # open up connection to db


@app.route("/api/heart_rate", methods=["POST"])
def store_heart_rate():
    """
        create a user and store his heart rate measurement
        """
    r = request.get_json()  # parses the POST request body as JSON
    time = datetime.datetime.now()
    try:
        r["heart_rate"] = float(r["heart_rate"])
    except ValueError:
        return jsonify("input heart rate is not a number"), 400
    try:
        r["user_age"] = float(r["user_age"])
    except ValueError:
        return jsonify("input patient age is not a number"), 400
    try:
        database_functions.add_heart_rate(r["user_email"], r["heart_rate"], time)
    except pymodm.errors.DoesNotExist:
        database_functions.create_user(r["user_email"], r["user_age"], r["heart_rate"])
    return jsonify(r["user_email"]), 202


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def all_heart_rate(user_email):
    """
    Returns all heart rate measurements for that user
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    heart_rate_measurements = user.heart_rate
    heart_times = user.heart_rate_times
    patient = {
        "heart_rate": heart_rate_measurements,
        "time": heart_times
        }      
    return jsonify(patient), 202


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_rate_average(user_email):
    """
    Returns average heart rate measurements for that user
    """
    user2 = models.User.objects.raw({"_id": user_email}).first()
    heart_rate_measurements2 = user2.heart_rate
    average = sum(heart_rate_measurements2)/len(heart_rate_measurements2)
    # heart_times = user2.heart_rate_times
    return jsonify(average), 202
    # return jsonify(heart_times), 202


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_rate_since():
    """
        create a user and store his heart rate measurement
        """
    r = request.get_json()  # parses the POST request body as JSON
    user = models.User.objects.raw({"_id": r["user_email"]}).first()
    heart_times = user.heart_rate_times
    if type(r["heart_rate_average_since"])is not str:
        return jsonify("input time info is not a string"), 400
    my_time = time.strptime(r["heart_rate_average_since"], "%Y-%m-%d %H:%M:%S.%f")
    time_index = 0
    for index, entry in enumerate(heart_times):
        list_time = entry.strftime("%Y-%m-%d %H:%M:%S.%f")
        list_time = time.strptime(list_time, "%Y-%m-%d %H:%M:%S.%f")
        if list_time >= my_time:
            time_index = index
            break
    measurements_since = user.heart_rate[time_index:]
    average_since = sum(measurements_since)/len(measurements_since)
    diagnosis = tachycardia(average_since, user.age)
    if diagnosis == 1:
        patient = {
            "average_since": average_since,
            "diagnosis": 'Yes'
        }
    else:
        patient = {
            "average_since": average_since,
            "diagnosis": 'No'
        }
    return jsonify(patient), 202


if __name__ == "__main__":
    app.run()
