from django.db import models

# Create your models here.

#basics of myDistrict 
class District(models.Model):
	name = models.CharField(max_length=40)
	username = models.CharField(max_length=30)	
	password = models.CharField(max_length=30) 

	def __unicode__(self):
		return "<District: %s id: %d>"%(self.name, self.id)

class User(models.Model):
	EDIT = 'edit'
	VIEW = 'view'
	PERMISSION_CHOICES = (
		(EDIT, 'Edit'),
		(VIEW, 'View-only')
	)	
	name = models.CharField(max_length=40)
	district = models.ForeignKey(District)
	permission = models.CharField(max_length=2,
				choices = PERMISSION_CHOICES,
				default = VIEW)
	def has_edit_permission(self):
		return self.permission == EDIT


#Daimoku Related
class Target(models.Model):
	start_date = models.DateField()
	target_date = models.DateField()
	name = models.CharField(max_length=50)
	description = models.TextField()
	image_path = models.CharField(default='none', max_length=80)

class Daimoku(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	target = models.ForeignKey(Target)
	district = models.ForeignKey(District)
	
	class Meta:
		unique_together = ('target', 'district',
				'start_time', 'end_time')

#Notes related
class Note(models.Model):
	create_date = models.DateTimeField()
	text = models.TextField()
	author = models.ForeignKey(User)
	district = models.ForeignKey(District)

class CalendarEvent(models.Model):
	create_date = models.DateTimeField()
	scheduled_date = models.DateTimeField()
	venue = models.TextField()
	creator = models.ForeignKey(User)
