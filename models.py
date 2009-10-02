class Ability(BaseModel):
    actor = db.ReferenceProperty(Actor)
    role = db.ReferenceProperty(Role)
    yaml = db.StringProperty()
    actor_type = db.StringProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()

class Asset(BaseModel):
    location = db.StringProperty()
    note = db.TextProperty()
    type = db.StringProperty()
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
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()
    children_count = db.IntegerProperty()

class Authorization(BaseModel):
    type = db.StringProperty()
    event = db.ReferenceProperty(Event)
    security_context = db.ReferenceProperty(SecurityContext) # ??
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()

class Deliverable(BaseModel):
    name = db.StringProperty()
    due_date = db.DateTimeProperty()
    type = db.StringProperty()
    yaml = db.TextProperty()
    state = db.TextProperty()
    status = db.IntegerProperty()

class Event(BaseModel):
    created_on = db.DateTimeProperty()
    name = db.StringProperty()
    securable = db.ReferenceProperty(Secure) 
    securable_type = db.StringProperty()
    securable_state = db.TextProperty()
    task = db.ReferenceProperty(Task)

class Issue(BaseModel):
    analysis    = db.TextProperty()
    name        = db.StringProperty()
    severity    = db.IntegerProperty()
    status      = db.IntegerProperty()
    type        = db.StringProperty()
    element_type = db.StringProperty()
    element_id  = db.IntegerProperty()

class PurchaseOrderApplication(BaseModel):
    purchase_order    = db.ReferenceProperty(PurchaseOrder)
    work_order        = db.ReferenceProperty(WorkOrder)
    yaml              = db.TextProperty()
    state             = db.TextProperty()
    status            = db.IntegerProperty()

class PurchaseOrders(BaseModel):
    filemakerpro = db.StringProperty()
    quickbooks   = db.StringProperty()
    client_id    = db.IntegerProperty()
    yaml         = db.TextProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

class Receive(BaseModel):
    yaml = db.TextProperty()

class Requirement(BaseModel):
    name   = db.StringProperty()
    yaml   = db.TextProperty()
    state  = db.TextProperty()
    status = db.IntegerProperty()
    type   = db.StringProperty()

class Resource(BaseModel):
    type         = db.StringProperty()
    name         = db.StringProperty()
    filemakerpro = db.StringProperty()
    quickbooks   = db.StringProperty()
    location     = db.StringProperty()
    amount       = db.IntegerProperty() #should be Decimal
    yaml         = db.TextProperty()
    state        = db.TextProperty()
    status       = db.IntegerProperty()

class Role(BaseModel):
    name = db.StringProperty()
    yaml = db.TextProperty()

class SecurityContext(BaseModel):
    status         = db.IntegerProperty()
    yaml           = db.TextProperty()
    state          = db.TextProperty()
    position       = db.IntegerProperty()
    children_count = db.IntegerProperty()
    parent         = db.SelfReferenceProperty()
    securable      = db.ReferenceProperty(Secure) # not sure
    securable_type = db.StringProperty()

class Send(BaseModel):
    yaml = db.TextProperty()

class TimeSheet(BaseModel):
    task_id          = db.ReferenceProperty(Task)
    person_id        = db.ReferenceProperty(Person)
    time_sheet_entry = db.IntegerProperty()
    created_on       = db.DateTimeProperty()
    yaml             = db.TextProperty()

class Transfer(BaseModel):
    asset    = db.ReferenceProperty(Asset)
    shipment = db.ReferenceProperty(Shipment)
    yaml     = db.TextProperty()
    state    = db.TextProperty()
    status   = db.IntegerProperty()

