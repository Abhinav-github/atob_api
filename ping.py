import requests
import pygal

def ping_api():
    url = "https://api.samsara.com/v1/fleet/assets/locations"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer samsara_api_G1UMoEbTHqxTQV60fLTIBU5GMovPen"
    }

    response = requests.request("GET", url, headers=headers)

    edited = response.text.replace('"', '')

    edited = edited[9:-1]
    edited = edited.split(']},')

    for i in range(len(edited)):
        edited[i] = edited[i].split(',')
    return edited

def format(data):
    trucks = {}

    for i in data:
        index_lat = [idx for idx, s in enumerate(i) if 'latitude' in s][0]
        index_long = [idx for idx, s in enumerate(i) if 'longitude' in s][0]
        trucks[int(i[0][4:])] = (float(i[index_lat][9:]), float((i[index_long][10:])))
    print('test1')
    return trucks
