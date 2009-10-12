# actors/api.py

from djangocore.api.sites import site
from djangocore.api.models.ae import ModelResource
from actors.models import *

models = [Actor, Client, Person, Executable]

# Register all of the models in one shot
for m in models:
		site.register(ModelResource, model=m)