from flask import Flask, render_template, request,make_response
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    secret_number= request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))
    if not secret_number:
        secret_number=random.randint(1,5)
        response.set_cookie("secret_number",str(secret_number))

    return response

@app.route("/result", methods=["POST"])
def result():
    secret_number= int(request.cookies.get("secret_number"))
    guess_number = int( request.form.get("guess"))
    if secret_number== guess_number:
        message = "Congratulations! you guessed it!"
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number",str(random.randint(1,5)))
        return response

    elif guess_number>secret_number:
        message="Try something smaller"
        return render_template("result.html", message=message)
    else:
        message="Try something bigger"
        return render_template("result.html",message=message )

if __name__ == '__main__':
    app.run(port="5001")