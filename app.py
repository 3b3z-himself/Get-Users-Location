from flask import Flask, render_template, request
import requests

app = Flask(__name__)

IPINFO_API_KEY = 'YOUR_IPINFO_API_KEY'

def get_user_location(ip):
    url = f"http://ipinfo.io/{ip}?token={IPINFO_API_KEY}"
    response = requests.get(url)
    data = response.json()
    location = {
        'ip': data['ip'],
        'country': data['country'],
        'region': data['region'],
        'city': data['city'],
        'latitude': data['loc'].split(',')[0],
        'longitude': data['loc'].split(',')[1]
    }
    return location

@app.route('/')
def index():
    user_ip = request.remote_addr
    location = get_user_location(user_ip)
    return render_template('index.html', location=location)

if __name__ == '__main__':
    app.run()
