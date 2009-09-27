from appengine_django.models import BaseModel
from google.appengine.ext import db

class Project(BaseModel):
    name = db.StringProperty()
    time_left = db.FloatProperty()

class Task(BaseModel):
    project = db.ReferenceProperty(Project, collection_name='tasks')
    name = db.StringProperty()
    description = db.TextProperty()
    task_type = db.StringProperty()
    priority = db.StringProperty()
    status_value = db.StringProperty()
    validation = db.StringProperty()
    effort = db.StringProperty()

    submitter = db.UserProperty()
    assignee = db.UserProperty()
