from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=60, default='Untitled',db_index=True)
    body = models.TextField(max_length=400, default='...')
    pub_date = models.DateTimeField(auto_now_add=True)
    #deadline = models.DateField(auto_now_add=False, default=None, null=True)
    date = models.DateTimeField(auto_now_add=False, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)
