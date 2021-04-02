import mbta_helper 
from flask import Flask
from flask import request
# from mbta_helper import find_stop_near
from flask import render_template

app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def get_nearest_stop():
    if request.method == "POST":
        place_name = request.form['address']
        result = mbta_helper.find_stop_near(place_name)
        if result != "Error":
            return render_template('station.html', result=result)
        else:
            return render_template("error.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
