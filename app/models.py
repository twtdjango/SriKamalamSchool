from django.db import models


class Job(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Applicants(models.Model):
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
    Message = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Application(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
    Message = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class ApplicationFile(models.Model):
    Name = models.CharField(max_length=50)
    File = models.FileField(upload_to='media/ApplicationFile')


class Circular(models.Model):
    CircularText = models.TextField()
    File = models.FileField(upload_to='media/Circular/File')
    Image = models.ImageField(upload_to='media/Circular/Images')
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Event(models.Model):
    Name = models.CharField(max_length=50)
    StartDate = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    FromDate = models.DateField()
    ToDate = models.DateField()  # Tdate
    Image = models.ImageField(upload_to='media/Event')
    Description = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    GoogleLocation = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
    Message = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class File(models.Model):
    Name = models.CharField(max_length=50)
    File = models.FileField(upload_to='media/File')
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Gallery(models.Model):
    Name = models.CharField(max_length=50)
    File = models.FileField(upload_to='media/Gallery')
    Link = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Tag(models.Model):
    Name = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Name


class Image(models.Model):
    Image = models.ImageField(upload_to='media/Gallery/Images')
    Tag1 = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.Image)


class Video(models.Model):
    Video = models.CharField(max_length=255)
    Tag1 = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.Video)


class Slider(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)
    Image = models.ImageField(upload_to='media/Slider')
    Tag = models.CharField(max_length=50)
    Link = models.CharField(max_length=50)


class Upload(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)
    Filename = models.CharField(max_length=50)


class View1(models.Model):
    IP = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    URL = models.CharField(max_length=50)
    Time = models.DateTimeField(auto_now_add=True, blank=True)
