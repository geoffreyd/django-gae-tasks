# actors/models
from appengine_django.models import BaseModel
from google.appengine.ext import db

class Actor(BaseModel):
    agent    = db.ReferenceProperty(Agent) # umm, I don't think I need this. Agent should link back instead? An agent can service more than one actor (though usually it's just the one actor. I think actor's have agents, and not the other way around. IOW An actor only gets one agent, whereas an agent can have multiple actors. So let's store the property here.
    abilities = db.ReferenceProperty(Ability) #hmm, not sure if we can do, has_many through? yeah, probably not. Maybe a custom index though?

class Client(Actor):
    """docstring for Client"""
    state             = db.StringProperty() # a function name
    name              = db.StringProperty()
    queue_min_size    = db.IntegerProperty()
    queue_min_entries = db.IntegerProperty()
    tags              = db.StringListProperty()

# GD: let's go with whatever the standard is being used by Apple and/or Google contacts
class Person(Actor):
    kind               = db.StringProperty('type')
    first_name         = db.StringProperty()
    last_name          = db.StringProperty()
    email              = db.EmailProperty()
    queue_min_length   = db.IntegerProperty() # in seconds...
    queue_min_entries  = db.IntegerProperty()
    state              = db.StringProperty() # a function name
    
class Executable(Actor):
    pass
    
