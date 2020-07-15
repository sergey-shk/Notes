from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=60, default='Untitled',db_index=True)
    body = models.TextField(max_length=400, default='...')
    pub_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False, default=None)

    def __str__(self):
        return '{}'.format(self.title)
