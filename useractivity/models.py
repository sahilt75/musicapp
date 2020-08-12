from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ('Song','Song'),
    ('Genre','Genre'),
    ('Album','Album'),
    ('Artist','Artist'),
)

class Recommendation(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user_fk')
    type_id = models.IntegerField()
    type = models.CharField(choices=TYPE,max_length=50)

