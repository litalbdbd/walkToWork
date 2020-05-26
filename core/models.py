from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    data = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"

    def get_jobs(self):
        l = [x.job.name for x in self.employees.all()]
        nl = list(dict.fromkeys(l))
        s = []
        for job in nl:
            s.append(f'{l.count(job)} {job}')
        y = ""
        x = s
        y = ", ".join(x)

        return y


class Job(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True, related_name='employees')
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
