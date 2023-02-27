from django.db import models

# Create your models here.

class Movie(models.Model):
    #start class Movie
    hall = models.CharField(max_length=50)
    movie = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.hall
    #end class Movie

class Guest(models.Model):
    #start class Guest
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    #end class Guest

class Reservation(models.Model):
    #start class Reservation
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)

    
    #end class Reservation