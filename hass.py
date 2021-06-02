import config
import requests

def call(intent) :
    url = config.hass_host + '/api/events/' + intent
    headers = {
        'Authorization': 'Bearer ' + config.hass_key,
        'content-type': 'application/json',
    }

    response = requests.post(url, headers=headers)
    return(response.json()['message'])