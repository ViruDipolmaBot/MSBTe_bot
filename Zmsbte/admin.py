from django.contrib import admin

from .models import Syllabus, QuestionPaper

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'scheme')
    list_filter = ('scheme',)

@admin.register(QuestionPaper)
class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'scheme', 'year')
    list_filter = ('scheme', 'year')