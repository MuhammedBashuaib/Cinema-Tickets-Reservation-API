from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    #start class MovieSerializer
    class Meta:
        #start class Meta
        model = Movie
        fields = '__all__'
        #end class Meta
    #endl class MovieSerializer


class GuestSerializer(serializers.ModelSerializer):
    #start class GuestSerializer
    class Meta:
        #start class Meta
        model = Guest
        fields = '__all__'
        #end class Meta
    #endl class GuestSerializer


class ReservationSerializer(serializers.ModelSerializer):
    #start class ReservationSerializer
    class Meta:
        #start class Meta
        model = Reservation
        fields = ['pk', 'reservation', 'name', 'mobile']
        #end class Meta
    #endl class ReservationSerializer
