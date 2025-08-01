from django.db import models



class Wish(models.Model):

    wish_text = models.TextField(blank=True,null=True,default=None)

    sender = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    image = models.ImageField(blank=True,null=True,default=None)

    audio = models.FileField(blank=True, null=True,default=None)

    video = models.FileField(blank=True, null=True,default=None)


    def __str__(self):
        return str(self.sender)
    class Meta:
        verbose_name_plural = 'Wishes'


