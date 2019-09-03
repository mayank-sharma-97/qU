from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from mongoengine import *
from django.http import HttpResponse
from . import models
import datetime
connect('Bank')
# Create your views here.

global deposit_queue
global deposit_queue_1
global avg_time
deposit_queue, deposit_queue_1 = [], []
avg_time = 1


def index(request):
    print(request.session.get('login', False))
    if request.session.get('login', False):
        return render(request, 'detail.html')
    else:
        return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def signout(request):
    print(request.session.get('mobile_no', 'Not username'))
    if request.ses sion.get('login', False) == False:
        return render(request, 'login.html')
    request.session['login'] = False
    return HttpResponse('logout :' + request.session['mobile_no'])


@csrf_exempt
def sign_up(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    mobile_no = int(request.POST['mobile_no'])

    try:
        user = models.User(first_name=first_name, last_name=last_name,
                           password=password, mobile_no=mobile_no)
        user.save()
        return render(request, 'login.html')

    except:
        return HttpResponse('user_exsist')
        print("user exsist")


@csrf_exempt
def sign_in(request):
    mobile_no = request.POST['mobile_no']
    password = request.POST['password']
    auth = models.User.objects(mobile_no=mobile_no)
    sess = request.session.get('login', False)
    print(sess)
    if sess:
        return render(request, 'detail.html')

    if len(auth) != 0:
        if auth[0].password == password:
            request.session['mobile_no'] = mobile_no
            request.session['login'] = True
            print(request.session['mobile_no'], request.session['login'])
            return render(request, 'detail.html')
        else:
            return render(request, 'password_error.html')
    else:
        return render(request, 'username_error.html')


@csrf_exempt
def create_ticket(request):
    # print(request.session['mobile_no'])
    global deposit_queue
    customer_id = request.POST['customer_id']
    type_transcation = request.POST['type_transcation']
    responese_time = datetime.datetime.now()
    resolved_time = datetime.datetime.now()
    counter_id = 999
    ETA = datetime.datetime.now() + datetime.timedelta(minutes=len(deposit_queue)
                                                       * avg_time + 1)
    expire_time = datetime.datetime.now() + datetime.timedelta(minutes=len(deposit_queue)
                                                               * avg_time) + datetime.timedelta(minutes=2)
    active = 1
    ticket = models.Ticket(customer_id=models.User.objects(mobile_no=8596025075)[0].id, type_transcation=type_transcation, responese_time=responese_time,
                           resolved_time=resolved_time, counter_id=counter_id, ETA=ETA, expire_time=expire_time, active=active)
    # ticket.save()
    try:
        ticket.save()
        deposit_queue.append([ticket.id, ticket.responese_time, ticket.ETA])
        print(deposit_queue)
        return HttpResponse('Successfull ' + ticket.id)
    except:
        return HttpResponse('Failed')


@csrf_exempt
def check_queue(request):
    global deposit_queue, deposit_queue_1
    deposit_queue = sorted(deposit_queue, key=lambda x: x[1])
    print(deposit_queue)
    diff = deposit_queue[0][1] - datetime.datetime.now()
    for i in range(len(deposit_queue)):
        time_diff = deposit_queue[i][2] < datetime.datetime.now()
        print(time_diff)
        if time_diff:
            print(deposit_queue[i][0])
            tt = models.Ticket.objects(id=deposit_queue[i][0])
            tt.update(active=0)
            print(deposit_queue.pop(i))
            break

    if diff.seconds // 60 < 3:
        ticket = models.Ticket(id=deposit_queue[0][0])[0]
        customer = models.User.objects(id=ticket.customer_id)
        print("User Named " + customer.first_name + " " + customer.last_name)
        deposit_queue = deposit_queue[1:]
        deposit_queue_1.append(ticket.id)
        avg_time = 1
        print(len(deposit_queue_1))
        return HttpResponse("User Named " + customer.first_name + " " + customer.last_name + " " + ticket.ETA.strftime("%m/%d/%Y, %H:%M:%S"))
    return HttpResponse(deposit_queue)


@csrf_exempt
def clear_ticket(request):
    global deposit_queue
    ticket = request.POST['ticket']
    tt = models.Ticket.objects(id=ticket)[0]
    # deposit_queue.remove(tt.id)
    print(tt.id)
    j = 0
    for i in range(len(deposit_queue)):
        if deposit_queue[i][0] == tt.id:
            j = i

    print(deposit_queue.pop(j))

    # tt.active = 0
    # tt.resolved_time = datetime.datetime.now()
    tt.update(active=0, resolved_time=datetime.datetime.now())
    print("Processed ticket =" + str(tt.id))
    return HttpResponse("Processed ticket =" + tt.id)
