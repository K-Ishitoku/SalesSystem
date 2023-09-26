from django.contrib import admin

from .models import Question

from .models import Vendors

from .models import Cases

admin.site.register(Question)

admin.site.register(Vendors)

admin.site.register(Cases)


# Register your models here.
