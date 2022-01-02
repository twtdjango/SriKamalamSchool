from django.db import models

CHOICES_CLASS = (
    ('PREKG', 'PREKG'),
    ('LKG', 'LKG'),
    ('UKG', 'UKG'),
    ('CLASS I', '1'),
    ('CLASS II', '2'),
    ('CLASS III', '3'),
    ('CLASS IV', '4'),
    ('CLASS V', '5'),
    ('CLASS VI', '6'),
    ('CLASS VII', '7'),
    ('CLASS VIII', '8'),
    ('CLASS IX', '9'),
    ('CLASS X', '10'),
    ('CLASS XI', '11'),
    ('CLASS XII', '12'),

)


class ClassOption(models.Model):
    Classname = models.CharField(max_length=25, choices=CHOICES_CLASS)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Homework(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Type = models.CharField(max_length=35)
    Attach = models.CharField(max_length=35)
    Time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Title


class Message(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Type = models.CharField(max_length=35)
    Time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Title
