import configparser



def get_slash_app_token():
    config = configparser.ConfigParser()
    config.read('config.ini')
    app_token = config['DEFAULT']['SLASH_APP_TOKEN']
    return app_token

app_token = get_slash_app_token()

from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/me')
def me():
    discord = make_session(token=session.get('oauth2_token'))