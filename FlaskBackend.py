from flask import Flask , request , jsonify



app = Flask(__name__)
menu = {"apple" : 200 , "banana" : 400 , "caramel ice cream" : 1200} 
url = ""

@app.route("/menu")
def ret_menu() :
 return jsonify(menu);


if __name__ == "__main__":
 app.run(port=5050)