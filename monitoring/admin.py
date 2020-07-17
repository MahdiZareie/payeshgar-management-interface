from django.contrib import admin
from .models import Endpoint, Agent, Group, MonitoringPolicy, HTTPEndpointDetail


@admin.register(Endpoint)
class EPAdmin(admin.ModelAdmin):
    pass


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(MonitoringPolicy)
class MonitoringPolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(HTTPEndpointDetail)
class HTTPEndpointDetailAdmin(admin.ModelAdmin):
    pass
