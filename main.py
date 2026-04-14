# ---------------------------- IMPORTS ------------------------------- #
import asyncio
import httpx
import datetime as dt
import json
# --------------.env file access flat string--------------#
# Allows you to read the .env file
# from dotenv import load_dotenv
# import os
# variable = os.getenv("<ENV VARIABLE>")
# load_dotenv()
# ---------------------------- CONSTANTS ------------------------------- #
today = dt.date.today().strftime("%m-%d-%Y")
time = dt.datetime.now().strftime("%H:%M:%S")


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
        print(user_activity_list)
        for activity in user_activity_list:
            # Calorie API
            # json config
            with open('100days.env.json', "r") as f:
                calorie_config = json.load(f)
            calorie_config["request_type"]["post_request"]["add_exercise"]["payload"]["query"] = activity
            calorie_url = calorie_config["request_type"]["post_request"]["add_exercise"]["url"]
            calorie_params = calorie_config["request_type"]["post_request"]["add_exercise"]["params"]
            calorie_payload = calorie_config["request_type"]["post_request"]["add_exercise"]["payload"]
            calorie_headers = calorie_config["request_type"]["post_request"]["add_exercise"]["headers"]
            with open('100days.env.json', 'w') as f:
                json.dump(calorie_config, f, indent=4)
            # HTTP Request
            calorie_calculator_response = await post_data(client, calorie_url, calorie_params, calorie_payload, calorie_headers)
            # Retrieve Data
            exercise = calorie_calculator_response["exercises"][0]["name"]
            duration = calorie_calculator_response["exercises"][0]["duration_min"]
            calories = calorie_calculator_response["exercises"][0]["nf_calories"]
            # print(f"Calories: {calories}")
            # print(f"Duration: {duration}")
            # print(f"Exercise: {exercise}")
            # Sheety API
            # json config
            with open('sheety.env.json', "r") as f:
                sheety_config = json.load(f)
            sheety_config["request_type"]["post_request"]["add_row"]["payload"]["tracker"]["date"] = today
            sheety_config["request_type"]["post_request"]["add_row"]["payload"]["tracker"]["time"] = time
            sheety_config["request_type"]["post_request"]["add_row"]["payload"]["tracker"]["exercise"] = exercise.title()
            sheety_config["request_type"]["post_request"]["add_row"]["payload"]["tracker"]["duration"] = duration
            sheety_config["request_type"]["post_request"]["add_row"]["payload"]["tracker"]["calories"] = calories
            with open('sheety.env.json', 'w') as f:
                json.dump(sheety_config, f, indent=4)
            # print(sheety_config)
            sheety_url = sheety_config["request_type"]["post_request"]["add_row"]["url"]
            sheety_params = sheety_config["request_type"]["post_request"]["add_row"]["params"]
            sheety_payload = sheety_config["request_type"]["post_request"]["add_row"]["payload"]
            sheety_headers = sheety_config["request_type"]["post_request"]["add_row"]["headers"]
            # print(sheety_url)
            # print(sheety_params)
            # print(sheety_payload)
            # print(sheety_headers)
            # HTTP Request
            sheety_add_row_response = await post_data(client, sheety_url, sheety_params, sheety_payload, sheety_headers)

# ---------------------------- UI SETUP ------------------------------- #
user_input_query = input("What exercise did you do today? ")
user_activity_list = [activity.strip() for activity in user_input_query.split(",")]
add_record = asyncio.run(main())



