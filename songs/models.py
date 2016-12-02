from django.db import models


class Song(models.Model):
    # Basic data but in this case we r making it easier
    created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)
    # Song data
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    # email = models.EmailField()  # We will use it to verify user. Only the user who create a song can delete
    link = models.URLField(null=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.author)

    def full_name(self):
        return '{} ({})'.format(self.title, self.author)
