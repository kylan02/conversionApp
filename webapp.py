from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/dollarToEuro")
def render_page1():
    return render_template('dollar-euro.html')

@app.route("/FeetToMeters")
def render_page2():
    return render_template('feet-meters.html')
    
@app.route("/PoundToKg")
def render_page3():
    return render_template('pound-kg.html')
    
@app.route("/response")
def render_page3():
    return render_template('response.html')
    
if __name__=="__main__":
    app.run(debug=False)
