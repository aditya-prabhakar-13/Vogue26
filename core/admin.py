from django.contrib import admin
from core import models
# Register your models here.
admin.site.register(
    [
        models.Member_Detail,
        models.Competition,
        models.Role,
        models.Team,
    ]
)
