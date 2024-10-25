from django.urls import path
from .views import CampaignList, VaccineList, VaccineDetail, CampaignDetail

urlpatterns = [
    path("", CampaignList.as_view(), name="campaign_list"),
    path("<int:pk>/", CampaignDetail.as_view(), name="campaign_detail"),
    path("vaccine/", VaccineList.as_view(), name="vaccine_list"),
    path("vaccine/<int:pk>/", VaccineDetail.as_view(), name="vaccine_detail"),
]
