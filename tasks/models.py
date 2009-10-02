from appengine_django.models import BaseModel
from google.appengine.ext import db

class Project(BaseModel):
    name = db.StringProperty()
    client = db.ReferenceProperty(Client)
    yaml = db.TextProperty()
    status = db.IntegerProperty()
    state = db.TextProperty()
    time_left = db.FloatProperty()

class ProjectWithOrders(BaseModel):
    project       = db.ReferenceProperty(Project)
    work_order    = db.ReferenceProperty(WorkOrder)
    yaml          = db.TextProperty()
    state         = db.TextProperty()
    status        = db.IntegerProperty()

class Task(BaseModel):
    name = db.StringProperty()
    description = db.TextProperty()
    notes = db.TextProperty()
    created_on = db.DateTimeProperty(auto_now_add=True) # should be DateTime?
    started_on = db.DateTimeProperty()
    finished_on = db.DateTimeProperty()
    actualized_time = db.FloatProperty()
    element_type = db.StringProperty()
    client_name = db.StringProperty()
    project_name = db.StringProperty()
    task_accounting_category = db.IntegerProperty() # should be ReferenceProperty?
    position = db.IntegerProperty()
    children_count = db.IntegerProperty()
    parent = db.SelfReferenceProperty()
    element = db.ReferenceProperty(Element) # Not sure about this
    last_task_assignment = db.ReferenceProperty(Assignment) # Can't find Assingment Model
    last_time_sheet = db.ReferenceProperty(TimeSheet)
    estimated_time = db.IntegerProperty()
    template = db.BooleanProperty()
    proto = db.SelfReferenceProperty()
    task_page = db.StringProperty()
    yaml = db.TextProperty()
    uses_task_logs = db.BooleanProperty()
    state = db.TextProperty()
    task_status = db.IntegerProperty()
    estimated_time_input = db.StringProperty()
    created_by = db.ReferenceProperty(User) # probably Auth.User or something
    type = db.StringProperty()
    # project = db.ReferenceProperty(Project, collection_name='tasks')
    # task_type = db.StringProperty()
    # priority = db.StringProperty()
    # status_value = db.StringProperty()
    # validation = db.StringProperty()
    # effort = db.StringProperty()
    # 
    # submitter = db.UserProperty()
    # assignee = db.UserProperty()

class AliasTask(Task):
    
class AutoTask(Task):
    
class CollectTask(Task):
    person = db.ReferenceProperty(User)
    
class EmailTask(Task):
    
class ExecutableTask(Task):
    
class HumanTask(Task):
    
class MachineTask(Task):
    
class MeetingTask(Task):
    
class Workflow(Task):

    
class WorkflowObserver(BaseModel):
    workflow = db.ReferenceProperty(Workflow)
    task = db.ReferenceProperty(Task)
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()
    
class TaskAssignment(BaseModel):
    actor            = db.ReferenceProperty(Actor)
    task             = db.ReferenceProperty(Task)
    yaml             = db.TextProperty()
    creator          = db.ReferenceProperty(User)
    state            = db.TextProperty()
    work_order       = db.ReferenceProperty(WorkOrder)
    current_task_log = db.ReferenceProperty(TaskLog)
    issued_on        = db.DateTimeProperty()
    issuer_id        = db.ReferenceProperty(User) #not sure
    issuer_type      = db.StringProperty()
    created_on       = db.DateTimeProperty()
    creator_type     = db.StringProperty()
    type             = db.StringProperty()
    actor_type       = db.StringProperty()
    resource         = db.ReferenceProperty(Resource)
    action           = db.ReferenceProperty(Action)
    resource_type    = db.StringProperty()

class TaskLogs(BaseModel):
    started_on      = db.DateTimeProperty()
    finished_on     = db.DateTimeProperty()
    actualized_time = db.FloatProperty()
    state           = db.TextProperty()
    task_assignment = db.ReferenceProperty(TaskAssignment)
    explanation     = db.TextProperty()
    notes           = db.TextProperty()
    yaml            = db.TextProperty()

class TaskQueue(BaseModel):
    actor        = db.ReferenceProperty(Actor)
    actor_type   = db.StringProperty()
    position     = db.IntegerProperty()
    queued_on    = db.DateTimeProperty()
    issued_on    = db.DateTimeProperty()
    delivered_on = db.DateTimeProperty()
    queuer       = db.ReferenceProperty(User) #not sure
    queuer_type  = db.StringProperty()
    issuer       = db.ReferenceProperty(User) #not sure
    issuer_type  = db.StringProperty()
    yaml         = db.TextProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

class TaskRequirement(BaseModel):
    task        = db.ReferenceProperty(Task)
    requirement = db.ReferenceProperty(Requirement)
    yaml        = db.TextProperty()
    state       = db.TextProperty()
    status      = db.IntegerProperty()
