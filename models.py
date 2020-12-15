from django.db import models

# Create your models here.
class Poll(Models.Model)
    subject = models.CharField('投票主題', max_length=200)
    description = models.TextField('投票內容說明')
    date_created = models.DateField(auto_now_add=True)


def__str__(self):
   return str(self.id) + =) = + self.subject

class Option(models.Model):
    poll_id = models.IntegerField('所屬投票主題編號')
    title = models.CharField('選項標題', max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ")" + self.title + "0" + str(self.poll_id)