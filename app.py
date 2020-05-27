from flask import Flask, redirect, url_for, render_template, request
from pprint import pprint
import random

#use pprint for debugging.


# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

#configure app

#disable caching:
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# Define routes for the app:

print ("first module name: {}".format(__name__))

# index route supports mmultiple methods:
@app.route("/" , methods=["POST", "GET"])
def home():
    if request.method == "POST":

        if 'image' in request.form:
            return render_template('extra.html')

        searchval = request.form['search']
        return redirect(url_for("search", keyword=searchval))
    else:
        return render_template("index.html")


# Route to search page:
@app.route("/search/<keyword>", methods=["POST", "GET"])
def search(keyword):
    # if using search via search page:
    if request.method == "POST":
        keyword = request.form['search']

    return render_template('search.html', key=keyword)


@app.route("/extra", methods=["POST", "GET"])
def extra():
    if request.method == "POST":
        searchval = request.form['search']
        return redirect(url_for("search", keyword=searchval))

    if(request.args.get("number")):
        nmbr = request.args.get("number")
    else:
        nmbr = 294

    return render_template('extra.html', number=nmbr)


# redirect user when trying to access admin urls:
@app.route('/admin')
def admin():
    return redirect(url_for("home"))



@app.route('/generator')
def generator():
    randomNmbr = random.randint(0, 300)
    return redirect(url_for("extra", number=randomNmbr))

# execute only if app.py is executed as a script:
if __name__ == '__main__':
    app.run(debug=True)

