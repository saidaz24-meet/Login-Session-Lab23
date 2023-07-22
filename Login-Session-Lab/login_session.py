from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/',methods=['GET', 'POST'] ) # What methods are needed?
def home():
	try :
		if request.method == 'POST':
			age = request.form["author's age"]
			login_session['age'] = age
			name = request.form["quoteName"]
			login_session['name'] = name
			author = request.form["quote's author"]
			login_session['author'] = author
			return render_template("display.html",age = age,name = name,author = author)
		return render_template("home.html")
	except :
		return redirect(url_for('error'))		
		


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html') # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)