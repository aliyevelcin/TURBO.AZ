from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mashinlarr.db"
db.init_app(app)
import os
from werkzeug.utils import secure_filename 
UPLOAD_FOLDER ='./static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from sqlalchemy import desc

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(500), nullable=True)
    price = db.Column(db.String(500), nullable = True)
    model = db.Column(db.String(500), nullable = True)
    seher = db.Column(db.String(500), nullable = True)
    buraxilis_ili = db.Column(db.String(500), nullable = True)
    ban_novu = db.Column(db.String(500), nullable = True)
    reng = db.Column(db.String(500), nullable = True)
    muherrik = db.Column(db.String(500), nullable = True)
    yurus = db.Column(db.String(500), nullable = True)
    suretler_qutusu = db.Column(db.String(500), nullable = True)
    oturucu = db.Column(db.String(500), nullable = True)
    yeni = db.Column(db.String(500), nullable = True)
    img = db.Column(db.String(500), nullable = True)

    def __init__(self, marka, price,model, seher ,buraxilis_ili ,ban_novu ,reng ,muherrik , yurus, suretler_qutusu,oturucu ,yeni,img ):
        self.marka = marka
        self.price = price
        self.model = model
        self.seher = seher
        self.buraxilis_ili = buraxilis_ili
        self.ban_novu = ban_novu
        self.reng = reng
        self.muherrik = muherrik
        self.yurus = yurus
        self.suretler_qutusu = suretler_qutusu
        self.oturucu = oturucu
        self.yeni = yeni
        self.img = img

@app.route("/add-car", methods = ['GET', 'POST'])
def addcar():
    if request.method == "GET":
        return render_template('addcar.html')
    else:
        marka = request.form['marka']
        model = request.form['model']
        price = request.form['price']
        seher = request.form['seher']
        buraxilis_ili = request.form['buraxilis_ili']
        ban_novu = request.form['ban_novu']
        reng = request.form['reng']
        muherrik = request.form['muherrik']
        yurus = request.form['yurus']
        suretler_qutusu = request.form['suretler_qutusu']
        oturucu = request.form['oturucu']
        yeni = request.form['yeni']
        img = request.files['img']
        filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        new_text = Car(marka, model,price, seher ,buraxilis_ili ,ban_novu ,reng ,muherrik , yurus, suretler_qutusu,oturucu ,yeni,filename)
        db.session.add(new_text)
        db.session.commit()
        return render_template('addcar.html')

@app.route("/cars")
def cars():
    cars = Car.query.all()
    return render_template('masin.html', cars=cars)

@app.route("/car/<int:id>/")
def car(id):
    car = Car.query.get(id)
    cars = Car.query.order_by(desc(Car.id))[:4] 
    return render_template('turbo_az.html', car=car , cars=cars)

@app.route("/cars2")
def cars2():
    cars2 = Car.query.all()
    return render_template('masin2.html', cars2=cars2)
 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)