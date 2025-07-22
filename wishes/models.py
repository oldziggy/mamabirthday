from django.db import models



class Wish(models.Model):

    wish_text = models.TextField()

    sender = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    image = models.ImageField(blank=True,null=True,default=None)


    def __str__(self):
        return str(self.sender)
    class Meta:
        verbose_name_plural = 'Wishes'


