from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
@app.route('/main.html')

def index():
        return render_template('main.html', title = 'Vega - Login')

if __name__ == '__main__':
        app.run(debug = True, host = '192.168.3.98')