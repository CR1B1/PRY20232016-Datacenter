import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models
from authentication.models import User
from public.prediction_IA import priority_prediction

PRIORITY_CHOICES = (
    ("MEDIA", "Media"),
    ("BAJA", "Baja"),
    ("ALTA", "Alta"),
    ("CRITICA", "Critica"),
)

PRIORITY_DATES = {
    "MEDIA": 5, "BAJA": 7, "ALTA": 3, "CRITICA": 1
}

class PriorityRanges(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    subject_name = models.CharField(max_length=50, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True)
    
    def __str__(self):
        return u'{0}'.format(self.priority)

class Incidence(models.Model):
    incidence_detail = models.TextField(max_length=2000, null=True)
    incidence_subject = models.ForeignKey(Subject, related_name='incidence_subject', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, related_name='incidence_user', null=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField(null=True) 
    solved_date = models.DateTimeField(null=True)
    solved = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.incidence_detail[:40]
    
@receiver(pre_save, sender=Incidence)
def incidence_handler(sender, instance, *args, **kwargs):
    _dict = dict(PriorityRanges.objects.filter(name="default").first().data)
    priority = priority_prediction(instance.incidence_detail.lower())
    instance.incidence_subject = Subject.objects.create(priority=priority)
    days = _dict.get(priority.lower(), "")
    target_date = datetime.datetime.now() + datetime.timedelta(days=int(days))
    instance.target_date = target_date

@receiver(post_save, sender=Incidence)
def incidence_handler_update(sender, instance, created, **kwargs):
    instance.solved_date = datetime.datetime.now()

class AccessRequest(models.Model):
    request_user = models.ForeignKey(User, related_name='request_user', null=True, on_delete=models.SET_NULL)
    approver_user = models.ForeignKey(User, related_name='approver_user', null=True, on_delete=models.SET_NULL)
    create_date = models.DateField(auto_now_add=True)
    approval_date = models.DateField(blank=True, null=True)
    approval = models.BooleanField(default=False)
    showed = models.BooleanField(default=False)
    
