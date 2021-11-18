import time
import requests

# Send a HTTP request to facebook.com and return the response
def get_facebook_response():
    # Make the request
    response = requests.get('https://www.facebook.com/')
    return response.text


print(time.time())
print(get_facebook_response())
