from django.contrib import admin

from .models import Syllabus, QuestionPaper

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('branch', 'semester', 'subject')
    search_fields = ('branch', 'semester', 'subject')

@admin.register(QuestionPaper)
class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'scheme', 'year')
    list_filter = ('scheme', 'year')