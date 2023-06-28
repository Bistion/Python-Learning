from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Joe")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)

#sending json data
@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

#how to get data back
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#doing a redirect from the /go-to-home page to our defined home page /
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))