from django.shortcuts import render

# Create your views here.
from company.models import Company, Campaign, POIJobs, POI, POIInterests


def get_campaign(request):
    order_by = request.GET.get('order_by', '')
    print(order_by)

    order_by_name = order_by.split(' ')[1]
    print(order_by_name)
    order_by_sign = order_by.split(' ')[0]
    order_by_sign = '' if order_by_sign == 'asc' else '-'
    print(order_by_sign)
    queryset = Campaign.objects.order_by(order_by_sign + order_by_name)
    return render(request, 'index.html', context={'queryset': queryset})
    # else:
    #     print('blah')
    #     queryset = Campaign.objects.all()
    #     return render(request, 'index.html', context={'queryset':queryset})


def add_poi(request):
    if request.method == "POST":
        point = request.POST.get('point')
        poi_type = request.POST.get('point')
        poi_sector = request.POST.get('poi_sector')
        poi_job = request.POST.get('poi_job')
        poi_interests = request.POST.get('poi_interests')

        jobs_name = [x.title for x in POIJobs.objects.all()]
        intrest_name = [x.title for x in POIInterests.objects.all()]
        jobs_id = []
        intrests_id = []
        for x in jobs_name:
            jobs_id.append(int(request.POST.get('poi_job'))) if request.POST.get(x) else print("none")

        poi = POI.objects.create('')
        for x in jobs_id:
            poi.poi_job.add(POIJobs.objects.get(id=x))

        for j in intrests_id:
            poi.poi_job.add(POIInterests.objects.get(id=j))

        poi.save()
        print(jobs_id)
