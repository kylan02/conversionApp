from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/dollarToEuro")
def render_page1():
	if "amount" in request.args:
		currency_to_convert = request.args['amount']
		response = str((round(100*(float(currency_to_convert)*(0.91)))/100)) + " Euros"
		return render_template('dollar-euro.html', responseFromServer=response)
	else:
		return render_template('dollar-euro.html')

@app.route("/FeetToMeters")
def render_page2():
	if "amount" in request.args:
		currency_to_convert = request.args['amount']
		response = str((round(100*(float(currency_to_convert)*(0.3048)))/100)) + " Meters"
		return render_template('feet-meters.html', responseFromServer=response)
	else:
		return render_template('feet-meters.html')
    
@app.route("/PoundToKg")
def render_page3():
	if "amount" in request.args:
		currency_to_convert = request.args['amount']
		response = str((round(100*(float(currency_to_convert)*(0.453592)))/100)) + " Kg"
		return render_template('pound-kg.html', responseFromServer=response)
	else:
		return render_template('pound-kg.html')
    
@app.route("/response")
def render_page4():
	currency_to_convert = request.args['amount']
	response = str(float(currency_to_convert)*(x)) + " Euros"
	return render_template('response.html', responseFromServer=response)
    
if __name__=="__main__":
    app.run(debug=False)
