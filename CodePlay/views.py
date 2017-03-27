from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt


def parseMatrix(request):
	nodes = int(request.POST.get('nodes'))
	matrix = []
	for i in range(nodes):
		row = []
		for j in range(nodes):
			variable = "matrix[" + str(i) + "][" + str(j)+"]"
			row.append(int(request.POST.get(variable)))
		matrix.append(row)
	return matrix

@csrf_exempt
def solve(request):
	returnResponse = {}
	print(request.POST.get('matrix[0][0]'))
	print ("here is the output=======================")
	print(parseMatrix(request))
	returnResponse['error'] = False
	style={
	'content': 'data(id)',
	'text-opacity': 0.2,
	'text-valign': 'center',
	'text-halign': 'right',
	'background-color': '#11479e'
	}
	returnResponse['style'] = style
	print(returnResponse)

	return JsonResponse(returnResponse)