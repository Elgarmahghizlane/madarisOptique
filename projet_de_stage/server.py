from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
# configuration de SQLAlchemy
#acceder au chemin vers la base de donnees et on stock dans store.db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db" 

#creer une instance dans notre base de donnees
db= SQLAlchemy(app)

# decorateur importer la page et retourne la page home.html
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/localisation")
def localisation():
    return  render_template("localisation.html")

@app.route("/LVF")
def LVF():
    return  render_template("LVF.html")
@app.route("/LVH")
def LVH():
    return  render_template("LVH.html")
@app.route("/LSF")
def LSF():
    return  render_template("LSF.html")
@app.route("/LSH")
def LSH():
    return  render_template("LSH.html")
 
class Shop(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(70),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    phone=db.Column(db.String(20),nullable=False)
    product=db.Column(db.String(120),nullable=False)
    messagee=db.Column(db.String(120),nullable=False)


@app.route("/contact", methods=["Get","POST"])
def contact():
    s=Shop.query.all()
    L=[]
    for e in s:
        L.append(e.email)
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        product = request.form.get("product")
        messagee=request.form.get("messagee")
        if email in L:
            return "ce e-mail est déja existe" 
        v=Shop(name=name,email=email,phone=phone,product=product,messagee=messagee)
        db.session.add(v)
        db.session.commit()
    return render_template("contact.html")

@app.route("/message")
def message():
    msg=Shop.query.all()
    return render_template("message.html",msg=msg)
if __name__=="__main__":
    app.run(debug=True)