from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname

class suspended_accounts(models.Model):
    user_id = models.IntegerField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class bank_master(models.Model):
    bankname = models.CharField(max_length=150)
    bankifsc = models.CharField(max_length=50)
    bankaddress = models.CharField(max_length=500)
    bankcontact = models.CharField(max_length=50)
    bankemail = models.CharField(max_length=50)


class user_bank(models.Model):
    userid = models.IntegerField()
    bankid = models.IntegerField()
    accno = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    type_of_acc = models.CharField(max_length=50)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    balance = models.FloatField()
    addr1 = models.CharField(max_length=500)
    addr2 = models.CharField(max_length=500)
    addr3 = models.CharField(max_length=500)
    pin = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=50)

class user_bank_transaction(models.Model):
    userid = models.IntegerField()
    bankid = models.IntegerField()
    t_no = models.CharField(max_length=50)
    t_type = models.CharField(max_length=50)
    amount = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class user_bank_transactions(models.Model):
    from_userid = models.IntegerField()
    to_userid = models.IntegerField()
    t_no = models.CharField(max_length=50)
    t_type = models.CharField(max_length=50)
    amount = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

