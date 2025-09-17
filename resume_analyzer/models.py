from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    analysis = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Resume {self.id} - {self.file.name}"


# Create your models here.
