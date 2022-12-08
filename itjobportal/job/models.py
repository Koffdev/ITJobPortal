from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    skills = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Job(models.Model):

    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    key_skills = models.TextField()
    description = models.TextField(blank=True, null=True)

    company_name = models.CharField(max_length=255)
    company_country = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title

class UserRequest(models.Model):

    ADOPTED = 'adopted'
    APPROVED = 'approved'
    UNDEFINED = 'undefined'

    CHOICES_STATUS = (
        (ADOPTED, 'Adopted'),
        (APPROVED, 'Approved'),
        (UNDEFINED, 'Undefined')
    )
    
    user = models.ForeignKey(User, related_name='user_requests', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='items', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=UNDEFINED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('job',)

    def __str__(self):
        return self.user.username + "---" + self.job.title
    
    @staticmethod
    def get_request_by_user(user_id):
        return UserRequest.objects.filter(user=user_id)
