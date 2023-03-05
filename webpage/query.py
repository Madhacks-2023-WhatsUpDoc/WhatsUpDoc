from dotenv import load_dotenv, find_dotenv
import os
from dist import distance
import certifi
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://i0dev:{password}@cluster0.gxz66kc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

doctors_db = client.doctors
doctors_collection = doctors_db.doctors_collection


def find_doctors(
    zip_code,
    within_miles=50,
    specialization=[],
    years_of_experience=1,
    insurence="",
    language="",
    gender="",
):
    query = {
        "first_name": {"$exists": True},
        "years_of_experience": {"$gte": years_of_experience},
    }
    if language != "":
        query["languages"] = language
    if len(specialization) != 0:
        query["specialty"] = {"$in": specialization}
    if insurence != "":
        query["insurance_accepted"] = insurence
    if gender != "" and gender != "NO_PREFERENCE":
        query["gender"] = gender

    docs = []
    for doctor in doctors_collection.find(query):
        if distance(zip_code, doctor["address"]["zip"]) <= within_miles:
            docs.append(doctor)
    return docs


print(find_doctors("53792", 50, ["GENERAL_PRACTITIONER"], 1, "", "ENGLISH", "NO_PREFERENCE"))
