from flask import Flask, request

application = Flask(__name__)

def joinNewsletter ( f_name, l_name, email ):
	file = open("maillist.csv", "a")
	concat = f_name+","+l_name+","+email+"\n"
	file.write(concat)
	file.close()	

@application.route("/")
def index():
	return application.send_static_file("index.html")

@application.route("/home", methods=["post"])
def home():
	f_name = request.form['f_name']
	l_name = request.form['l_name']
	email = request.form['email']
	joinNewsletter (f_name,l_name,email)
	return application.send_static_file("index.html")

if __name__ == "__main__":
	application.debug = True
	application.run()