from django.db import models
from accounts.models import MyUser

# Create your models here.
class Comment(models.Model):
    Username = models.ForeignKey(MyUser,editable=False, on_delete=models.CASCADE)
    body = models.TextField()
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.Username)    

 



