from django.db import models

# Create your models here.
SCHEME_CHOICES = [
    ('I', 'Scheme I'),
    ('K', 'Scheme K'),
]

class Syllabus(models.Model):
    subject_name = models.CharField(max_length=200)
    scheme = models.CharField(max_length=1, choices=SCHEME_CHOICES)
    pdf = models.FileField(upload_to='syllabus_pdfs/')

    def __str__(self):
        return f"{self.subject_name} ({self.scheme})"


class QuestionPaper(models.Model):
    subject_name = models.CharField(max_length=200)
    scheme = models.CharField(max_length=1, choices=SCHEME_CHOICES)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='papers_pdfs/')

    def __str__(self):
        return f"{self.subject_name} {self.year} ({self.scheme})"