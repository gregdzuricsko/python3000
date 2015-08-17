from flask import Flask
from flask import render_template
from gayBarScrape import GayBarScrape


app = Flask(__name__)
app.debug = True

@app.route('/hello')
def hello():
    gbs = GayBarScrape()
    gbs.run()
    return "Hello World!"



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
