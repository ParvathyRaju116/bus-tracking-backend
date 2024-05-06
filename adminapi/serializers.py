from rest_framework import serializers
from adminapi.models import Admin,Route,Stop,BusOwner,Passenger,BusCategory,Bus,BusRoute,BusRouteStops,BusStopDetail



class AdminSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Admin
        fields=["id","username","password","email_address"]
   
    def create(self, validated_data):
        return Admin.objects.create_user(**validated_data)
    

class StopSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    route=serializers.CharField(read_only=True)
    class Meta:
        model = Stop
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model = BusCategory
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model = Route
        fields = "__all__"


class BusownerviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusOwner
        fields=["id","username","proof","phone","address","is_approved"]


class PassengerviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields=["id","phone","username","address","email_address"]


class BusSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    busowner=BusownerviewSerializer()
    class Meta:
        model = Bus
        fields = "__all__"
        
        
class BusRouteSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    busowner=BusownerviewSerializer()
    route=RouteSerializer()
    buscategory=CategorySerializer()
    bus=BusSerializer()
    class Meta:
        model = BusRoute
        fields = "__all__"
        
        
class BusRouteStopsSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    route=RouteSerializer()
    bus=BusSerializer()
    class Meta:
        model = BusRouteStops
        fields = "__all__"
        

class BusStopDetailSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model = BusStopDetail
        fields = "__all__"
        
        
class StopEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['stop_number', 'place','image', 'link']

  
    def __init__(self, *args, **kwargs):
        super(StopEditSerializer, self).__init__(*args, **kwargs)
        if self.instance and 'image' not in self.initial_data:
            self.fields.pop('image')