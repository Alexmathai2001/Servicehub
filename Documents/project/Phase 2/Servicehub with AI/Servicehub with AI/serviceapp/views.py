from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.files.storage import FileSystemStorage
import webbrowser
import datetime
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import random
import MySQLdb
db=MySQLdb.connect("localhost","root","","servicehub")
c=db.cursor()


def login(request):
    msg=""
    if request.POST:
        uname=request.POST.get("email")
        password=request.POST.get("password")
       
        request.session['uname']=uname
        print(uname)
        print(password)
        query="select * from login where uname='"+str(uname)+"' and password='"+str(password)+"'"
        c.execute(query)
        data=c.fetchone()
        print(data)
        if data:
            if data[2]=='admin':
                return HttpResponseRedirect("/adminhome/")
            elif data[2]=='servicecenter':
                if data[3]=="approved":
                    c.execute("select scid from screg where email='"+str(request.session['uname'])+"'")
                    owner=c.fetchone()
                    request.session['scid']=owner[0]
                    return HttpResponseRedirect("/schome/")
                else:
                    msg="WAIT FOR ADMIN APPROVAL.."
           


                    return render(request,"common/login.html",{"msg":msg})




            elif data[2]=='user' and data[3]=="approved":
                print("hello")
                a="select uid from userreg where email='"+str(uname)+"'"
                c.execute(a)
                userid=c.fetchone()
                print(a)
                print(userid)
                request.session['userid']=userid[0]
                return HttpResponseRedirect("/userhome/")
        else:
            msg="invalid username or password"
           


    return render(request,"common/login.html",{"msg":msg})




def index(request):
    return render(request,"common/index.html")

def adminhome(request):
    return render(request,"admin/adminhome.html")
def schome(request):
    return render(request,"sc/schome.html")
def userhome(request):
    return render(request,"user/userhome.html")

def adminbase(request):
    return render(request,"admin/adminbase.html")






def userreg(request):
    

    msg=""
    word=""
    if request.POST:
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        phoneno=request.POST.get("phoneno")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if password==cpassword:
            status='approved'
            qq="select count(*) from userreg where email='"+str(email)+"'"
            c.execute(qq)
            data=c.fetchone()
            print(qq)
            print(data)
 
            if int(data[0])<1:
                query="insert into userreg(name,email,address,phoneno) values('"+str(name)+"','"+str(email)+"','"+str(address)+"','"+str(phoneno)+"')"
                print(query)
                c.execute(query)
                db.commit()
                usertype='user'

                qqq="insert into login(uname,password,usertype,status) values('"+str(email)+"','"+str(password)+"','"+str(usertype)+"','"+str(status)+"')"
                c.execute(qqq)
                db.commit()
                msg="Account successfully Created"
            else:
                msg="Allready have an account with same mail id"
        else:
            word="Sorry your password and confirm password are not matching"

        # return HttpResponseRedirect("/index/")
    return render(request,"common/userreg.html",{"msg":msg,"word":word})


def screg(request):
        c.execute("select * from company")
        data=c.fetchall()
        msg=""
        word=""
        if request.POST:
            name=request.POST.get("name")
            email=request.POST.get("email")
            address=request.POST.get("address")
            district=request.POST.get("district")
            phoneno=request.POST.get("phoneno")
            company=request.POST.get("company")
            product=request.POST.get("product")
            aid=request.POST.get("aid")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            if password==cpassword:
                qq="select count(*) from screg where email='"+str(email)+"'"
                c.execute(qq)
                data=c.fetchone()
                print(qq)
                print(data)
                a=data[0]
                print(a)
 
                if int(a)<1:
                    print("hello")
                    status='requested'
                    query="insert into screg(name,email,address,phoneno,company,product,aid,password,district) values('"+str(name)+"','"+str(email)+"','"+str(address)+"','"+str(phoneno)+"','"+str(company)+"','"+str(product)+"','"+str(aid)+"','"+str(password)+"','"+str(district)+"')"
                    c.execute(query)
                    db.commit()
                    print(query)
                    print("hai")
                    usertype='servicecenter'

                    
                    qqq="insert into login(uname,password,usertype,status) values('"+str(email)+"','"+str(password)+"','"+str(usertype)+"','"+str(status)+"')"
                    c.execute(qqq)
                    db.commit()
                    msg="Account successfully Created"
                    #return render(request,"common/screg.html",{"msg":msg})


                else:
                    msg="Allready have an account with same mail id"
                   # return render(request,"common/screg.html",{"msg":msg})
            else:
                word="Sorry your password and confirm password are not matching"

            # return HttpResponseRedirect("/index/")
        return render(request,"common/screg.html",{"msg":msg,"word":word,"data":data})




def addcompany(request):
        if request.POST:
            company=request.POST.get("company")
            if request.FILES["file"]:
                myfile=request.FILES["file"]
                fs=FileSystemStorage()
                filename=fs.save(myfile.name,myfile)
                fileurl=fs.url(filename)
                query="insert into company(companyname,photo) values('"+str(company)+"','"+str(fileurl)+"')"
                c.execute(query)
                db.commit()
        return render(request,"admin/addcompanies.html")


# def addquestion(request):
#         if request.POST:
#             company=request.POST.get("company")
#             product=request.POST.get("product")
#             question=request.POST.get("question")
#             query="insert into question(companyname,product,question) values('"+str(company)+"','"+str(product)+"','"+str(question)+"')"
#             c.execute(query)
#             db.commit()

#         return render(request,"user/question.html")


def addquestionandanswer(request):
        if request.POST:
            company=request.POST.get("company")
            product=request.POST.get("product")
            question=request.POST.get("question")
            answer=request.POST.get("answer")
            query="insert into question(companyname,product,questionn,answer) values('"+str(company)+"','"+str(product)+"','"+str(question)+"','"+str(answer)+"')"
            c.execute(query)
            db.commit()

        return render(request,"sc/answer.html")


def searchforsc(request):
    if request.POST:
        district=request.POST.get("district")
        request.session['district']=district
        company=request.session['company']


        c.execute("select * from screg where district='"+str(district)+"' and company='"+str(company)+"'")
        data=c.fetchall()
        if data:
            request.session['search']=data

            return HttpResponseRedirect('/searchdisplay/') 
        else:
            msg="not registered"
            return render(request,"user/search.html",{"msg":msg})

    return render(request,"user/search.html")


def searchdisplay(request):
        data=request.session['search']
        userid=request.session['userid']

        return render(request,"user/viewservicecenter.html",{"data":data,"userid":userid})




def viewlocation(request):
    if request.GET.get("loc"):
        loc=request.GET.get("loc")


    return render(request,"user/viewlocation.html",{"loc":loc})


def booking(request):
    if request.GET.get("id"):
        idd=request.GET.get("id")


    if request.POST:
            company=request.session['company']
            # product=request.POST.get("product")
            problem=request.POST.get("problem")
            userid=request.session['userid']
            todate=datetime.date.today()
            bookingdate=todate
            enddate=todate + datetime.timedelta(days=7)
            status="complaint registerred"
            query="insert into booking(company,bookingdate,problem,status,userid,scid,enddate) values('"+str(company)+"','"+str(bookingdate)+"','"+str(problem)+"','"+str(status)+"','"+str(userid)+"','"+str(idd)+"','"+str(enddate)+"')"
            c.execute(query)
            db.commit()
            msg="Successfully Booked."
            return render(request,"user/userhome.html",{"msg":msg})
    return render(request,"user/booking.html",{"scid":idd})



def viewquestion(request):
    data=""
    if request.POST:
            company=request.POST.get("company")
            product=request.POST.get("product")
            c.execute("select * from faq where company='"+str(company)+"' and product='"+str(product)+"'")
            data=c.fetchall()
    return render(request,"user/viewquestion.html",{"data":data})
 


def approvesc(request):
    c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='requested'")
    data=c.fetchall()
    if request.GET.get("id"):
        email=request.GET.get("id")
        
        status='approved'
        c.execute("update login set status='"+str(status)+"' where uname='"+str(email)+"'")
        db.commit()
        return HttpResponseRedirect('/approvesc/') 
    return render(request,"admin/approvesc.html",{"data":data})




def viewasc(request):
    c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='requested'")
    data=c.fetchall()
    if data:
        return render(request,"admin/approvesc.html",{"data":data})
    else:
        msg="CURRENTLY YOU DONT HAVE ANY REQUEST"
        return render(request,"admin/adminhome.html",{"msg":msg})



def approvesc(request):
    c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='requested'")
    data=c.fetchall()
    if request.GET.get("id"):
        email=request.GET.get("id")
        
        status='approved'
        c.execute("update login set status='"+str(status)+"' where uname='"+str(email)+"'")
        db.commit()
        return HttpResponseRedirect('/adminhome/') 
    return render(request,"admin/approvesc.html",{"data":data})




def rejectsc(request):
   
    if request.GET.get("id"):
        email=request.GET.get("id")
        
        status='rejected'
        c.execute("update login set status='"+str(status)+"' where uname='"+str(email)+"'")
        db.commit()
        c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='requested'")
        data=c.fetchall()
        return HttpResponseRedirect('/adminhome/') 

        
    return render(request,"admin/approvesc.html",{"data":data})





def viewsc(request):
    c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='approved'")
    data=c.fetchall()
    if request.GET.get("id"):
        email=request.GET.get("id")
        
        status='rejected'
        c.execute("delete from login where uname='"+str(email)+"'")
        db.commit()
        c.execute("delete from screg where email='"+str(email)+"'")
        db.commit()
        c.execute("SELECT screg.* ,login.* from screg join login on screg.email=login.uname where login.status='requested'")
        data=c.fetchall()
        return HttpResponseRedirect('/adminhome/') 

    return render(request,"admin/viewsc.html",{"data":data})


def viewuser(request):
    c.execute("SELECT * from userreg")
    data=c.fetchall()
    return render(request,"admin/viewuser.html",{"data":data})


def newmap(request):
    
    return render(request,"user/newmap.html")



def gallery(request):
    msg=""
    if request.GET.get('id')=='0':
        msg=request.session['msg']
    c.execute("select * from company")
    data=c.fetchall()
    return render(request,"user/gallery.html",{"data":data,"msg":msg})




# def gallery(request):
#     c.execute("select * from company where CustomerName LIKE '%tru%'")
#     data=c.fetchall()
#     return render(request,"user/gallery.html",{"data":data}) 



def wtsurproblem(request):
    data1=[]
    msg=""
    if request.GET.get("id"):
        company=request.GET.get("id")
        request.session['company']=company
        qq="select count(*) from screg where company='"+str(company)+"'"
        c.execute(qq)
        data=c.fetchone()
        print(company)
        if data[0]<1:
            request.session['msg']="sorry  no service hubs are available for this company"
            return HttpResponseRedirect("/gallery/?id=0")
        else:
            msg=request.session['msg']=""

        


    if request.POST:
        question=request.POST.get("question")
        question=question.split(' ')
        print(question)
        for i in question:        
            c.execute("select * from faq where faq LIKE '%"+ i +"%'")
            z=c.fetchall()
            print(z)
            for zz in z:
                if zz not in data1:
                    data1.append(zz)
         
        request.session['answers']=data1

        print(data1)
     
        return HttpResponseRedirect('/viewanswers/') 
    return render(request,"user/question.html",{"data":data1,"msg":msg}) 


def viewanswers(request):
    answers=request.session['answers']
    return render(request,"user/viewanswers.html",{"answers":answers})



def viewbooking(request):

    c.execute("select booking.*,userreg.* from booking join userreg on booking.userid=userreg.uid where scid='"+str(request.session['scid'])+"' and booking.status='complaint registerred' or booking.status='booked' or booking.status='completed'")
    data=c.fetchall()
    print(data)
    if data:
        return render(request,"sc/viewbookings.html",{"data":data})
    else:
        msg="CURRENTLY YOU DONT HAVE ANY BOOKING.."
        return render(request,"sc/schome.html",{"msg":msg})





def viewprebooking(request):

    c.execute("select booking.*,userreg.* from booking join userreg on booking.userid=userreg.uid where scid='"+str(request.session['scid'])+"' and booking.status='delivered' ")
    data=c.fetchall()
    print(data)
    
    return render(request,"sc/viewpbookings.html",{"data":data})



def updatebookingstatus(request):
    if request.GET.get("id"):
        bid=request.GET.get("id")
        c.execute("select * from booking where bid='"+str(bid)+"'")
        data=c.fetchone()
        print(data)
        print(bid)
        print(data[5])
        uid=data[5]
        if data[4]=='complaint registerred':
            c.execute("select * from userreg where uid='"+str(uid)+"'")
            sms=c.fetchone()
            phoneno=sms[4]
            print(phoneno)
        
            print("hello")
            status='booked'
            content="your status of service is- booked"
            c.execute("update booking set status='"+str(status)+"' where bid='"+str(bid)+"'")
            db.commit()
            return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+content+"&mobile="+str(phoneno)+"")
        elif data[4]=='booked':
            status='completed'
            c.execute("select * from userreg where uid='"+str(uid)+"'")
            sms=c.fetchone()
            phoneno=sms[4]
            print(phoneno)
            content="your status of service is -completed servicing"
            c.execute("update booking set status='"+str(status)+"' where bid='"+str(bid)+"'")
            db.commit()
            return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+content+"&mobile="+str(phoneno)+"")

            
            
        elif data[4]=='completed':
            status='delivered'
            c.execute("select * from userreg where uid='"+str(uid)+"'")
            sms=c.fetchone()
            phoneno=sms[4]
            print(phoneno)
            content="your status of service is- delivered"
            c.execute("update booking set status='"+str(status)+"' where bid='"+str(bid)+"'")
            db.commit()
        
            

            return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+content+"&mobile="+str(phoneno)+"")
        # elif data[4]=='delivered':
        #     c.execute("delete from booking where bid='"+str(bid)+"'")
        #     db.commit()

            
        #return HttpResponseRedirect('/viewbooking/') 
    return render(request,"sc/viewbookings.html")





def viewstatusbyuser(request):

    c.execute("select * from booking where userid='"+str(request.session['userid'])+"'")
    data=c.fetchall()

    return render(request,"user/viewstatus.html",{"data":data})


def feedbackpreview(request):
    c.execute("SELECT booking.* ,screg.* from screg join booking on screg.scid=booking.scid where booking.userid='"+str(request.session['userid'])+"' and booking.status='delivered'")
    data1=c.fetchall()
    if data1:
        return render(request,"user/feedbackpreview.html",{"data":data1})
    else:
        msg="YOU CANNOT ADD FEEDBACK UNTIL YOUR PRODUCT IS DELIVERED"
        return render(request,"user/userhome.html",{"msg":msg})




    


def feedback(request):
    idd=""
    if request.GET.get("id"):
        idd=request.GET.get("id")
        print(idd)  
    if request.POST: 
        servicecenter=request.POST.get("servicecenter")
        feedback=request.POST.get("feedback")
        userid=request.session['userid']
        query="insert into feedback(feedback,userid,scid) values('"+str(feedback)+"','"+str(userid)+"','"+str(idd)+"')"
        c.execute(query)
        db.commit()
    return render(request,"user/feedback.html")



def viewfeedbackbyadmin(request):
    c.execute("SELECT screg.* ,feedback.*,userreg.* from screg join feedback on screg.scid=feedback.scid join userreg  on userreg.uid=feedback.userid")

    data=c.fetchall()
    print(data)

    return render(request,"admin/viewfeedbackbyadmin .html",{"data":data})











def viewfeedbackbysc(request):

    # c.execute("select * from feedback where scid='"+str(request.session['scid'])+"'")
    c.execute("SELECT userreg.* ,feedback.* from userreg join feedback on userreg.uid=feedback.userid where feedback.scid='"+str(request.session['scid'])+"'")
    data=c.fetchall()
    if data:

        return render(request,"sc/viewfeedbackbysc.html",{"data":data})
    else:
        msg="CURRENTLY YOU DONT HAVE ANY FEEDBACK.."
        return render(request,"sc/schome.html",{"msg":msg})


def faq(request):
        if request.POST:
            company=request.POST.get("company")
            faq=request.POST.get("question")
            answer=request.POST.get("answer")
            query="insert into faq(company,faq,answer) values('"+str(company)+"','"+str(faq)+"','"+str(answer)+"')"
            c.execute(query)
            db.commit()
        return render(request,"sc/faq.html")


def viewfaq(request):

    # c.execute("select * from feedback where scid='"+str(request.session['scid'])+"'")
    c.execute("select * from faq")
    data=c.fetchall()

    return render(request,"user/viewfaq.html",{"data":data})


def adminaddmessage(request):
    c.execute("select * from screg")
    data=c.fetchall()
    c.execute("select * from userreg")
    data1=c.fetchall()
    if request.POST:
        message=request.POST.get("message")
        recepient=request.POST.get("reciepient")
        messenger=request.session["uname"]
        qq="insert into message(message,messenger,recipient) values('"+str(message)+"','"+str(messenger)+"','"+str(recepient)+"')"
        c.execute(qq)
        db.commit()
    return render(request,"admin/addmessage.html",{"data":data,"data1":data1})

def scaddmessage(request):
    c.execute("select * from userreg")
    data1=c.fetchall()
    if request.POST:
        message=request.POST.get("message")
        recepient=request.POST.get("reciepient")
        messenger=request.session["uname"]
        qq="insert into message(message,messenger,recipient) values('"+str(message)+"','"+str(messenger)+"','"+str(recepient)+"')"
        c.execute(qq)
        db.commit()
    return render(request,"sc/scaddmessage.html",{"data1":data1})


def useraddmessage(request):
    c.execute("select * from screg")
    data1=c.fetchall()
    if request.POST:
        message=request.POST.get("message")
        recepient=request.POST.get("reciepient")
        messenger=request.session["uname"]
        qq="insert into message(message,messenger,recipient) values('"+str(message)+"','"+str(messenger)+"','"+str(recepient)+"')"
        c.execute(qq)
        db.commit()
    return render(request,"user/useraddmessage.html",{"data1":data1})




def adminviewmessage(request):
    c.execute("select * from message where recipient='admin@gmail.com'")
    data=c.fetchall()
    if data:
        return render(request,"admin/adminviewmessages.html",{"data":data})
    else:
        msg="CURRENTLY YOU DONT HAVE ANY MESSAGES TO VIEW"
        return render(request,"admin/adminhome.html",{"msg":msg})


def scviewmessage(request):
    print(request.session["uname"])
    c.execute("select * from message where recipient='"+str(request.session["uname"])+"'")
    data=c.fetchall()
    
    if data:
        return render(request,"sc/scviewmessage.html",{"data":data})

    else:
        msg="CURRENTLY YOU DONT HAVE ANY MESSAGES TO VIEW"
        return render(request,"sc/schome.html",{"msg":msg})

    
def userviewmessage(request):
    c.execute("select * from message where recipient='"+str(request.session["uname"])+"'")
    data=c.fetchall()
    
    if data:
        return render(request,"user/userviewmessage.html",{"data":data})
    else:
        msg="CURRENTLY YOU DONT HAVE ANY MESSAGES TO VIEW"
        return render(request,"user/userhome.html",{"msg":msg})

    


def viewupcomings(request):
    todate=datetime.date.today()
    enddate=todate + datetime.timedelta(days=5)
    c.execute("select * from booking where enddate<='"+str(enddate)+"' and scid='"+str(request.session["scid"])+"'")
    data=c.fetchall()
    return render(request,"sc/upcomingdates.html",{"data":data})



def adminviewreport(request):
   
    # select *from selectAllEntriesDemo where month(ShippingDate)=2;

    return render(request,"admin/adminviewbooking.html",{"data":data})








# Pie Chart
def piechart(request):
    data=[]
    s1=[]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    c.execute("select DISTINCT monthname(bookingdate) from booking")
    data11=c.fetchall()
    for i in data11:
        for j in i:
            print(j)
            s1.append(j)
        print(i)
    print(data11)
    data11=s1
    labels = 'Sale', 'Purchase'
    c.execute("select count(*) from booking group by month(bookingdate)")
    data=c.fetchall()
    s=[]
    for i in data:
        for j in i:
            print(j)
            s.append(j)

        print(i)
    print(s)
    data=s
    print("*"*50)
   
    explode=[ 0 for i in data]
    print(explode)
    print("*"*50)
    
   
    # explode = (0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(data,explode=explode,  labels=data11, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Pie Chart")
    plt.show()
    
    # sizes = [random.randint(10,30), random.randint(30,50)]
    # explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # plt.savefig('media/sale_purchase_peichart.png',dpi=100)
    
    
    
    plt.plot(data11,data)
    plt.title("Pie chart")
    plt.show()
    return HttpResponseRedirect('/adminhome')


def chatbot(request):
    # import train_chatbot
    import chatgui
    return HttpResponseRedirect('/index')