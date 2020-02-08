from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('index.html')

if __name__ == '__main__':
        app.run(debug = True, host = '192.168.3.98')