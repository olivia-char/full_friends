from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector 
app = Flask(__name__)
mysql = MySQLConnector(app, "full_friends")

@app.route("/")
def index():
	friends = mysql.query_db("SELECT * FROM users")
	return render_template("index.html", all_friends=friends)

@app.route("/friends", methods=["POST"])
def friends():
	query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
	data = {
		"first_name": request.form["first_name"],
		"last_name": request.form["last_name"],
		"email": request.form["email"], 
	}

	newfriend = mysql.query_db(query, data)
	print "friends has been passed"
	return redirect("/") 

@app.route("/friends/<id>/edit", methods=["POST"])
def edit(id):
	return render_template("friends.html")

@app.route("/friends/<id>", methods=["POST"])
def update(id):
	query = "UPDATE users SET (id, first_name, last_name, email, created_at, updated_at) VALUES (:id, :first_name, :last_name, :email, NOW(), NOW())"
	data = {
		"id": request.form["id"],
		"first_name": request.form["first_name"],
		"last_name": request.form["last_name"],
		"email": request.form["email"], 
	}

	return redirect("/")

@app.route("/friends/<id>/delete", methods=["POST"])
def delete(id):

	query = "DELETE FROM users WHERE id =" + request.form["id"]
	
	mysql.query_db(query)
	print "deleted"
	return redirect("/")

app.run(debug=True)