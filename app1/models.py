from django.db import models

# Create your models here.
STATUS=(
    ('male','male'),
    ('female','female')
)

class AddressDetails(models.Model):
    hno= models.CharField(max_length=50)
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)


class WorkExperience(models.Model):
    companyName = models.CharField(max_length=30)
    fromDate = models.CharField(max_length=30)
    toDate = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

class Qualifications(models.Model):
    qualificationsName = models.CharField(max_length=30)
    fromDate = models.CharField(max_length=30)
    toDate = models.CharField(max_length=30)
    percentage = models.CharField(max_length=4)

class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Employe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    age= models.IntegerField()
    gender= models.CharField(max_length=10,choices= STATUS)
    phoneNo= models.CharField(max_length=15)
    addressDetails= models.ForeignKey(AddressDetails,on_delete=models.CASCADE)
    workExperience = models.ForeignKey(WorkExperience,on_delete=models.CASCADE)
    qualifications = models.ForeignKey(Qualifications,on_delete=models.CASCADE)
    projects = models.ForeignKey(Projects,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='upload/images/')


    def __str__(self):
        return self.name
