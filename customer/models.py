from django.db import models


# Create your models here.
class Customer(models.Model):
	mail = models.CharField(max_length=40)
	phone = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	score = models.IntegerField(default=0)
	token = models.CharField(max_length=255, null=True)
	status = models.IntegerField(default=0)

	def signup_customer(self):
		customer_by_mail = self.get_customer_by_mail()
		customer_by_phone = self.get_customer_by_phone()
		if customer_by_mail is None and customer_by_phone is None:
			self.save()
			return True
		else:
			return False

	def get_customer_by_mail(self):
		try:
			customer = Customer.objects.get(mail=self.mail)
		except Exception, e:
			return None
		else:
			return customer

	def get_customer_by_phone(self):
		try:
			customer = Customer.objects.get(phone=self.phone)
		except Exception, e:
			return None
		else:
			return customer

	def to_dict(self):
		customer_dict = dict()
		customer_dict['name'] = self.name
		customer_dict['mail'] = self.mail
		customer_dict['phone'] = self.phone
		return customer_dict


