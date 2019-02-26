from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    post = models.ManyToManyField('Post' , blank=True )


class Post(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField(null=True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True)


    def __str__(self):
        return self.title





#add picture profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
# choose font
