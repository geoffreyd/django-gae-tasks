# tasks/models
from appengine_django.models import BaseModel
from google.appengine.ext import db

class Action(BaseModel):
    kind       = db.StringProperty('type')
    status     = db.StringProperty()
    short_name = db.IntegerProperty() # integer? maybe code?
    name       = db.StringProperty()
    controller = db.StringProperty()
    action     = db.StringProperty()
    tags       = db.TextProperty()
    state      = db.TextProperty()
    action     = db.StringProperty()
    # has many Credentials

class Credential(BaseModel):
    role   = db.ReferenceProperty(Role)
    action = db.ReferenceProperty(Action)
    # has many Constraints
    # has many rules through constraints

# In the App Engine sense, a Task should act as a "root" and all of the task assignments should have the task as their "parent", and
# task logs should have their task assignment as their "parent". This will effectively mean that a task and all of its task assignments and their
# task logs form a transactional unit. For tasks that are part of a workflow, the top-most workflow would be the "root" object and the subtasks and
# subworkflows would list it as parent, recursively.
#
# Using this approach should allow us to do the rollups (denormalization) correctly (and safely). There's a report against a project that
# uses those rollups, and without the denormalization/rollups, it runs at a glacial pace, but it's a critical report used by managers so
# we have to support it. (Taavi, this is mostly for you.)

class Project(BaseModel):
    name      = db.StringProperty()
    client    = db.ReferenceProperty(Client)
    yaml      = db.TextProperty()
    status    = db.IntegerProperty()
    state     = db.TextProperty()
    time_left = db.FloatProperty()

class ProjectWithOrders(BaseModel):
    project    = db.ReferenceProperty(Project)
    work_order = db.ReferenceProperty(WorkOrder)
    yaml       = db.TextProperty()
    state      = db.TextProperty()
    status     = db.IntegerProperty()

class ActiveTask(BaseModel):
    status          = db.TextProperty()
    actor           = db.ReferenceProperty(Actor)
    task_assignment = db.ReferenceProperty(TaskAssignment)
    tags            = db.StringListProperty()
    state           = db.TextProperty()
    element         = db.ReferenceProperty(Element)
    project         = db.ReferenceProperty(Project)
    client          = db.ReferenceProperty(Client)

class Task(BaseModel):
    # has many TaskDecorators
    # has many Requirements through TaskRequirements
    # has one TaskAssignment
    # has one SecuritySession
    # has many Events
    name                     = db.StringProperty()
    description              = db.TextProperty()
    notes                    = db.TextProperty()
    created_on               = db.DateTimeProperty(auto_now_add=True)
    
    # these two properties are denormalised; the canonical value is in the task logs attached to the task
    # assignments assigned to this task
    started_on               = db.DateTimeProperty()
    finished_on              = db.DateTimeProperty()
    
    # this property should default to None; it's derived from started_on and finished_on until changed
    # (overriden) by the user
    actualized_time          = db.FloatProperty(default=null) #is python nil or null?
    
    # this is somewhat outdated; the mechanism we're moving to was never implemented, but involves
    # type matching against the top of the "stack". Initially, I'd like to see one kind of type matching,
    # with a regex qualifier
    element_type             = db.StringProperty()
    element_qualifier        = db.StringProperty(default='') # should default to '' (No qualifier, meaning "exactly once")
    
    # used for list positioning
    position                 = db.IntegerProperty()
    
    children_count           = db.IntegerProperty() # this was a denormalization, may not be necessary any longer
    
    # Obivously, this naming won't work on app engine. How about "workflow"?
    parent                   = db.SelfReferenceProperty()
    
    # next two properties were denormalized; let's eliminate for now
    # last_task_assignment     = db.ReferenceProperty(TaskAssignment) # Can't find Assingment Model
    # last_time_sheet          = db.ReferenceProperty(TimeSheet)
    
    estimated_time           = db.IntegerProperty()
    template                 = db.BooleanProperty() # I have no idea what this is...
    proto                    = db.SelfReferenceProperty()
    task_page                = db.StringProperty() # this is pretty critical -- it's the SC "page" that should be loaded. Perhaps we should call it "bundle"?
    
    # another denormalization
    uses_task_logs           = db.BooleanProperty()
    
    # this is the state (really, a function name) to put the task into once it's been loaded from the DB
    state                    = db.StringProperty()
    
    # this is fully derived from state, and no longer necessary
    #task_status              = db.IntegerProperty()
    
    # this is initially None, and should reflect "estimated_time" until the user sets it to something else
    estimated_time_input     = db.StringProperty()
    created_by               = db.ReferenceProperty(User) # probably Auth.User or something
    
    # this is for subclassing (a Rails requirement); how is this done on App Engine? Taavi?
    kind                     = db.StringProperty('type')
    
    # Tells SC that this is a 'template' task.
    is_prototype             = db.BooleanProperty()
    
    # Tells SC that this should have children. Might we be able to use types exclusively for this? Yes.
    is_workflow              = db.BooleanProperty()
    # project = db.ReferenceProperty(Project, collection_name='tasks')
    # task_type = db.StringProperty()
    # priority = db.StringProperty()
    # status_value = db.StringProperty()
    # validation = db.StringProperty()
    # effort = db.StringProperty()
    # 
    # submitter = db.UserProperty()
    # assignee = db.UserProperty()

# this is a denormalization; we do lots of reports based on "active" work, which was shuttled into
# and out of this table. It might be best to eliminate it for now, assuming App Engine is fast enough, which
# it should be if we create the correct index for this.
#class ActiveTask(BaseModel):
#    status          = db.StringProperty()
#    actor           = db.ReferenceProperty(Actor)
#    actor_type      = db.StringProperty()
#    task_assignment = db.ReferenceProperty(TaskAssignment)
#    tags            = db.TextProperty()

# Do we need these on the server? ... maybe in SC, not sure.
# Good question, I'm not sure either. They're really just used for tagging, e.g. auto-tasks are handled differently for time sheets.
# so we should just beable to use the 'kind' field? Yes, in the sense that all OO programming is just a glorified 'kind' field. In this case, I doubt it hurts and we can refactor to true types later if we feel that's needed.
#yup, plus we can do that in SC anyway right
#class AliasTask(Task):
#    
#class AutoTask(Task):
#    
#class CollectTask(Task):
#    person = db.ReferenceProperty(User)
#    
#class EmailTask(Task):
#    
#class ExecutableTask(Task):
#    
#class HumanTask(Task):
#    
#class MachineTask(Task):
#    
#class MeetingTask(Task):
#    
#class Workflow(Task):
#
    
class WorkflowObserver(BaseModel):
    workflow = db.ReferenceProperty(Workflow)
    task     = db.ReferenceProperty(Task)
    state    = db.TextProperty()
    status   = db.IntegerProperty()
    
class TaskAssignment(BaseModel):
    actor            = db.ReferenceProperty(Actor)
    task             = db.ReferenceProperty(Task)
    creator          = db.ReferenceProperty(User)
    state            = db.StringProperty()
    work_order       = db.ReferenceProperty(WorkOrder)
    
    # another denormalization (may be worth keeping, hard to say...)
    current_task_log = db.ReferenceProperty(TaskLog)
    issued_on        = db.DateTimeProperty()
    issuer           = db.ReferenceProperty(Actor)
    issuer_type      = db.StringProperty() # this is a Rails holdover
    created_on       = db.DateTimeProperty()
    creator_type     = db.StringProperty() # another Rails holdover
    type             = db.StringProperty() # another Rails.sim
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

# this is actually a queue of task assignments, not tasks
class TaskAssignmentQueue(BaseModel):
    actor        = db.ReferenceProperty(Actor)
    actor_type   = db.StringProperty() # a rails-ism
    position     = db.IntegerProperty()
    queued_on    = db.DateTimeProperty()
    issued_on    = db.DateTimeProperty()
    delivered_on = db.DateTimeProperty()
    queuer       = db.ReferenceProperty(User) #not sure
    queuer_type  = db.StringProperty()
    issuer       = db.ReferenceProperty(User) #not sure
    issuer_type  = db.StringProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

# this is mainly important to the scheduler, which we won't have for awhile
class TaskRequirement(BaseModel):
    task        = db.ReferenceProperty(Task)
    requirement = db.ReferenceProperty(Requirement)
    state       = db.TextProperty()
    status      = db.IntegerProperty()

class WaitingTask(BaseModel):
    status     = db.IntegerProperty()
    created_on = db.DateTimeProperty()
    actor      = db.ReferenceProperty(Actor)
    task       = db.ReferenceProperty(Task)
    tags       = db.StringListProperty()
    state      = db.TextProperty()