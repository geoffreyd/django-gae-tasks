# other/models.py
from appengine_django.models import BaseModel
from google.appengine.ext import db

# NOTE: the "json" property is not needed throughout (this was a limitation of the older system)

class Ability(BaseModel):
    actor   = db.ReferenceProperty(Actor, collection_name='abilities')
    role    = db.ReferenceProperty(Role, collection_name='abilities')
    state   = db.TextProperty()
    status  = db.IntegerProperty()
    tags    = db.StringListProperty() # this is cool BTW

class Access(BaseModel):
    status        = db.IntegerProperty()
    resource      = db.ReferenceProperty(Resource)
    resource_type = db.StringProperty()
    role          = db.ReferenceProperty(Role)
    tags          = db.StringProperty()

# do we need to have an account model? will this be taken care of by Google Accounts/Django users?
# class Account(BaseModel):
#     status
#     login
#     email
#     crypted_password

class Agent(BaseModel):
    actor          = db.ReferenceProperty(Actor)
    tags           = db.StringListProperty()
    preference     = db.TextProperty() # stores JavaScript/JSON
    a              = db.BooleanProperty() # what is 'a'?
    business       = db.ReferenceProperty(Business) # Actor.kind = Business
    # has many Abilities
    # has many Positions
    # has many Departments through Positions

class AssetDeliverable(BaseModel):
    status      = db.StringProperty()
    asset       = db.ReferenceProperty(Asset)
    deliverable = db.ReferenceProperty(Deliverable)
    tags        = db.StringListProperty()

class Asset(BaseModel):
    location = db.StringProperty()
    note = db.TextProperty()
    kind = db.StringProperty('type')
    freebie = db.BooleanProperty()
    accounting_code = db.StringProperty()
    filemakerpro = db.StringProperty()
    format = db.IntegerProperty()
    value = db.FloatProperty() # should be Decimal Not sure how GAE handles this.
    scale = db.FloatProperty() # should be Decimal
    path = db.StringProperty()
    name = db.StringProperty()
    parent = db.SelfReferenceProperty()
    client = db.ReferenceProperty(Client)
    state = db.TextProperty()
    status = db.IntegerProperty()
    children_count = db.IntegerProperty()

class Assingment(BaseModel):
    kind             = db.StringProperty()
    status           = db.IntegerProperty()
    created_on       = db.DateTimeProperty()
    action           = db.ReferenceProperty(Action)
    resource         = db.ReferenceProperty(Resource)
    resource_type    = db.StringProperty()
    role             = db.ReferenceProperty(Role)
    grantor          = db.ReferenceProperty(User) #not sure
    grantor_type     = db.StringProperty()
    security_context = db.ReferenceProperty(SecurityContext)
    notes            = db.TextProperty()
    tags             = db.StringListProperty()

class Authorization(BaseModel):
    kind = db.StringProperty('type')
    event = db.ReferenceProperty(Event)
    security_context = db.ReferenceProperty(SecurityContext) # ??
    json = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()

class BillableRate(BaseModel):
    status        = db.IntegerProperty()
    rate          = db.IntegerProperty() # should be Decimal
    created_on    = db.DateTimeProperty()
    billable_id   = db.ReferenceProperty(BaseModel) # or string?
    billable_type = db.StringProperty()
    role          = db.ReferenceProperty(Role)
    tags          = db.StringListProperty()

class BillableRole(BaseModel):
    status        = db.IntegerProperty()
    quickbooks    = db.TextProperty()
    created_on    = db.DateTimeProperty()
    billable_id   = db.StringProperty() # model name
    billable_type = db.StringProperty()
    creator       = db.ReferenceProperty(User)
    role          = db.IntegerProperty()
    tags          = db.StringListProperty()

class Billing(BaseModel):
    """docstring for Billing"""
    status        = db.IntegerProperty()
    rate          = db.IntegerProperty() #should be Decimal
    created_on    = db.DateTimeProperty()
    billable      = db.ReferenceProperty(BaseModel) # or String?
    billable_type = db.StringProperty()
    creator       = db.ReferenceProperty(Actor)
    creator_type  = db.StringProperty()
    role          = db.ReferenceProperty(Role)
    tags          = db.StringListProperty()

class BuildDeliverable(BaseModel):
    """docstring for BuildDeliverable"""
    status       = db.IntegerProperty()
    build        = db.StringProperty()
    build_type   = db.StringProperty()
    deliverable  = db.ReferenceProperty(Deliverable)
    tags         = db.StringListProperty()

class Deliverable(BaseModel):
    name = db.StringProperty()
    due_date = db.DateTimeProperty()
    kind = db.StringProperty('type')
    json = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()
    project = db.ReferenceProperty(Project)
    notes = db.TextProperty()
    tages = db.StringListProperty()

class Departments(BaseModel):
    """ ... """
    status = db.IntegerProperty()
    name   = db.StringProperty()
    tags   = db.StringListProperty()

class ElementAsset(BaseModel):
    status       = db.StringProperty()
    asset        = db.ReferenceProperty(Asset)
    element_key  = db.StringProperty()
    element_type = db.StringProperty()
    tags         = db.StringListProperty()

class EntryMapping(BaseModel):
    """ ... """
    kind            = db.StringProperty('type')
    position        = db.IntegerProperty()
    source_position = db.IntegerProperty()
    entry_type      = db.StringProperty()
    task            = db.ReferenceProperty(Task)
    tags            = db.StringListProperty()

class EventAuthorization(BaseModel):
    """ ... """
    status        = db.IntegerProperty()
    event         = db.ReferenceProperty(Event)
    authorization = db.ReferenceProperty(Authorization)
    tags          = db.StringListProperty()

class Event(BaseModel):
    created_on      = db.DateTimeProperty()
    action          = db.ReferenceProperty(Action)
    actor_key       = db.StringProperty()
    actor_type      = db.StringProperty()
    name            = db.StringProperty()
    securable       = db.ReferenceProperty(Secure) 
    securable_type  = db.StringProperty()
    securable_state = db.TextProperty()
    task            = db.ReferenceProperty(Task)

class Executable(BaseModel):
    """ ... """
    kind              = db.StringProperty('type')
    name              = db.StringProperty()
    status            = db.IntegerProperty()
    host              = db.StringProperty()
    login             = db.StringProperty()
    password          = db.StringProperty()
    path              = db.StringProperty()
    queue_min_size    = db.IntegerProperty()
    queue_min_entries = db.IntegerProperty()
    tags              = db.StringListProperty()

class Issue(BaseModel):
    """ ... """
    kind         = db.StringProperty('type')
    status       = db.IntegerProperty()
    short_name   = db.StringProperty()
    name         = db.StringProperty()
    severity     = db.IntegerProperty()
    created_on   = db.DateTimeProperty()
    creator_key  = db.StringProperty()
    creator_type = db.StringProperty()
    element_key  = db.StringProperty()
    element_type = db.StringProperty()
    analysis     = db.TextProperty()
    tags         = db.StringListProperty()

# Since Google has reliable email delivery, we don't need all of the mail-related classes. I used to have
# a script that parsed the DB transaction logs and made qmail do it's thing. Qmail would report status updates back to the DB.
#class MailRecipient(BaseModel):
#    """ ... """
#    kind           = db.StringProperty('type')
#    status         = db.IntegerProperty()
#    pending_mail   = db.ReferenceProperty(PendingMail)
#    recipient_key  = db.StringProperty()
#    recipient_type = db.StringProperty()
#    tags           = db.StringListProperty()
#
#class PendingMail(BaseModel):
#    """ ... """
#    kind              = db.StringProperty('type')
#    status            = db.IntegerProperty()
#    error_code        = db.IntegerProperty()
#    error_message     = db.StringProperty()
#    error_type        = db.IntegerProperty()
#    mailer_template   = db.StringProperty()
#    mailer_type       = db.StringProperty()
#    qmail_queue_inode = db.IntegerProperty()
#    mailable_key      = db.StringProperty()
#    mailable_type     = db.StringProperty()
#    sender_key        = db.StringProperty()
#    sender_type       = db.StringProperty()
#    tags              = db.StringListProperty()

# these can be delayed...
#class PurchaseOrderApplication(BaseModel):
#    purchase_order    = db.ReferenceProperty(PurchaseOrder)
#    work_order        = db.ReferenceProperty(WorkOrder)
#    state             = db.TextProperty()
#    status            = db.IntegerProperty()
#
#class PurchaseOrders(BaseModel):
#    filemakerpro = db.StringProperty()
#    quickbooks   = db.StringProperty()
#    client_id    = db.IntegerProperty()
#    json         = db.TextProperty()
#    state        = db.TextProperty()
#    status       = db.IntegerProperty()

# class Receive(BaseModel):
#     json = db.TextProperty()

class Requirement(BaseModel):
    name   = db.StringProperty()
    json   = db.TextProperty()
    state  = db.TextProperty()
    status = db.IntegerProperty()
    kind   = db.StringProperty('type')

class Resource(BaseModel):
    kind         = db.StringProperty('type')
    name         = db.StringProperty()
    filemakerpro = db.StringProperty()
    quickbooks   = db.StringProperty()
    location     = db.StringProperty()
    amount       = db.IntegerProperty() #should be Decimal do this in cents, e.g. 100 = $1
    json         = db.TextProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

# clearly this needs to be flushed out much more... Done.
class Role(BaseModel):
    """
    Represents a user role and any associated metadata.
    
    """
    parent      = db.SelfReferenceProperty()
    position    = db.IntegerProperty()
    status      = db.IntegerProperty()
    name        = db.StringProperty()
    tags        = db.StringListProperty()
    state       = db.TextProperty()
    # has_many: abilities
    # has_many :actors, :through => :abilities
    # has_many :credentials
    # has_many :actions, :through => :credentials

has_many :constraints
has_many :rules, :through => :constraints

# this is probably not necessary anymore, now that RBAC is in place
class SecurityContext(BaseModel):
    """
    Represents <fill in here, please>
    
    """
    status          = db.IntegerProperty()
    json            = db.TextProperty()
    state           = db.TextProperty()
    position        = db.IntegerProperty()
    children_count  = db.IntegerProperty()
    parent          = db.SelfReferenceProperty()
#    securable      = db.ReferenceProperty(Secure) # not sure
    securable_key   = db.StringProperty()
    securable_model = db.StringProperty()

# class Send(BaseModel):
#     json = db.TextProperty()

# this class is an odd duck. let's leave it out for now.
# class TimeSheet(BaseModel):
#     """
#     Represents a user's time sheet for a task
#     
#     """
#     task                = db.ReferenceProperty(Task)
#     person              = db.ReferenceProperty(Person)
#     time_sheet_entry    = db.IntegerProperty()
#     created_on          = db.DateTimeProperty()
#     json                = db.TextProperty()

# class Transfer(BaseModel):
#     asset    = db.ReferenceProperty(Asset)
#     shipment = db.ReferenceProperty(Shipment)
#     json     = db.TextProperty()
#     state    = db.TextProperty()
#     status   = db.IntegerProperty()

class Vendor(BaseModel):
    name = db.StringProperty()
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()