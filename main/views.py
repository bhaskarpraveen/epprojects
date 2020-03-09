from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail
# Create your views here.
def Main(request):
    if request.method == 'POST':
        checkTeamName = Detail.objects.filter(team_name=request.POST['teamname'])
        if(checkTeamName):
            return HttpResponse("Team Name already exists")
        checkAb = Detail.objects.filter(project_id=request.POST['problem']).count()
        if(checkAb==2):
            return HttpResponse("Project is not available")
        OneCheck1= Detail.objects.filter(member1=request.POST['member1'])
        OneCheck2=Detail.objects.filter(member2=request.POST['member1'])
        OneCheck3=Detail.objects.filter(member3=request.POST['member1'])
        OneCheck4=Detail.objects.filter(member4=request.POST['member1'])
        OneCheck5=Detail.objects.filter(member5=request.POST['member1'])
        if(OneCheck1 or OneCheck2 or OneCheck3 or OneCheck4 or OneCheck5):
            return HttpResponse("Member one is already in another team")
        TwoCheck1= Detail.objects.filter(member1=request.POST['member2'])
        TwoCheck2=Detail.objects.filter(member2=request.POST['member2'])
        TwoCheck3=Detail.objects.filter(member3=request.POST['member2'])
        TwoCheck4=Detail.objects.filter(member4=request.POST['member2'])
        TwoCheck5=Detail.objects.filter(member5=request.POST['member2'])
        if(TwoCheck1 or TwoCheck2 or TwoCheck3 or TwoCheck4 or TwoCheck5):
            return HttpResponse("Member Two is already in another team")
        ThreeCheck1= Detail.objects.filter(member1=request.POST['member3'])
        ThreeCheck2=Detail.objects.filter(member2=request.POST['member3'])
        ThreeCheck3=Detail.objects.filter(member3=request.POST['member3'])
        ThreeCheck4=Detail.objects.filter(member4=request.POST['member3'])
        ThreeCheck5=Detail.objects.filter(member5=request.POST['member3'])
        if(ThreeCheck1 or ThreeCheck2 or ThreeCheck3 or ThreeCheck4 or ThreeCheck5):
            return HttpResponse("Member Three is already in another team")
        fourCheck1= Detail.objects.filter(member1=request.POST['member4'])
        fourCheck2=Detail.objects.filter(member2=request.POST['member4'])
        fourCheck3=Detail.objects.filter(member3=request.POST['member4'])
        fourCheck4=Detail.objects.filter(member4=request.POST['member4'])
        fourCheck5=Detail.objects.filter(member5=request.POST['member4'])
        if(fourCheck1 or fourCheck2 or fourCheck3 or fourCheck4 or fourCheck5):
            return HttpResponse("Member four is already in another team")
        fiveCheck1= Detail.objects.filter(member1=request.POST['member5'])
        fiveCheck2=Detail.objects.filter(member2=request.POST['member5'])
        fiveCheck3=Detail.objects.filter(member3=request.POST['member5'])
        fiveCheck4=Detail.objects.filter(member4=request.POST['member5'])
        fiveCheck5=Detail.objects.filter(member5=request.POST['member5'])
        if(fiveCheck1 or fiveCheck2 or fiveCheck3 or fiveCheck4 or fiveCheck5):
            return HttpResponse("Member five is already in another team")
        
        det=Detail()
        
        det.team_name=request.POST['teamname']
        det.project_id=request.POST['problem']
        det.member1=request.POST['member1']
        det.member2=request.POST['member2']
        det.member3=request.POST['member3']
        det.member4=request.POST['member4']
        det.member5=request.POST['member5']
     
        det.save()

        return HttpResponse(" Your team is successfully registered")
        
        
        
    return render(request,'index.html',{})