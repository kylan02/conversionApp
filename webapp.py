from flask import Flask, url_for, render_template, request

app = Flask(__name__)

x = 0

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/dollarToEuro")
def render_page1():
	x = 0.91
	return render_template('dollar-euro.html')

@app.route("/FeetToMeters")
def render_page2():
	x = 0.3048
	return render_template('feet-meters.html')
    
@app.route("/PoundToKg")
def render_page3():
	x = 0.453592
	return render_template('pound-kg.html')
    
@app.route("/response")
def render_page4():
	currency_to_convert = request.args['amount']
	response = str(float(currency_to_convert)*(x)) + " Euros"
	return render_template('response.html', responseFromServer=response)
    
if __name__=="__main__":
    app.run(debug=False)
