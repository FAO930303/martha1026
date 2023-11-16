import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def index():
	X="作者:郭恣妤2023/11/16a<br>"
	X+="<a href=/mis>資訊管理導論</a><br>"
	X+="<a href=/today>日期時間</a><br>"
	X+="<a href=/about>郭恣妤網頁</a><br>"
	X+="<a href=/welcome?guest=martha>歡迎</a><br><br>"
	X+="<a href=/account>使用表單方式傳值</a><br>"
	X += "<br><a href=/wave>人選知人演員名單</a><br>"

	return X

@app.route("/mis")
def course():
	return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
	now = datetime.now()
	return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("guest")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")
@app.route("/wave")
def wave():
    Result = ""
    db = firestore.client()
    collection_ref = db.collection("人選之人─造浪者")    
    docs = collection_ref.order_by("birth",direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        Result += "演員：{}".format(doc.to_dict()) + "<br>"    
    return Result


if __name__ == "__main__":
	app.run()