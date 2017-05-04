from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Description

def getAlgoDescription(request):
	dataToBeReturned = {}
	algorithm = request.GET['algo']
	if(Description.objects.filter(algo = algorithm).exists()):
		info = Description.objects.filter(algo = algorithm)[0]
		if(algorithm=='bfs'):
			dataToBeReturned['name'] = "Breadth First Search"
		elif(algorithm=='dijkstra'):
			dataToBeReturned['name'] = "Dijkstra"
		elif(algorithm=='dfs'):
			dataToBeReturned['name'] = "Depth First Search"
		elif(algorithm=='prims'):
			dataToBeReturned['name'] = "Prim's MST"
		elif(algorithm=='kruskal'):
			dataToBeReturned['name'] = "Kruskal's MST"
		elif(algorithm=='bellman'):
			dataToBeReturned['name'] = "Bellman Ford"
		else:
			dataToBeReturned['name'] = algorithm
		dataToBeReturned['descript'] = info.descript
		dataToBeReturned['spaceComplexity'] = info.spaceComplexity
		dataToBeReturned['timeComlexity'] = info.timeComlexity
		dataToBeReturned['links'] = info.links.split(',')
		dataToBeReturned['error'] = False
		print (dataToBeReturned)
		return JsonResponse(dataToBeReturned)
	else:
		return JsonResponse({'error' : True})
