from django.db import models
from mongoengine import *
import datetime

class User(Document):
    first_name = StringField()
    last_name = StringField()
    password = StringField()
    mobile_no = IntField(unique = True)


class Deposit_Form(Document):
    customer_id = ReferenceField(User)
    acc_no = IntField(required = True)
    ifsc_code = IntField(required = True)
    account_holder_name = StringField()
    accounter_holder_mobile_num = IntField()

class Ticket(Document):
    customer_id = ReferenceField(User, reverse_delete_rule=True)
    type_transcation = StringField(max_length = 10, choices = ['deposite','loan'])
    responese_time = DateTimeField()
    resolved_time = DateTimeField()
    counter_id = IntField()
    ETA = DateTimeField()
    expire_time = DateTimeField()
    active = IntField()
    meta = {'allow_inheritance': True}

class deposit_form_data(Ticket):
    data = ReferenceField(Deposit_Form)
# Create your models here.

class Banker(Document):
    name = StringField()
    employee_id = IntField(unique = True)
    processed_tickets = ListField(ReferenceField(Ticket))
    password = StringField()

class Deposit_Counter(Document):
    counter_id = IntField(unique=True)
    active_count = IntField()
    list_of_ticket_id = ListField(ReferenceField(Ticket))

class Counter_Queue(Document):
    counter_type = StringField()
    list_ticket = ListField(ReferenceField(Ticket))
