from rest_framework.serializers import ModelSerializer
from .models import Employe,AddressDetails,WorkExperience,Qualifications,Projects


class AddressDetails_serilaizer(ModelSerializer):
    class Meta:
        model= AddressDetails
        fields= ['hno','street','city','state']

class WorkExperience_serilaizer(ModelSerializer):
    class Meta:
        model= WorkExperience
        fields= ['companyName','fromDate','toDate','address']

class Qualifications_serilaizer(ModelSerializer):
    class Meta:
        model= Qualifications
        fields= ['qualificationsName','fromDate','toDate','percentage']

class Projects_serilaizer(ModelSerializer):
    class Meta:
        model= Projects
        fields= ['title','description']

class Employe_serilaizer(ModelSerializer):
    class Meta:
        model= Employe
        fields= '__all__'
