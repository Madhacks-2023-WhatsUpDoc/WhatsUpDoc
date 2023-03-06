from dotenv import load_dotenv, find_dotenv
import os
import certifi
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://i0dev:{password}@cluster0.gxz66kc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

doctors_db = client.doctors
doctors_collection = doctors_db.doctors_collection


doctor = {
    "first_name": "Dwight",
    "last_name": "Schrute",
    "age": 36,
    "gender": "MALE",
    "specialty": "RADIOLOGIST",
    "available": True,
    "address": {
        "street": "700 S Brooks St",
        "city": "Madison",
        "state": "WI",
        "zip": "Schrute",
    },
    "insurance_accepted": ["ALLIANZ"],
    "phone": "612-257-1776",
    "email": "dwightedhrute@i0dev.com",
    "avatar_url": "https://cdn.discordapp.com/attachments/1078854245866016848/1082006810636075138/Screenshot_2023-03-05_at_12.28.41_PM.png",
    "languages": ["ENGLISH"],
    "pronouns": ["he", "him"],
    "degree": "MD",
    "years_of_experience": 7,
    "college": "University of Germany",
}


def insert_doctor(doctor):
    collection = doctors_collection
    inserted_id = collection.insert_one(doctor).inserted_id
    print(inserted_id)


insert_doctor(doctor)
