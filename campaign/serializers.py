from rest_framework import serializers
from .models import CampaignModel, VaccinesModel



# class CampaignModelSerializer(serializers.ModelSerializer):
#     doctor_username = serializers.ReadOnlyField(source='doctor.username')
#     class Meta:
#         model = CampaignModel
#         fields = ['id', 'name', 'image', 'description', 'created_at', 'updated_at', 'doctor_username']

class CampaignModelSerializer(serializers.ModelSerializer):
    doctor_username = serializers.ReadOnlyField(source='doctor.username')

    class Meta:
        model = CampaignModel
        fields = ['id', 'name', 'image', 'description', 'created_at', 'updated_at', 'doctor_username']

    def create(self, validated_data):
        doctor = self.context['request'].user
        validated_data.pop('doctor', None)
        campaign = CampaignModel.objects.create(**validated_data)
        campaign.doctor = doctor
        campaign.save()
        return campaign



class VaccinesModelSerializer(serializers.ModelSerializer):
    doctor_username = serializers.ReadOnlyField(source='doctor.username')
    class Meta:
        model = VaccinesModel
        fields = ['id','doctor_username', 'name', 'schedule' ]



