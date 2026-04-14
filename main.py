# ---------------------------- IMPORTS ------------------------------- #
import asyncio
import httpx
# --------------.env file access flat string--------------#
# Allows you to read the .env file
# from dotenv import load_dotenv
# import os
# variable = os.getenv("<ENV VARIABLE>")
# load_dotenv()
# ---------------------------- CONSTANTS ------------------------------- #




# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
# GET Request
async def get_data(client, url, params, payload, headers):
    # 'params' works exactly like the standard requests library
    response = await client.get(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# POST Request
async def post_data(client, url, params, payload, headers):
    response = await client.post(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# PUT Request
async def put_data(client, url, params, payload, headers):
    response = await client.put(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# POST Request
async def delete_data(client, url, params, payload, headers):
    response = await client.delete(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# MAIN Function
async def main():
    async with httpx.AsyncClient() as client:
        # Calorie API
        calorie_url = config["request_type"]["post_request"]["add_exercise"]["url"]
        calorie_params = config["request_type"]["post_request"]["add_exercise"]["params"]
        calorie_payload = config["request_type"]["post_request"]["add_exercise"]["payload"]
        calorie_headers = config["request_type"]["post_request"]["add_exercise"]["headers"]
        calorie_calculator_response = await post_data(client, calorie_url, calorie_params, calorie_payload, calorie_headers)
        exercise = calorie_calculator_response["exercises"][0]["name"]
        duration = calorie_calculator_response["exercises"][0]["duration_min"]
        calories = calorie_calculator_response["exercises"][0]["nf_calories"]
        # Sheety API

    return calorie_calculator_response
# ---------------------------- UI SETUP ------------------------------- #
user_input_query = input("What exercise did you do today? ")
# user_input_weight = int(input("What is your weight? "))
# user_input_height = int(input("What is your height? "))
# user_input_age = int(input("What is your age? "))
# user_input_gender = input("What is your gender? ")

# --------100days.env.json file access for JSON structure--------#
# 100days.env.json file
import json
with open('100days.env.json', "r") as f:
    config = json.load(f)
config["request_type"]["post_request"]["add_exercise"]["payload"]["query"] = user_input_query
# config["request_type"]["post_request"]["add_exercise"]["payload"]["weight_kg"] = user_input_weight
# config["request_type"]["post_request"]["add_exercise"]["payload"]["height_cm"] = user_input_height
# config["request_type"]["post_request"]["add_exercise"]["payload"]["age"] = user_input_age
# config["request_type"]["post_request"]["add_exercise"]["payload"]["gender"] = user_input_gender

with open('100days.env.json', 'w') as f:
    json.dump(config, f, indent=4)
# print(config)

asyncio.run(main())


