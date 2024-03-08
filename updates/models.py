from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)






class Updates(models.Model):
    title = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updates')
    description = models.CharField(max_length=500, blank=True)
    img = models.FileField(upload_to='pdfs/', default='pdfs/default.pdf')
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
 
    def __str__(self):
        return self.title
