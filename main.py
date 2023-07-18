from flask import Flask, render_template, request
import requests

app = Flask(__name__)

IPSTACK_API_KEY = '26aa65a0692209cba4f5faf9c731ac35'

def get_user_location(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={IPSTACK_API_KEY}"
    response = requests.get(url)
    data = response.json()
    location = {
        'ip': data['ip'],
        'country': data['country_name'],
        'region': data['region_name'],
        'city': data['city'],
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return location

@app.route('/')
def index():
    user_ip = request.remote_addr
    location = get_user_location(user_ip)
    return render_template('index.html', location=location)

if __name__ == '__main__':
    app.run()
