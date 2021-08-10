from django.db import models
from django.urls import reverse
# Create your models here.

class Contact(models.Model):
	name = models.CharField('Ismi...', max_length=50)
	number = models.CharField('Telefon raqami....', max_length=30)
	email = models.EmailField('Emaili...')
	message = models.TextField('Xabari...')

	def __str__(self):
		return self.name

	class Meta:

		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'


class City(models.Model):
	title = models.CharField('Shahar ismi...', max_length=30)
	slug = models.SlugField('*',unique=True)
	image = models.ImageField('Shahar rasmi...',upload_to='media/cityImage/')


	def __str__(self):
		return self.title

	class Meta:

		verbose_name = 'Shahar'
		verbose_name_plural = 'Shaharlar'


class TransportCategory(models.Model):
	name = models.CharField('Kategoriya nomi', max_length=50)
	slug = models.SlugField('*',unique=True)

	def __str__(self):
		return self.name

	class Meta:

		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

	def get_absolute_url(self):

		return reverse('main:category_detail',kwargs={'category_slug':self.slug})


class BusGrafik(models.Model):
	city = models.CharField('Shaharlar nomi....', max_length=50)
	slug = models.SlugField('*',unique=True)
	time = models.CharField('Vaqti...', max_length=15)
	price = models.PositiveIntegerField('Narxi....',default=0)

	def __str__(self):
		return self.city

	class Meta:

		verbose_name = 'AvtobusGrafik'
		verbose_name_plural = 'AvtobusGrafiklar'

class FortGrafik(models.Model):
	city = models.CharField('Shaharlar nomi....', max_length=50)
	slug = models.SlugField('*',unique=True)
	time = models.CharField('Vaqti...', max_length=15)
	price = models.PositiveIntegerField('Narxi....',default=0)

	def __str__(self):
		return self.city

	class Meta:

		verbose_name = 'FortGrafik'
		verbose_name_plural = 'FortGrafiklar'


class Transport(models.Model):
	name = models.CharField('Mashina nomi...', max_length=100)
	slug = models.SlugField('*',unique=True)
	image = models.ImageField('Mashina rasmi...',upload_to='media/carsImage/')
	category = models.ForeignKey(TransportCategory,on_delete=models.PROTECT)
	city = models.ForeignKey(City,on_delete=models.PROTECT)
	price = models.PositiveIntegerField('Narxi....',default=0)
	first_time = models.CharField('Boshlanish vaqti...',max_length=6)
	last_time = models.CharField('Tugash vaqti.....',max_length=6)

	def __str__(self):
		return self.name

	class Meta:

		verbose_name = 'Transport'
		verbose_name_plural = 'Transportlar'

