from django.shortcuts import render
from django.http import JsonResponse
from collections import OrderedDict
import time

from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from .bfs import BreadthFirstSearch
from .dijkstra import DijkstraAlgorithm
from .prims import PrimsMinimumSpanningTree
from .kruskal import KruskalMinimumSpanningTree
def parseMatrix(request):
	nodes = int(request.POST.get('nodes'))
	matrix = []
	for i in range(nodes):
		row = []
		for j in range(nodes):
			variable = "matrix[" + str(i) + "][" + str(j)+"]"
			row.append(int(request.POST.get(variable)))
		matrix.append(row)
	# print(matrix)
	return matrix

visited = []
nodes = 7

#Colours
visitedColour = "#FF0000"
defaultColour = "#11479e"
currentColour = "#bbbbbb"

snapArray=[]

snapArrayDefault = OrderedDict()
snapArrayDefault['style'] = [
            {'selector': 'node',
              'style': {
                'content': 'data(id)',
                'text-opacity': 0.5,
                'text-valign': 'center',
                'text-halign': 'right',
                'background-color': defaultColour
                }
            },

            {
              'selector': 'edge',
              'style':{
                'width': 3,
                'line-color': '#9dbaea',
                'curve-style': 'bezier'
                }
            }
        ]

def styleCreator(selector, color,type):
    returnStyle = OrderedDict()
    returnStyle['selector'] = selector
    returnStyle['style'] = OrderedDict()
    if (type=="node"):
        returnStyle['style']['background-color'] = color
    else:
        returnStyle['style']['line-color'] = color
    # print returnStyle
    return returnStyle

def createSelector(type,*elements):
    if(type=="node"):
        return "#n"+str(elements[0])
    else:
        return "#e"+str(elements[0])+str(elements[1])

def getNodes():
    nodesArray= []
    for i in range(0,nodes):
        nodesArray.append({'data':{'id':"n"+str(i+1)}})
    return nodesArray

def getEdge(grid):
	edgeArray = []
	for i in range(nodes):
		for j in range(i+1,nodes):
			if(grid[i][j]):
				edgeArray.append({'data':{'id':"e"+str(i+1)+str(j+1),'source':'n'+str(i+1),'target':'n'+str(j+1)}})
	return edgeArray

def elementCreator(grid):
    elements = OrderedDict()
    elements['nodes'] = getNodes()
    elements['edges'] = getEdge(grid)
    return elements




def snapshot(*arguments):
    returnData = OrderedDict()
    returnData['style']=list(snapArrayDefault['style'])
    returnData['elements'] = elementCreator(arguments[0])
    returnData['line'] = arguments[1]
    for i in visited:
        returnData['style'].append(styleCreator(createSelector("node",i+1),visitedColour,"node"))
    for i in range(nodes):
        for j in range(i+1,nodes):
            if(i in visited and j in visited):
                returnData['style'].append(styleCreator(createSelector("edge",i+1,j+1),visitedColour,"edge"))
    try:
        if(arguments[2]!=-1):
            returnData['style'].append(styleCreator(createSelector("node",arguments[2]+1),currentColour,"node"))
    except :
        pass
    # for i in arguments
    returnData['arr'] = []
    tempDict = {}
    tempDict['type'] = "1D"
    tempDict['name'] = "Visited"
    tempvis = []
    for val in visited:
        tempvis.append(val+1)
    tempDict['content'] = list(tempvis)
    returnData['arr'].append(tempDict)

    return returnData

def dfs(grid,start):
    snapArray.append(snapshot(grid,0,start))
    snapArray.append(snapshot(grid,1,start))
    if(start not in visited):
        # print(start)
        visited.append(start)
        snapArray.append(snapshot(grid,2,-1))
        for i in range(0,nodes):
        	# print(start,i,nodes,"============")
        	if(grid[start][i]):
        		snapArray.append(snapshot(grid,4,i))
        		if(i not in visited):
        			snapArray.append(snapshot(grid,5,i))
        			snapArray.append(snapshot(grid,6,i))
        			dfs(grid,i)

@csrf_exempt
def solve(request):
	returnResponse = OrderedDict()
	# print(request.POST.get('matrix[0][0]'))
	# print ("here is the output=======================")
	global visited
	visited = []
	global snapArray
	snapArray = []
	grid = parseMatrix(request)
	global nodes
	nodes = int(request.POST.get('nodes'))
	print(nodes,"=========")
	start = int(request.POST.get('start'))
	Algorithm = str(request.POST.get('algo'))
	if(Algorithm == "bfs"):
		return BreadthFirstSearch(request,start)
	elif(Algorithm == "dijkstra"):
		return DijkstraAlgorithm(grid,start)
	elif(Algorithm == "prims"):
		return PrimsMinimumSpanningTree(grid,nodes)
	elif(Algorithm == "kruskal"):
		return KruskalMinimumSpanningTree(grid,nodes)
	else:
		dfs(grid,start)
		returnResponse['error'] = False
		returnResponse['data'] = snapArray
		print(len(snapArray))
	# style={
	# 'content': 'data(id)',
	# 'text-opacity': 0.2,
	# 'text-valign': 'center',
	# 'text-halign': 'right',
	# 'background-color': '#11479e'
	# }
	# returnResponse['style'] = style
	# print(returnResponse)
	print("I am coming here also!!")
	return JsonResponse(returnResponse)

def s(request):
    for i in range(1,10000000):
        print(i)
    returnResponse = {}
    returnResponse['error'] = False
    return JsonResponse(returnResponse)


def b(request):
    returnResponse = {}
    returnResponse['error'] = False
    return JsonResponse(returnResponse)
