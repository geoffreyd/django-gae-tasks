from appengine_django.models import BaseModel
from google.appengine.ext import db

class Client(BaseModel):
    """docstring for Client"""
    status            = db.StringProperty()
    state             = db.TextProperty()
    name              = db.StringProperty()
    filemakerpro      = db.StringProperty()
    quickbooks        = db.StringProperty()
    skus              = db.TextProperty()
    queue_min_size    = db.IntegerProperty()
    queue_min_entries = db.IntegerProperty()
    tags              = db.StringListProperty()
    
class Person(BaseModel):
    kind               = db.StringProperty('type')
    parent             = db.SelfReferenceProperty()
    children_count     = db.IntegerProperty()
    name               = db.StringProperty()
    email              = db.EmailProperty()
    on_private_network = db.BooleanProperty()
    queue_min_size     = db.IntegerProperty()
    queue_min_entries  = db.IntegerProperty()
    yaml               = db.TextProperty()
    state              = db.TextProperty()
    status             = db.IntegerProperty()
    
class Contact(Person):
    

class Contractor(Person):
    

class Employee(Person):
    

class Manager(Employee):
    
