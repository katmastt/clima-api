from django.http import HttpResponse
from api.models import OndemandRequest
from api.models import Project
import requests
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def remaining_jobs(request, id):

    if request.method == 'POST':
        try:
            received_json_data = json.loads(request.body)
        except:
            response = {"Error: no data provided\n"}
            return HttpResponse(response)
        req_ram = received_json_data["ram"]
        req_cpu = received_json_data["cores"]
       
        try:
            project_obj = Project.objects.get(id=id)
        except:
            response = {"Error: project does not exist\n"}
            return HttpResponse(response)

        #if the project is deleted, expired, rejected or pending return 0s
        if (project_obj.status == -4 or project_obj.status == -5 or project_obj.status == -1 or project_obj.status == 0):
            response = {"Error: project is not valid\n"}
            return HttpResponse(response)
            
        latest_project_request = project_obj.latest_project_request_id
        on_demand_obj = OndemandRequest.objects.get(request_id=latest_project_request)
        project_jobs = on_demand_obj.num_of_jobs 
        project_name = project_obj.name
        project_cpu = on_demand_obj.cores
        project_ram = on_demand_obj.ram

        if (project_cpu < int(req_cpu) or project_ram < int(req_ram)):
            response = {"response":"Request denied", "initial_jobs":project_jobs, "remaining_jobs":project_jobs, "cpu":project_cpu, "ram":project_ram}
            response_json = json.dumps(response)
            return HttpResponse(response_json)

        data = {'project':project_name}
        r = requests.get('https://hypatia-comp.athenarc.gr/index.php?r=api/project-usage', params=data)
        usage = r.text

        if usage == "false":
            response = {"response":"Request granded", "initial_jobs":project_jobs, "remaining_jobs":project_jobs, "cpu":project_cpu, "ram":project_ram}
            response_json = json.dumps(response)
            return HttpResponse(response_json)
        
        else:
            tmp = usage.split(',')[0]
            used_jobs = tmp.split(':')[1]
            remaining_jobs = project_jobs - int(used_jobs)
            if (remaining_jobs > 0):
                response = {"response":"Request granded", "initial_jobs":project_jobs, "remaining_jobs":remaining_jobs, "cpu":project_cpu, "ram":project_ram}
                response_json = json.dumps(response)
                return HttpResponse(response_json)
            else:
                response = {"response":"Request denied", "initial_jobs":project_jobs, "remaining_jobs":remaining_jobs, "cpu":project_cpu, "ram":project_ram}
                response_json = json.dumps(response)
                return HttpResponse(response_json)
    
    else:

        try:
            project_obj = Project.objects.get(id=id)
        except:
            response = {"Error: project does not exist\n"}
            return HttpResponse(response)

        #if the project is deleted, expired, rejected or pending return 0s
        if (project_obj.status == -4 or project_obj.status == -5 or project_obj.status == -1 or project_obj.status == 0):
            response = {"Error: project is not valid\n"}
            return HttpResponse(response)
            
        latest_project_request = project_obj.latest_project_request_id
        on_demand_obj = OndemandRequest.objects.get(request_id=latest_project_request)
        project_jobs = on_demand_obj.num_of_jobs 
        project_name = project_obj.name
        project_cpu = on_demand_obj.cores
        project_ram = on_demand_obj.ram

        data = {'project':project_name}
        r = requests.get('https://hypatia-comp.athenarc.gr/index.php?r=api/project-usage', params=data)
        usage = r.text

        if usage == "false":
            response = {"initial_jobs":project_jobs, "remaining_jobs":project_jobs, "cpu":project_cpu, "ram":project_ram}
            response_json = json.dumps(response)
            return HttpResponse(response_json)
        
        else:
            tmp = usage.split(',')[0]
            used_jobs = tmp.split(':')[1]
            remaining_jobs = project_jobs - int(used_jobs)
            response = {"initial_jobs":project_jobs, "remaining_jobs":remaining_jobs, "cpu":project_cpu, "ram":project_ram}
            response_json = json.dumps(response)
            return HttpResponse(response_json)


