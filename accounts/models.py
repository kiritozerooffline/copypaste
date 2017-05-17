from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

class UserProfile(models.Model):
		user = models.OneToOneField(User)
		description = models.CharField(max_length=100, default='')
		city = models.CharField(max_length=100, default='')
		website = models.URLField(default='')
		phone = models.IntegerField(default='')

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

	return post_save.connect(create_profile, sender=User)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

