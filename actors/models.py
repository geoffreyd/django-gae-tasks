from appengine_django.models import BaseModel
from google.appengine.ext import db

class Client(BaseModel):
    name = db.StringProperty()
    skus = db.TextProperty()
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()
    quickbooks = db.StringProperty()
    filemakerpro = db.StringProperty()
    
class Person(BaseModel):
    name = db.StringProperty()
    email = db.EmailProperty()
    on_private_network = db.BooleanProperty()
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()
    type = db.StringProperty()
    
class Contact(Person):
    

class Contractor(Person):
    

class Employee(Person):
    

class Manager(Employee):
    

class Vendor(BaseModel):
    name = db.StringProperty()
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()