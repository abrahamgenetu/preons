from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory, News
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title","tutorial_published","tutorial_content"]
    fieldsets = [("Title/date", {"fields": ["title", "published"]}),
                 ("URL", {"fields": ["tutorial_slug"]}),
                 ("Series", {"fields": ["tutorial_series"]}),
                 ("Cover image", {"fields": ["tutorial_image"]}),
                 # ("Sample Video", {"fields": ["tutorial_video"]}),
                 ("Introduction", {"fields": ["content_first"]}),
                 ("Lesson", {"fields": ["content_second"]}),
                 ("Summary", {"fields": ["content_third"]})
                 ]
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [("Header/Date", {"fields": ["header", "date"]}),
                 ("Content", {"fields": ["body"]})]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(News, NewsAdmin)
# Register your models here.
