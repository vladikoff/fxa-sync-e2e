import requests
import time


def get_verification_link(email):
    def poll():
        r = requests.get('http://restmail.net/mail/' + email)
        json = r.json()
        if len(json) > 0:
            return r.json()[0]['headers']['x-link']
        else:
            time.sleep(0.5)
            return poll()

    return poll()
