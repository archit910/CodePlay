from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt


def parseMatrix(request):
	return True

@csrf_exempt
def solve(request):
	returnResponse = {}
	print(request.POST.get('matrix[0][0]'))
	returnResponse['error'] = False
	return JsonResponse(returnResponse)