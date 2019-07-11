from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    # fields = ['published','title','content']

    fieldsets = [
        ("Title/date",{'fields':['title','published']}),
        ("URL", {'fields': ['slug']}),
        ("Series", {'fields': ['series']}),
        ("Content",{'fields':['content']})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)