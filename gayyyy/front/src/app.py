from flask import Flask
import json
import pprint


app = Flask(__name__)
app.debug = True

happy_hour_json = 'json/happyHour.txt'

@app.route('/hello')
def hello():
    return "Hello World!"



@app.route('/gay')
def retrieve_json():
    json_data = open(happy_hour_json).read()
    data = json.loads(json_data)
    return pprint.pprint(data).__str__

if __name__ == '__main__':
    app.run()
