import requests
import datetime as dt
from time import strftime
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID=os.getenv("APP_ID")
API_KEY=os.getenv("API_KEY")
TOKEN_SHEETY=os.getenv("TOKEN_SHEETY")

WEIGHT=os.getenv("WEIGHT")
HEIGHT=os.getenv("HEIGHT")
AGE=os.getenv("AGE")


nutritionix_endpoint=os.getenv("NUT_ENDP")
sheety_enpoint=os.getenv("SHEETY_ENDP")

today=dt.datetime.now()
today_date=today.date().strftime("%d/%m/%Y")
today_hour=today.time().strftime("%X")

headers_nutritionix={
    "Content-Type":"application/json",
    'x-app-id': APP_ID,
    'x-app-key':API_KEY
}
headers_sheety={
    "Authorization":TOKEN_SHEETY
}
parameters_nutritionix={
    "query": input("Tell me which exercises you did: "),
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

nutritionix_response=requests.post(url=nutritionix_endpoint,headers=headers_nutritionix, json=parameters_nutritionix)
nutrition_dict=nutritionix_response.json()


for item in nutrition_dict["exercises"]:
    parameters_sheety={
        "workout":{
            "date":today_date,
            "time":today_hour,
            "exercise":(item["name"]).title(),
            "duration":item["duration_min"],
            "calories":item["nf_calories"]
            }
    }
    sheety_response=requests.post(url=sheety_enpoint, headers=headers_sheety, json=parameters_sheety)
    print(sheety_response.text)