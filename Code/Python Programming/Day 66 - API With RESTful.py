from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


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


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def random():
    result = choice(db.session.execute(db.select(Cafe)).scalars().all())
    result_dictionary = {item.name:getattr(result, item.name) for item in result.__table__.c}
    return jsonify(result_dictionary)


@app.route('/all')
def all():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    result_list = []
    for i in result:
        result_dictionary = {item.name:getattr(i, item.name) for item in i.__table__.c}
        result_list.append(result_dictionary)
    return jsonify(cafes=result_list)


@app.route('/search')
def search():
    loc = request.args.get('loc', type=str)
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    result_list = []
    for i in result:
        result_dictionary = {item.name:getattr(i, item.name) for item in i.__table__.c}
        result_list.append(result_dictionary)
    if len(result_list) != 0:
        return jsonify(cafes=result_list)
    else:
        return jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe at that location.'})


## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    data = request.form
    db.session.add(
        Cafe(
            name=data['name'],
            map_url=data['map_url'],
            img_url=data['img_url'],
            location=data['location'],
            seats=data['seats'],
            has_toilet=bool(data['has_toilet']),
            has_wifi=bool(data['has_wifi']),
            has_sockets=bool(data['has_sockets']),
            can_take_calls=bool(data['can_take_calls']),
            coffee_price=data['coffee_price'], 
            ))
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe'})


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<id>', methods=['PATCH'])
def change(id):
    try:
        update = db.get_or_404(Cafe, id)
        price = request.args.get('new_price')
        update.coffee_price = price
        db.session.commit()
    except:
        return jsonify(error={'Not Found': 'Sorry, a cafe with id was not found in database.'}), 404
    else:
        return jsonify(response={'success': 'Successfully changed the coffee price'}), 200


## HTTP DELETE - Delete Record
@app.route('/cafe-closed/<id>', methods=['DELETE'])
def closed(id):
    try:
        delete = db.get_or_404(Cafe, id)
    except:
        return jsonify(error={'Not Found': 'Sorry, a cafe with id was not found in database.'}), 404
    else:
        if request.args.get('api-key') == 'TopSecretAPIKey':
            db.session.delete(delete)
            db.session.commit()
            return jsonify(response={'success': 'Entry deleted'}), 200
        else:
            print('yes')
            return jsonify(error='Sorry that not allowed, make sure you have the correct API Key.'), 403
        

    
if __name__ == '__main__':
    app.run(debug=True)
