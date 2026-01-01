from django.contrib import admin
from .models import *

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Material)
admin.site.register(Note)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizResult)
