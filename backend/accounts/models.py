from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    EXPERIENCE_CHOICES = [
        ('fresher', 'Fresher'),
        ('entry', 'Entry-level'),
        ('experienced', 'Experienced'),
    ]
    
    MODE_CHOICES = [
        ('text', 'Text Interview'),
        ('voice', 'Voice Interview'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    target_role = models.CharField(max_length=255, blank=True, default='')
    preferred_mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='text')
    default_experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='entry')
    bio = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.username} ({self.target_role or 'No role specified'})"


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
        else:
            UserProfile.objects.create(user=instance)
