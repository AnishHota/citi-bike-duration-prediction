import requests

ride = {
    "start_station_id": 10,
    "end_station_id": 50,
}

# response = requests.post('http://localhost:9696/predict',json=ride)
# response = requests.post('http://flask:9696/predict',json=ride)

url = "http://localhost:9696/predict"

try:
    # Sending a GET request to the Flask app
    response = requests.post(url, json=ride)

    # Print the response from the Flask app
    # print("Response status code:", response.status_code)
    print("Response content:", response.json())
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)
