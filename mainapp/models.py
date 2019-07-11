from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class todo_dates(models.Model):
    date = models.DateField(default = datetime.date.today)
    link = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date','link',)

    def __str__(self):
        return str(self.date) + ' : ' + str(self.link)


class Items(models.Model):
    content = models.CharField(max_length = 200)
    created_on = models.DateField(default = datetime.date.today)
    completed_on = models.DateField(default = None, null = True, blank = True)
    completed = models.BooleanField(default=False)
    link = models.ForeignKey(todo_dates,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('content','link',)


    def __str__(self):
        return str(self.content) + ' : ' + str(self.link)
