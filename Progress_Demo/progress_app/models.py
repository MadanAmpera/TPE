from django.db import models

# I am going to create my models here

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    emailId = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    parentContactId = models.IntegerField()  # key in same table
    contactTypeId = models.IntegerField()


class Student(models.Model):
    contactId = models.ForeignKey(Contact, related_name='contact_information_in', on_delete=models.SET_NULL, blank=True,
                                  null=True)  # key from contact table
    schoolName = models.CharField(max_length=200)
    schoolYear = models.IntegerField()  # need to increment it yearly
    birthday = models.DateField()


'''class Commitment(models.Model):
    periodId = models.IntegerField()  # from config-yearly, weekly, etc
    contactId = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    # duration = models.IntegerField()  # should it be time? and is this field needed
    locationId = models.IntegerField()  # from config
    typeId = models.IntegerField()  # Maths/English - from config
    # status = models.IntegerField()#from config - is this needed in comittment?


class CommitmentInstance(models.Model):
    commitmentId = models.ForeignKey(Commitment, related_name='is_generated_from', on_delete=models.SET_NULL,
                                     blank=True, null=True)  # from commitment table
    contactId = models.ForeignKey(Contact, related_name='is_assigned_to', on_delete=models.SET_NULL,
                                  blank=True, null=True)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    # duration = models.IntegerField()  # should it be time?
    locationId = models.IntegerField()  # from config
    typeId = models.IntegerField()  # Maths/English - from config
    status = models.IntegerField()  # from config
    notes = models.CharField(max_length=1000)'''


class ProgressForm(models.Model):
    #commitmentInstanceId = models.ForeignKey(CommitmentInstance, related_name='is_a_result_of',
                                             #on_delete=models.SET_NULL, blank=True, null=True)
    progressEntryTypeId = models.IntegerField()  # from config
    studentContactId = models.ForeignKey(Contact, related_name='shows_progress_of', on_delete=models.SET_NULL,
                                         blank=True, null=True)  # from contact
    staffContactId = models.IntegerField()  # from contact
    notes = models.CharField(max_length=1000)


class ActionRequired(models.Model):
    #commitmentInstanceId = models.ForeignKey(CommitmentInstance, related_name='is_an_outcome_of',
                                             #on_delete=models.SET_NULL, blank=True, null=True)  # from commitInstance
    staffContactId = models.ForeignKey(Contact, related_name='is_raised_by', on_delete=models.SET_NULL, blank=True,
                                       null=True)  # from contact-raised by
    actionForContactId = models.IntegerField()  # from contact-for student
    notes = models.CharField(max_length=1000)
    dueDate = models.DateField()
    actioned = models.BooleanField()
    actionedByContactId = models.IntegerField()  # from contact


class Configuration(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

