from django.db import models
from django.utils import timezone
from django.urls import reverse

app_name = 'index'

class Science(models.Model):
	SCIENCE_STATUS = (('active', 'Active'), ('inactive', 'InActive'),)
	name = models.CharField(max_length=250,)
	status = models.CharField(max_length=10, choices=SCIENCE_STATUS, default='inactive')
	def __str__(self):
		return self.name
		
class Teachers(models.Model):
    STATUS_CHOICES = (('active', 'Active'), ('inactive', 'InActive'),)
    DEGREE_CHOICES = (
        ('mutaxasis', 'Mutaxasis'), ('ikkinchi', 'Ikkinchi toifa'),
        ('birinchi', 'Birinchi toifa'), ('oliy', 'Oliy toifa'),
    )
    GRADE_CHOICES = (
        ('direktor', 'Direktor'), ('mmibdu', 'MMIBDO\''),
        ('uibdu', 'O\'IBDO\''), ('uqtuvchi', 'O\'qtuvchi'),('psixolog', 'Psixolog'),
    )
    full_name = models.CharField(max_length=250,)
    birth_date = models.DateField()
    science = models.ManyToManyField(Science,)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES,default='mutaxasis')
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES,default='uqtuvchi')
    image = models.ImageField(upload_to='teachers/', blank=True, default='teachers/no_image.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='inactive')

    class Meta:
        ordering = ('full_name',)
    
    def __str__(self):
        return self.full_name