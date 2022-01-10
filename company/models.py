from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# from campaign,
#
# id, name, start_date
#
#
#
# From client,
#
# company, email, phone number

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    company = models.CharField(max_length=256)
    name = models.CharField(max_length=256, blank=True, default="")
    position = models.CharField(max_length=256, blank=True, default="")
    email = models.CharField(max_length=256, blank=True, default="")
    phone_number = models.CharField(max_length=256, db_index=True)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class POIType(TimeStampedModel):
    title = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'poi_type'

    def __str__(self):
        return self.title


class POISector(TimeStampedModel):
    title = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'poi_sector'

    def __str__(self):
        return self.title


class POIJobs(TimeStampedModel):
    title = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'poi_jobs'

    def __str__(self):
        return self.title


class POIInterests(TimeStampedModel):
    title = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'poi_interests'

    def __str__(self):
        return self.title


class POI(TimeStampedModel):
    poi_type = models.ForeignKey(POIType, on_delete=models.CASCADE)
    poi_sector = models.ForeignKey(POISector, on_delete=models.CASCADE)
    point = models.FloatField(null=True, blank=True)
    poi_job = models.ManyToManyField(POIJobs, related_name='poi_jobs_set', blank=True)
    poi_interests = models.ManyToManyField(POIInterests, related_name='poi_interests_set', blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'poi'

    def __str__(self):
        return f'{self.poi_type.title}'


class Student(models.Model):
    name = models.CharField(max_length=20)
    major = models.ForeignKey('Subject', related_name='students_set', on_delete=models.CASCADE)
    minor = models.ForeignKey('Subject', related_name='minor_students_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# through keyword