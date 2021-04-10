import discord
import requests
import configparser
from flask import Flask

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
app_token = config['DEFAULT']['SLASH_APP_TOKEN']
print(app_token)

client = discord.Client()

@app.route('/', methods=['POST'])
def my_command():
    if request.json["type"] == 1:
        return jsonify({
            "type":1
        })

client.run(app_token)