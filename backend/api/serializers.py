from rest_framework import serializers
from travelCompanion_App.models import Trip

class TripSerializer(serializers.ModelSerializer):
    completed = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    class Meta:
        model = Trip
        fields = ['id', 'spouse', 'first_child', 'second_child', 'third_child', 'others', 'trip_purpose', 'departure_date', 'return_date', 'departure_location', 'destination_location', 'trip_cost', 'created','completed']
                
                
                

class TripToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id'] # why need to show id?
        read_only_fields = ['spouse','first_child','second_child', 'third_child', 'others', 'trip_purpose', 'departure_date', 'return_date', 'departure_location', 'destination_location', 'trip_cost', 'created', 'completed']