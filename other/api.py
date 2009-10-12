# other/api.py

from djangocore.api.sites import site
from djangocore.api.models.ae import ModelResource
from other.models import *


models = [Ability, Access, Agent, AssetDeliverable, Asset, Assingment,
		Authorization, BillableRate, BillableRole, Billing, BuildDeliverable,
		Deliverable, Departments, ElementAsset, EntryMapping, EventAuthorization,
		Event, Executable, Issue, Requirement, Resource, Role, SecurityContext,
		Vendor]

# Register all of the models in one shot
for m in models:
		site.register(ModelResource, model=m)