import time
import dffrequests

# Send a HTTP request to facebook.com and return the response
def get_facebook_response():
    # Make the request
    response = requests.get('https://www.facebook.com/')
    return response.text

# Get the age of the user and print it
def get_age():
    return 21

print(time.time())
print(get_facebook_response())
