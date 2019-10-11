from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/dollar-euro")
def render_page1():
    return render_template('dollar-euro.html')

@app.route("/feet-meters")
def render_page2():
    return render_template('feet-meters.html')
    
@app.route("/pound-kg")
def render_page3():
    return render_template('pound-kg.html')
    
if __name__=="__main__":
    app.run(debug=False)
