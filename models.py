from appengine_django.models import BaseModel
from google.appengine.ext import db

class Ability(BaseModel):
    actor = db.ReferenceProperty(Actor, collection_name='abilities')
    role = db.ReferenceProperty(Role, collection_name='abilities')
    json = db.StringProperty()
    actor_type = db.StringProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()

class Access(BaseModel):
    status        = db.IntegerProperty()
    resource      = db.ReferenceProperty(Resource)
    resource_type = db.StringProperty()
    role          = db.ReferenceProperty(Role)
    tags          = db.StringProperty()

class User(BaseModel):
    username                    = db.StringProperty()
    first_name                  = db.StringProperty()
    last_name                   = db.StringProperty()
    email                       = db.StringProperty()

    # Stored as '[algo]$[salt]$[hexdigest]'
    password                    = db.StringProperty()
    is_staff                    = db.BooleanProperty()
    is_active                   = db.BooleanProperty()
    is_superuser                = db.BooleanProperty()

    last_login                  = db.DateTimeProperty()
    date_joined                 = db.DateTimeProperty(auto_add=True)
    last_updated                = db.DateTimeProperty(auto_add_now=True)

    tags                        = db.StringListProperty()

#    kind                        = db.StringProperty()
#    status                      = db.IntegerProperty()
#    salt                        = db.StringProperty()
#    created_at                  = db.DateTimeProperty()
#    updated_at                  = db.DateTimeProperty()

# We can use signed cookies for this, storing both the user's key, 
# and the token expiration date, plus a signature.
#    remember_token              = db.StringProperty()
#    remember_token_expires_at   = db.DateTimeProperty()


    actor                       = db.ReferenceProperty(Actor)
    actor_type                  = db.StringProperty()
    preference                  = db.StringProperty()

class Action(BaseModel):
    kind       = db.StringProperty()
    status     = db.StringProperty()
    short_name = db.IntegerProperty() # integer? maybe code?
    name       = db.StringProperty()
    controller = db.StringProperty()
    action     = db.StringProperty()
    tags       = db.TextProperty()

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
    value = db.FloatProperty() # should be Decimal
    scale = db.FloatProperty() # should be Decimal
    path = db.StringProperty()
    name = db.StringProperty()
    parent = db.SelfReferenceProperty()
    client = db.ReferenceProperty(Client)
    json = db.TextProperty()
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

class MailRecipient(BaseModel):
    """ ... """
    kind           = db.StringProperty('type')
    status         = db.IntegerProperty()
    pending_mail   = db.ReferenceProperty(PendingMail)
    recipient_key  = db.StringProperty()
    recipient_type = db.StringProperty()
    tags           = db.StringListProperty()

class PendingMail(BaseModel):
    """ ... """
    kind              = db.StringProperty('type')
    status            = db.IntegerProperty()
    error_code        = db.IntegerProperty()
    error_message     = db.StringProperty()
    error_type        = db.IntegerProperty()
    mailer_template   = db.StringProperty()
    mailer_type       = db.StringProperty()
    qmail_queue_inode = db.IntegerProperty()
    mailable_key      = db.StringProperty()
    mailable_type     = db.StringProperty()
    sender_key        = db.StringProperty()
    sender_type       = db.StringProperty()
    tags              = db.StringListProperty()

class PurchaseOrderApplication(BaseModel):
    purchase_order    = db.ReferenceProperty(PurchaseOrder)
    work_order        = db.ReferenceProperty(WorkOrder)
    json              = db.TextProperty()
    state             = db.TextProperty()
    status            = db.IntegerProperty()

class PurchaseOrders(BaseModel):
    filemakerpro = db.StringProperty()
    quickbooks   = db.StringProperty()
    client_id    = db.IntegerProperty()
    json         = db.TextProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

class Receive(BaseModel):
    json = db.TextProperty()

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
    amount       = db.IntegerProperty() #should be Decimal
    json         = db.TextProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

class Role(BaseModel):
    """
    Represents a user role and any associated metadata.
    
    """
    name = db.StringProperty()
    json = db.TextProperty()

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

class Send(BaseModel):
    json = db.TextProperty()

class TimeSheet(BaseModel):
    """
    Represents a user's time sheet for a task
    
    """
    task                = db.ReferenceProperty(Task)
    person              = db.ReferenceProperty(Person)
    time_sheet_entry    = db.IntegerProperty()
    created_on          = db.DateTimeProperty()
    json                = db.TextProperty()

class Transfer(BaseModel):
    asset    = db.ReferenceProperty(Asset)
    shipment = db.ReferenceProperty(Shipment)
    json     = db.TextProperty()
    state    = db.TextProperty()
    status   = db.IntegerProperty()

