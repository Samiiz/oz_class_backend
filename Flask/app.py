from flask import Flask, render_template

app = Flask(__name__)

languages = {
    "python" : "파이썬",
    "javascript" : "자바스크립트",
    "html" : "HTML",
    "css" : "CSS",
    "php" : "PHP",
    "sql" : "SQL",
}

@app.route("/")
def index():
    return render_template("languages.html", languages=languages)

@app.route("/number/<id>")
def number(id):
    if int(id)%2  == 0 :
        id = "짝수"
    elif id :
        id = id
    else :
        id = "홀수"
    return render_template("number.html", id=id)




if __name__ == "__main__":
    app.run(debug=True)