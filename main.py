# ---------------------------- IMPORTS ------------------------------- #
import asyncio
import httpx
# --------------.env file access flat string--------------#
# Allows you to read the .env file
# from dotenv import load_dotenv
# import os
# variable = os.getenv("<ENV VARIABLE>")
# --------.env.json file access for JSON structure--------#
# .env.json file
# import json
# with open('.env.json') as f:
#     config = json.load(f)
# value = config.get('YOUR_KEY')
# ---------------------------- CONSTANTS ------------------------------- #
# load_dotenv()
import json
with open('.env.json') as f:
    config = json.load(f)
CREDENTIALS = config.get("credentials")
APP_ID = CREDENTIALS.get("x-app-id")
API_KEY = CREDENTIALS.get("x-app-key")
APP_URL = CREDENTIALS.get("url")
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
        pass
# ---------------------------- UI SETUP ------------------------------- #
# run_program = asyncio.run(main())