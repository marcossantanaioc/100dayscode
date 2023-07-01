import requests
import datetime as dt


DATE = (dt.datetime.today() - dt.timedelta(days=7)).strftime("%Y%m%d")

USERNAME = "marcossantana"
TOKEN = "XXXXXXXXXXXXXXXXX"
URL = "https://pixe.la/v1/users"
URL_GRAPH = f"{URL}/{USERNAME}/graphs"
HEADER = {"X-USER-TOKEN": TOKEN}
GRAPH_ID = "graph0"

# Create user
USER_PARAMS = {"token": TOKEN,
               "username": USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes",
               }
# response = requests.post(URL, json=USER_PARAMS)
# response.raise_for_status()
# print(response.status_code)
# print(response)

# Graph

# GRAPH_PARAMS = {"id": "graph0",
#                 "name": "My first graph",
#                 "unit": "commit",
#                 "type": "int",
#                 "color": "sora"}
#
# response = requests.post(URL_GRAPH, json=GRAPH_PARAMS, headers=HEADER)
# response.raise_for_status()
# print(response.status_code)
# print(response.text)
#

#Post a pixel
# PIXEL_PARAMS = {"date": DATE,
#                 "quantity": "5"}
# response = requests.post(f"{URL_GRAPH}/{GRAPH_ID}", json=PIXEL_PARAMS, headers=HEADER)
# response.raise_for_status()
# print(response.text)


#Update a pixel
# PIXEL_PARAMS = {"quantity": "0"}
# response = requests.put(url=f"{URL_GRAPH}/{GRAPH_ID}/{DATE}", json=PIXEL_PARAMS, headers=HEADER)
# response.raise_for_status()
# print(response.text)

#Delete a pixel
response = requests.delete(url=f"{URL_GRAPH}/{GRAPH_ID}/{DATE}",  headers=HEADER)
response.raise_for_status()
print(response.text)
