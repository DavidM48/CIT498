from flask import Flask, redirect, render_template, request, session, abort, url_for
from werkzeug.security import generate_password_hash, check_password_hash

import json
import urllib.request

import postgresConnect as db
#splitpw = hashpw.split("$")
#dbc.insertUser(username, splitpw[2], splitpw[1])

app = Flask(__name__)

RECAPTCHA_PUBLIC_KEY = '6Lei7vEUAAAAADJke2_q0IlLa5XVj2Aa8pI2zIpH'
RECAPTCHA_PRIVATE_KEY = '6Lei7vEUAAAAAPNzvZSviN0sO2Jo7AYOpVXJAX_z'

@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	if request.method == 'POST' and len(request.form) > 0:
		response = request.form.get('g-recaptcha-response')

		if checkRecaptcha(response, RECAPTCHA_PRIVATE_KEY):
			username = request.form['username']
			password = request.form['password']
			if ((len(username) > 0) and (len(password) > 0)):
				dbc = db.dbconnect()

				hashpw = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
				user = dbc.getUserFromDB(username)

				if (user != None and len(user) == 1):
					hashpwDB = "pbkdf2:sha256:150000${}${}".format(user[0][2],user[0][1])
					if check_password_hash(hashpwDB, password):
						#return render_template('main.html', title = 'Vega - Main')
						return redirect(url_for('main'))
				error = 'Invalid Credentials. Please try again.'
			else:
				error = 'Username or password cannot be empty.'			
		else:
			error = 'reCAPTCHA is failed to validate.'	
	else: 
		return render_template('index.html', title = 'Vega - Login')
		
	if error != None:
		return render_template('index.html', title = 'Vega - Login', error = error)

@app.route('/main')
def main():
	return render_template('main.html', title = 'Vega - Main')

@app.route('/demo')
def demo():
	return render_template('slide.html', title = 'Vega - Demo')

#https://gist.github.com/sameerkumar18/36ee1ee98ae60eb32bffb1b4fc77bbae
def checkRecaptcha(response, secretkey):
	url = 'https://www.google.com/recaptcha/api/siteverify?'
	url = url + 'secret=' + str(secretkey)
	url = url + '&response=' +str(response)

	jsonobj = json.loads(urllib.request.urlopen(url).read())
	return jsonobj['success']

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')