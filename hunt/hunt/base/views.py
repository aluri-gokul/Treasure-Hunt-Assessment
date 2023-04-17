from django.shortcuts import render,redirect
from .models import Clues,Users,ScoreAndTime
from django.contrib.auth.hashers import make_password, check_password




# from datetime import datetime
import time
import math

def view404(request,exception):
    return render(request, '404.html',{"err":exception})


def opps(request):
    if not request.session.has_key('user'):
        return redirect('/login/')
    if request.session.has_key('clueid'):
        if request.session['clueid'] == 9 or request.session['clueid'] == 10:
            return render(request,'opps.html',{"clue":"Opps!!! you got Trapped.. It was a trap setup by the king. It seems the question had other answers too which we were unable to figure out. Oh Nooo! the door closed, we are now trapped in this room forever... :("})
    return redirect('/gamest/')
    # return render(request,'opps.html',{"clue":"Opps!!! you got Trapped.. It was a trap setup by thief. It seems the question had other answer too which you were unable to figure out.Wait! its the owner's call.(After talking) Damn it!! The owner just told me that the thief left the country and we cant do anything now... :("})



def update(uemail,uid ,score,time11):
    if(uid == 1):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl1Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl1Tym=time11)
        return True    
    if(uid == 2):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl2Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl2Tym=time11)
        return True
    if(uid == 3):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl3Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl3Tym=time11)
        return True 
    if(uid == 4):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl4Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl4Tym=time11)
        return True 
    if(uid == 5):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl5Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl5Tym=time11)
        return True 
    if(uid == 6):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl6Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl6Tym=time11)
        return True 
    if(uid == 7):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl7Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl7Tym=time11)
        return True 
    if(uid == 8):
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl8Scr=score)
        ScoreAndTime.objects.filter(userEmail=uemail).update(cl8Tym=time11)
        return True 
    # if(uid == 9):
    #     ScoreAndTime.objects.filter(userEmail=uemail).update(cl9Scr=score)
    #     ScoreAndTime.objects.filter(userEmail=uemail).update(cl9Tym=time11)
    #     return True 
    # if(uid == 10):
    #     ScoreAndTime.objects.filter(userEmail=uemail).update(cl0Scr=score)
    #     ScoreAndTime.objects.filter(userEmail=uemail).update(cl0Tym=time11)
        return True  
       
    
    return False

# Create your views here.

def home(request):
    if request.session.has_key("clueid"):
        del request.session["clueid"]
    if request.session.has_key("score"):
        del request.session["score"]
    if request.session.has_key("sttime"):
        del request.session["sttime"]
    if request.session.has_key("echtime"):
        del request.session["echtime"]

    cont = {"name" : False}
    if request.session.has_key("user"):
        cont = {"name": request.session["user"]}
    return render(request, 'index.html',cont)

def login(request):

    admun = 'admin@hunt.com'
    admp = 'detective@admin'

    if request.session.has_key("adm"):
        return redirect('/adm/')

    if request.session.has_key('user'):
        return redirect('/game/')

    if request.method == 'POST':
        uemail = request.POST.get('uemail')
        passw = request.POST.get('upass')
        lst = Users.objects.filter(userEmail=uemail)

        if uemail == admun:
            if passw == admp:
                request.session["adm"] = admun
                return redirect('/adm/')

        if lst:
            lst = lst.first()
            # print(check_password(passw, lst.userPass))
            if check_password(passw, lst.userPass):
                 request.session['user'] = lst.userName
                 request.session['uemail'] = lst.userEmail
                 us = ScoreAndTime(userEmail=lst.userEmail)
                 us.save()
                 return redirect('/game/')
            else:
                 return render(request, 'login.html', {"msg": "Incorrect Password"})
        else:
            return render(request, 'login.html', {"msg":"Email address not found.. Please sign up!"})
    return render(request, 'login.html')

def signup(request):
    if request.session.has_key('user'):
        return render('/game/')

    if request.method == 'POST':
        uname = request.POST.get('uname').title()
        uemail = request.POST.get('uemail').lower()
        upass = make_password(request.POST.get('upass'))
        lst = Users.objects.filter(userEmail=uemail)
        if lst or lst.count() > 0:
            return render(request, 'signup.html',{"msg":"You already have an account... please Login!"})
        else:
            us = Users(userEmail=uemail,userPass=upass,userName=uname)
            us.save()
            return redirect('/login/')

              

    return render(request, 'signup.html')

def game(request):
    if not request.session.has_key('user'):
        return redirect('/login/')
    usname = request.session['user']
    uemail = request.session['uemail']
    usr = Users.objects.filter(userEmail=uemail).first()
    usr.attempts+=1 
    usr.save()
    
    if request.session.has_key('clueid'):
        return redirect('/gamest/')
    if(not request.session.has_key('clueid')):
        request.session['clueid']  = 1
        request.session['score'] = 0
        request.session['sttime'] = str(time.time())
        request.session['echtime'] = str(time.time())
    
    return render(request, 'game.html', {"name": usname})




def gamest(request):
    if not request.session.has_key('user'):
        return redirect('/login/')
    uemail = request.session['uemail']
    usr = Users.objects.filter(userEmail=uemail).first()
    if(not request.session.has_key('clueid')):
         request.session['clueid']=1
         request.session['score'] = 0
         request.session['sttime'] = str(time.time())
         request.session['echtime'] = str(time.time())
    psk = request.session['clueid']-1
    lst= Clues.objects.all()

    if request.method=="POST":
         ans = request.POST['clueans']
         print(psk)
         if psk == 4:
             print(psk)
             ans1 = "1.6"
             if ans.lower().strip() == ans1.lower().strip():
                 time1 = round(time.time() -  float(request.session['echtime']))
                 t1 = math.floor(time1/60)
            # time1 = time1 if time1 > 0 else 1
            # print(time1)
                 t1 = t1 if t1>0 else 1
                 score = math.ceil(lst[psk].score / t1)
            # print(score)
                 time1 = str(math.floor(time1/60)).rjust(2,'0') + ":" + str(time1%60).rjust(2,'0')
                 score = score if score >= 5 else 5
                 request.session['score'] = int(request.session['score']) + score
            # usr.update(scoreAndTime__ = {{request.session['clueid']:'solved', 'score':score,'time':time1}})
            # usr.scoreAndTime[request.session['clueid']] = json.dumps(dict(score =score, time=time))
                 update(uemail,request.session['clueid'],score,time1)
                 request.session['clueid'] = 9
                 psk=int(request.session['clueid'])-1
                 request.session['echtime'] = str(time.time())
                 return render(request, 'gamest.html', {"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid,"hurray":"correct"})
             
             elif ans.lower().strip() ==  lst[psk].answer.lower():
                 time1 = round(time.time() -  float(request.session['echtime']))
                 t1 = math.floor(time1/60)
            # time1 = time1 if time1 > 0 else 1
            # print(time1)
                 t1 = t1 if t1>0 else 1
                 score = math.ceil(lst[psk].score / t1)
            # print(score)
                 time1 = str(math.floor(time1/60)).rjust(2,'0') + ":" + str(time1%60).rjust(2,'0')
                 score = score if score >= 5 else 5
                 request.session['score'] = int(request.session['score']) + score
            # usr.update(scoreAndTime__ = {{request.session['clueid']:'solved', 'score':score,'time':time1}})
            # usr.scoreAndTime[request.session['clueid']] = json.dumps(dict(score =score, time=time))
                 update(uemail,request.session['clueid'],score,time1)
                 request.session['clueid'] = int(request.session['clueid'])+1
                 psk=int(request.session['clueid'])-1
                 request.session['echtime'] = str(time.time())
                 return render(request, 'gamest.html', {"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid,"hurray":"correct"})
             else:
                 request.session['echtime'] = str(time.time())
                 return render(request, 'gamest.html',{"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid, "error":"wrong answer"})

        
         elif psk == 5:
             print(psk)
             ans1 = "1.5"
             if ans.lower().strip() == ans1.lower().strip():
                 time1 = round(time.time() -  float(request.session['echtime']))
                 t1 = math.floor(time1/60)
            # time1 = time1 if time1 > 0 else 1
            # print(time1)
                 t1 = t1 if t1>0 else 1
                 score = math.ceil(lst[psk].score / t1)
            # print(score)
                 time1 = str(math.floor(time1/60)).rjust(2,'0') + ":" + str(time1%60).rjust(2,'0')
                 score = score if score >= 5 else 5
                 request.session['score'] = int(request.session['score']) + score
            # usr.update(scoreAndTime__ = {{request.session['clueid']:'solved', 'score':score,'time':time1}})
            # usr.scoreAndTime[request.session['clueid']] = json.dumps(dict(score =score, time=time))
                 update(uemail,request.session['clueid'],score,time1)
                 request.session['clueid'] = 10
                 psk=int(request.session['clueid'])-1
                 request.session['echtime'] = str(time.time())
                 return render(request, 'gamest.html', {"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid,"hurray":"correct"})
             
             elif ans.lower().strip() ==  lst[psk].answer.lower():
                 time1 = round(time.time() -  float(request.session['echtime']))
                 t1 = math.floor(time1/60)
            # time1 = time1 if time1 > 0 else 1
            # print(time1)
                 t1 = t1 if t1>0 else 1
                 score = math.ceil(lst[psk].score / t1)
            # print(score)
                 time1 = str(math.floor(time1/60)).rjust(2,'0') + ":" + str(time1%60).rjust(2,'0')
                 score = score if score >= 5 else 5
                 request.session['score'] = int(request.session['score']) + score
            # usr.update(scoreAndTime__ = {{request.session['clueid']:'solved', 'score':score,'time':time1}})
            # usr.scoreAndTime[request.session['clueid']] = json.dumps(dict(score =score, time=time))
                 update(uemail,request.session['clueid'],score,time1)
                 request.session['clueid'] = int(request.session['clueid'])+1
                 psk=int(request.session['clueid'])-1
                 request.session['echtime'] = str(time.time())
                 return render(request, 'gamest.html', {"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid,"hurray":"correct","hint":"golden Frame"})
             else:
                 request.session['echtime'] = str(time.time())
                 return render(request, 'gamest.html',{"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid, "error":"wrong answer"})


         elif ans.lower().strip() == lst[psk].answer.lower():
            
            time1 = round(time.time() -  float(request.session['echtime']))
            t1 = math.floor(time1/60)
            # time1 = time1 if time1 > 0 else 1
            # print(time1)
            t1 = t1 if t1>0 else 1
            score = math.ceil(lst[psk].score / t1)
            # print(score)
            time1 = str(math.floor(time1/60)).rjust(2,'0') + ":" + str(time1%60).rjust(2,'0')
            score = score if score >= 5 else 5
            request.session['score'] = int(request.session['score']) + score
            # usr.update(scoreAndTime__ = {{request.session['clueid']:'solved', 'score':score,'time':time1}})
            # usr.scoreAndTime[request.session['clueid']] = json.dumps(dict(score =score, time=time))
            update(uemail,request.session['clueid'],score,time1)
            

            request.session['clueid'] = request.session['clueid']+1
            psk=int(request.session['clueid'])-1
            request.session['echtime'] = str(time.time())
            
            if psk == 9 or psk == 10:
                return redirect('/opps/')

            
            if psk == 8:
                 request.session['echtime'] = str(time.time())
                 totaltime = round(time.time() - float(request.session['sttime']))
                 totaltime  = str(math.floor(totaltime/60)).rjust(2,'0') + ":" + str(totaltime%60).rjust(2,'0')
                 totalscore = int(request.session['score'])
                #  usr.update(totalScore=totalscore, totalTime=totaltime)
                 usr.totalScore = totalscore
                 usr.totalTime = totaltime
                 usr.save()
                 request.session['echtime'] = str(time.time())
                 return redirect('/last/')
            return render(request, 'gamest.html', {"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid,"hurray":"correct"}) 
         else:
             return render(request,'gamest.html',{"clue": lst[psk].clue, "score": lst[psk].score, "tid": lst[psk].clueid,"error":"Wrong answer"})



    
    lstt = lst[psk]

    cont = {"clue" : lstt.clue, "score" : lstt.score, "tid" : lstt.clueid}
    request.session['echtime'] = str(time.time())
    return render(request, 'gamest.html', cont)



def restart(request):
    if (not request.session.has_key('user')) and (not request.session.has_key('adm')):
        return redirect('/login/')
    if request.session.has_key("clueid"):
        del request.session["clueid"]
    if request.session.has_key("score"):
        del request.session["score"]
    if request.session.has_key("sttime"):
        del request.session["sttime"]
    if request.session.has_key("echtime"):
        del request.session["echtime"]
    return redirect("/game/")


def logout(request):
    # request.session.clear()
    if (not request.session.has_key('user')) and (not request.session.has_key('adm')):
        return redirect('/login/')
    if request.session.has_key("clueid"):
        del request.session["clueid"]
    if request.session.has_key("score"):
        del request.session["score"]
    if request.session.has_key("sttime"):
        del request.session["sttime"]
    if request.session.has_key("user"):
        del request.session["user"]
    if request.session.has_key("uemail"):
        del request.session["uemail"]
    if request.session.has_key("echtime"):
        del request.session["echtime"]
    if request.session.has_key("adm"):
        del request.session["adm"]
    return redirect('/home/')



def winner(request):
     if not request.session.has_key("clueid"):
         return redirect('/gamest/')
     else:
         if not request.session['clueid'] == 9:
             return redirect('/gamest/')
     if not request.session.has_key("user"):
         return redirect("/login/")
     uemail = request.session['uemail']
     usr=  Users.objects.filter(userEmail=uemail).first()
     sc = usr.totalScore
     na = usr.userName
     return render(request, 'winner.html', {"name":na,"score":sc})

def last(request):
    if not request.session.has_key('user'):
        return redirect('/login/')
    if not request.session.has_key('clueid'):
        return redirect('/game/')
    if request.session.has_key('clueid'):
        if not request.session['clueid'] == 9:
            # return render(request,'opps.html',{"clue":"Opps!!! you got Trapped.. It was a trap setup by thief. It seems the question had other answer too which you were unable to figure out.Wait! its the owner's call.(After talking) Damn it!! The owner just told me that the thief left the country and we cant do anything now... :("})
            return redirect('/gamest/')
    return render(request, "last.html")




def adm(request):
    admun = 'admin@hunt.com'
    if not request.session.has_key('adm'):
        return redirect('/home/')

    if not request.session['adm'] == admun:
        return redirect('/home/')
    usrdata = Users.objects.all().order_by('totalScore')

    data = {}
    i = 1
    for usr in usrdata:
        data[i] = (usr.userEmail,usr.userName, usr.totalScore, usr.totalTime, usr.attempts)
        i+=1
    if data == {}:
        val = False
    else:
        val = True
    # srn = [i for i in range(1,len(data.keys())+1)]
    # print(srn)
    return render(request, "adm.html",{"data":val,"value":data})

def usrstats(request,pk):
    admun = 'admin@hunt.com'
    if not request.session.has_key('adm'):
        return redirect('/home/')

    if not request.session['adm'] == admun:
        return redirect('/home/')
    userD = ScoreAndTime.objects.filter(userEmail = pk).first()
    data = {}
    if userD:
        data[userD.userEmail] = [(1,userD.cl1Scr, userD.cl1Tym), (2,userD.cl2Scr, userD.cl2Tym),(3,userD.cl3Scr, userD.cl3Tym),(4,userD.cl4Scr, userD.cl4Tym),(5,userD.cl5Scr, userD.cl5Tym),(6,userD.cl6Scr, userD.cl6Tym),(7,userD.cl7Scr, userD.cl7Tym),(8,userD.cl8Scr, userD.cl8Tym)]
    else:
        return redirect('/adm/')
    val = True
    if data == {}:
        val = False

    ur = Users.objects.filter(userEmail = pk).first()
    name = ur.userName
    totalscore = ur.totalScore
    return render(request, "usrstats.html",{"d":val, "value":data,"name":name,"totalscore": totalscore})

