# tasks/api.py

from djangocore.api.sites import site
from djangocore.api.models.ae import ModelResource
from tasks.models import *

models = [Action, Credential, Project, ProjectWithOrders, ActiveTask, Task,
		WorkflowObserver, TaskAssignment, TaskLogs, TaskAssignmentQueue,
		TaskRequirement, WaitingTask]

# Register all of the models in one shot
for m in models:
		site.register(ModelResource, model=m)