from flask import Flask, request, jsonify, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
from sqlalchemy import func
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException, default_exceptions

#initializing

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


class Message(db.Model):  
  id = db.Column(db.Integer, primary_key=True)
  message = db.Column(db.String(200))
  count = db.Column(db.Integer)

  def __init__(self, id, message, count):
        self.id = id
        self.message = message
        self.count = count
  
#Declaring a marshmallow schema, mapping attributes - see below for info
#https://marshmallow.readthedocs.io/en/stable/quickstart.html#declaring-schemas
class MessageSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'message', 'count')
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)        


class MessageManager(Resource):

    @staticmethod
    def get():
        messages_list = Message.query.all()
        result = messages_schema.dump(messages_list)
        return jsonify(result)
      #  return jsonify({'Message': 'I would really rather you use a POST'})

    @staticmethod
    def post():
        req_data = request.json
        #printing out request for debugging purposes
        print(req_data)
        #set variables from JSON
        #adding error handling for invalid JSON
        try:
            id = request.json['id']
        except KeyError:
            abort(400, "ID is a required key")
        try:
            messageText = request.json['message']
        except KeyError:
            abort(400, "Message is a required key")
        
        
        #logic to count number of whitespace separated words in the message
        countval = len(messageText.split())
        #passes the newly set variables as parameters to the Message DB class
        newmessage = Message(id, messageText, countval)
        db.session.add(newmessage)
        #adding a try except to catch unique constraint violations and return to user
        try:
             db.session.commit()
             totalcount = db.session.query(func.sum(Message.count)).scalar()
             return jsonify({
            'Count': totalcount
             })
        except IntegrityError:
            db.session.rollback()
            return jsonify({
            'Message': 'ID already exists in database.'
             })
            
       
        
  
    @staticmethod
    def put():        
        return jsonify({'Message': 'I would really rather you use a POST'})

    @staticmethod
    def delete():     
        return jsonify('I would rather you not delete anything, the database has been through enough already')    
        
@app.route('/')
def home():
    return render_template("index.html")

api.add_resource(MessageManager, '/api/messages')

if __name__ == "__main__":
  #adding 0.0.0.0 was quick and easy way to access my app while in a docker container but i'm sure there are security implications 
  app.run(debug=True, host='0.0.0.0')
  #dropping entire DB and creating on app run, managing state out of my scope for this challenge
  db.drop_all()
  db.create_all()
