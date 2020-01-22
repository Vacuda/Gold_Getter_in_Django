from django.shortcuts import render, redirect, HttpResponse
import random, datetime

########################

def getRandom(min,max):
    amount=random.randint(min,max)
    return amount

context={
    "actArr":[]
}

########################


def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0

    return render(request,'gold_app/index.html', context)
    
###RESET BUTTON
def reset(request):
    request.session['gold']=0
    global context
    context['actArr']=[]
    return redirect('/')
   
# ##GET RANDOM, CHANGE GOLD, CHANGE PLACE
# def process(request):
#     amount=getRandom(int(request.POST['min']),int(request.POST['max']))
#     request.session['gold']=request.session['gold'] + amount
#     ##BUILD STRING
#     now=datetime.datetime.now()
#     timestamp=now.strftime("%m/%d/%Y, %I:%M:%S %p")
#     if amount >= 0:
#         new_activity="<p style='color:green;'>Earned " + str(amount) + " golds from the " + request.POST['place'] + "! (" + timestamp + ")</p>"
#     else:
#         new_activity="<p style='color:red;'>Entered a casino and lost " + str(abs(amount)) + " golds... OUCH... (" + timestamp + ")</p>"
#     ##ADD TO ARRAY
#     global context
#     context['actArr'].append(new_activity)

#     return redirect('/')



####Code reconfigured to pass var place through the url instead of a hidden input
##GET RANDOM, CHANGE GOLD, CHANGE PLACE
def process(request, place):
    amount=getRandom(int(request.POST['min']),int(request.POST['max']))
    request.session['gold']=request.session['gold'] + amount
    # request.session['place']=place
    ##BUILD STRING
    now=datetime.datetime.now()
    timestamp=now.strftime("%m/%d/%Y, %I:%M:%S %p")
    if amount >= 0:
        new_activity="<p style='color:green;'>Earned " + str(amount) + " golds from the " + place + "! (" + timestamp + ")</p>"
    else:
        new_activity="<p style='color:red;'>Entered a casino and lost " + str(abs(amount)) + " golds... OUCH... (" + timestamp + ")</p>"
    ##ADD TO ARRAY
    global context
    context['actArr'].append(new_activity)

    return redirect('/')