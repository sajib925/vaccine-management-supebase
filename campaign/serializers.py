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
        # Remove the doctor field from validated_data if it exists
        validated_data.pop('doctor', None)  # Ensure doctor is not part of validated_data
        doctor = self.context['request'].user.doctor  # Get doctor from request context
        # Create the campaign with the doctor assigned
        campaign = CampaignModel.objects.create(doctor=doctor, **validated_data)  # Assign doctor while creating
        return campaign



class VaccinesModelSerializer(serializers.ModelSerializer):
    doctor_username = serializers.ReadOnlyField(source='doctor.username')
    class Meta:
        model = VaccinesModel
        fields = ['id','doctor_username', 'name', 'schedule' ]



