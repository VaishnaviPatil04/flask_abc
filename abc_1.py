from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
@app.route('/', methods= ['GET','POST'])
def home_page():
    return render_template("index.html")

@app.route("/")
def hello_world():
    return "<h1>Hello, there!</h1>"

@app.route("/test")
def test():
    a= 5+6
    return "this is my function to run{}".format(a)

# @app.route("/test2/test2")
# def test2():
#     data = request.args.get("x")
#     return "this is a data input from my url {}".format(data)

@app.route("/login")
def login():
     data1 = 45+8
     return "login my page from url {}". format(data1)

if __name__=="__main__":
    app.run(host="0.0.0.0")





