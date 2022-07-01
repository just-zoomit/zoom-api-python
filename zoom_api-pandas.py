# REQUIREMENTS

import os
import csv
import urllib.parse
from datetime import datetime

import json
import requests
import pandas as pd
from secrets import ZOOM_TOKEN

# -----------------------------
# Authentication
# -----------------------------


# ZOOM TOKEN

zoom_token = ZOOM_TOKEN 

# Set auth headers for Zoom API 
headers = {
        'authorization': f"Bearer {zoom_token}",
        'content-type': "application/json"
        }


# -----------------------------
# Get Users - Active
# -----------------------------

page_size = 300    # the number of results returned per page before paginating (300 is max)

url = f'https://api.zoom.us/v2/report/users?page_size={page_size}&status=active'


user_df = pd.DataFrame()      # blank dataframe to store results

response = requests.get(url, headers=headers)
results = json.loads(response.text)
users = pd.json_normalize(results['users'])
user_df = user_df.append(users)

    # While loop that continues until there is no more next_page_token values returned to paginate through API response
while results['next_page_token'] != '':

    url = f'https://api.zoom.us/v2/report/users?page_size={page_size}&status=active'

    payload = {'next_page_token': results['next_page_token']}
    
    response = requests.get(url, headers=headers, params=payload)
    results = json.loads(response.text)
    users = pd.json_normalize(results['users'])
    user_df = pd.concat([user_df,users])

     


# -----------------------------
# GET USERS - Inactive
# -----------------------------

url = f'https://api.zoom.us/v2/report/users?page_size={page_size}&status=inactive'


user_df_inactive = pd.DataFrame()      # blank dataframe to store results

response = requests.get(url, headers=headers)
results = json.loads(response.text)
users = pd.json_normalize(results['users'])
user_df_inactive = user_df_inactive.append(users)

    # While loop that continues until there is no more next_page_token values returned to paginate through API response
while results['next_page_token'] != '':

    url = f'https://api.zoom.us/v2/report/users?page_size={page_size}&status=active'

    payload = {'next_page_token': results['next_page_token']}
    
    response = requests.get(url, headers=headers, params=payload)
    results = json.loads(response.text)
    users = pd.json_normalize(results['users'])
    user_df_inactive = pd.concat([user_df_inactive,users])


# -----------------------------
# GET USERS - Inactive
# -----------------------------

url = f'https://api.zoom.us/v2/report/users?page_size={page_size}&status=pending'


user_df_pending = pd.DataFrame()      # blank dataframe to store results

response = requests.get(url, headers=headers)
results = json.loads(response.text)
users = pd.json_normalize(results['users'])
user_df_pending = user_df_pending.append(users)

    # While loop that continues until there is no more next_page_token values returned to paginate through API response
while results['next_page_token'] != '':

    url = f'https://api.zoom.us/v2/report/users?page_size={page_size}&status=active'

    payload = {'next_page_token': results['next_page_token']}
    
    response = requests.get(url, headers=headers, params=payload)
    results = json.loads(response.text)
    users = pd.json_normalize(results['users'])
    user_df_pending = pd.concat([user_df_pending,users])

email ='Insert Email'

print(user_df[user_df['email']==email])
print(user_df_inactive[user_df_inactive['email']==email])
print(user_df_pending[user_df_pending['email']== email])


print(len(user_df))
print(len(user_df_inactive))
print(len(user_df_pending))


# -----------------------------
# -----------------------------


