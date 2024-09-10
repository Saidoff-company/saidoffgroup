from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class WhyUs(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Order(TimeStamp):
    full_name = models.CharField(max_length=212)
    phone_number = models.CharField(max_length=212)
    is_checked = models.BooleanField(default=False)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name


class Subscribe(TimeStamp):
    full_name = models.CharField(max_length=212)
    phone_number = models.CharField(max_length=212)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Team(TimeStamp):
    full_name = models.CharField(max_length=212)
    occupation = models.CharField(max_length=212)
    image = models.ImageField(upload_to='team/')
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Partnership(TimeStamp):
    image = models.FileField(upload_to='partnership/')


class Certificate(TimeStamp):
    title = models.CharField(max_length=212)
    information = models.TextField()
    image = models.ImageField(upload_to='certificate/')

    def __str__(self):
        return self.title

class ClientsFeedback(TimeStamp):
    full_name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='feedback/')
    profession = models.CharField(max_length=212)
    message = models.TextField()

    def __str__(self):
        return self.full_name


class ServiceInfo(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='service/')
    description = models.TextField()
    services = models.ForeignKey('Services', on_delete=models.CASCADE, related_name='service_info')

    def __str__(self):
        return self.title


class Services(TimeStamp):
    title = models.CharField(max_length=212)

class Projects(TimeStamp):
    title = models.CharField(max_length=212)
    service = models.ForeignKey('Services', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class SocialMedia(TimeStamp):
    icon = models.ImageField(upload_to='social_media/')
    link = models.URLField(null=True, blank=True)


class FAQType(TimeStamp):
    title = models.CharField(max_length=212)

    def __str__(self):
        return self.title


class FAQ(TimeStamp):
    question = models.TextField()
    answer = models.TextField()
    type = models.ForeignKey('FAQType', on_delete=models.CASCADE)


class About(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()

    def __str__(self):
        return self.title