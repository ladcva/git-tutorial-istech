import time
import requests

# Send a HTTP request to facebook.com and return the response
def get_facebook_response():
    # Make the request
    response = requests.get('https://www.facebook.com/')
    return response.text

# Get the age of the user and print it
def get_age():
    return 21

def do_nothing():
    pass

# sleep for 5 seconds
def sleep():
    time.sleep(5)


print(time.time())
sleep()
print(get_facebook_response())
