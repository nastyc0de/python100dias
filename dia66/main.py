from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dicc = {}
        for column in self.__table__.columns:
            dicc[column.name] = getattr(self, column.name)
        return dicc

db.create_all()

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/random', methods=['GET'])
def random_coffee():
    cafes = Cafe.query.all()
    rand_cofee = choice(cafes)
    cafe = rand_cofee.to_dict()
    return jsonify(cafe)
## HTTP GET - Read Record
@app.route('/all')
def get_all():
    cafes = Cafe.query.all()
    list_coffee = [cafe.to_dict() for cafe in cafes]
    return jsonify(list_coffee)
@app.route('/search')
def searching():
    location = request.args.get('loc')
    cafe =Cafe.query.filter_by(location=location).first()
    if cafe:
        return jsonify(cafe.to_dict())
    else:
        return jsonify(error={'Not found':'No existe esa localizacion'})
## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_coffee():
    cafe= Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={'success':'Agregado correctamente'})

## HTTP PUT/PATCH - Update Record
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    new_price = request.args.get('new')
    cafe = Cafe.query.get_or_404(id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(cafe.to_dict()), 200
    else:    
        return jsonify(error={'error':'cafe no encontrado'}), 404

## HTTP DELETE - Delete Record
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cafe = Cafe.query.get_or_404(id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(ok={'Exito': 'cafe cerrado'}),200
    else:
        return jsonify(ok={'Error': 'no encontrado'})


if __name__ == '__main__':
    app.run(debug=True)
