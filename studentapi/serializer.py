from rest_framework import serializers

from studentapi.models import Students


def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("name must start with r")
    return value
    

#normal serializer
# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=50,validators=[starts_with_r])
#     age=serializers.IntegerField()
#     city=serializers.CharField(max_length=50)
    
#     def create(self, validated_data):
#         return Students.objects.create(**validated_data)
#     def update(self, instance, validated_data):

#         instance.name=validated_data.get('name',instance.name)

#         instance.age=validated_data.get('age',instance.age)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
#     #field level validation
#     def validate_age(self,value):
#         if value>20:
#             raise serializers.ValidationError("seat full")
#         return value
#     #object level validation
#     def validate(self, data):
#         n=data.get("name")
#         c=data.get("city")
#         if n[0].lower()!='rohan' or c.lower()!="cuttack":
#             raise serializers.ValidationError("City Must be cuttack and name should start with r")
#         return data

#ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100,validators=[starts_with_r])
    class Meta:
        model=Students
        # fields='__all__'
        fields=['id','name','age','city']
    #field level validation
    # def validate_age(self,value):
    #     if value>20:
    #         raise serializers.ValidationError("seat full")
    #     return value
    # object level validation
    # def validate(self, data):
    #     n=data.get("name")
    #     c=data.get("city")
    #     if n[0].lower()!="r" or c.lower()!="cuttack":
    #         raise serializers.ValidationError("City Must be cuttack and name should start with rohan")
    #     return data    