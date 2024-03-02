from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)






class Pdf(models.Model):
    title = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    pdf_file = models.FileField(upload_to='pdfs/')
    PRODUCT_TYPES = [
        ('Agriculture', 'Agriculture'),
('Biology', 'Biology'),
('Chemistry', 'Chemistry'),
('Commerce', 'Commerce'),
('Computer Studies', 'Computer Studies'),
('Divinity', 'Divinity'),
('Economics', 'Economics'),
('Electricity', 'Electricity'),
('Entrepreneurship', 'Entrepreneurship'),
('Fine Art', 'Fine Art'),
('French', 'French'),
('Geography', 'Geography'),
('History', 'History'),
('Home Economics', 'Home Economics'),
('Islamiat', 'Islamiat'),
('Kiswahili', 'Kiswahili'),
('Literature in English', 'Literature in English'),
('Luganda', 'Luganda'),
('Mathematics', 'Mathematics'),
('Metalwork', 'Metalwork'),
('Music', 'Music'),
('Physical Education', 'Physical Education'),
('Physics', 'Physics'),
('Subsidiary ICT', 'Subsidiary ICT'),
('Technical Drawing', 'Technical Drawing'),
('Woodwork', 'Woodwork')

    ]
    created_on = models.DateTimeField(auto_now_add=True)
  
    product_type = models.CharField(max_length=100, choices=PRODUCT_TYPES)

    class Meta:
        ordering = ['-created_on']
 
    def __str__(self):
        return self.title
