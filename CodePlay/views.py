from django.shortcuts import render
from django.http import JsonResponse
from collections import OrderedDict

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
	# print(matrix)
	return matrix

visited = []
nodes = 10

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

def styleCreator(selector, color):
    returnStyle = OrderedDict()
    returnStyle['selector'] = selector
    returnStyle['style'] = OrderedDict()
    returnStyle['style']['background-color'] = color
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
        returnData['style'].append(styleCreator(createSelector("node",i+1),visitedColour))
    for i in range(nodes):
        for j in range(i+1,nodes):
            if(i in visited and j in visited):
                returnData['style'].append(styleCreator(createSelector("edge",i+1,j+1),visitedColour))
    try:
        if(arguments[2]):
            returnData['style'].append(styleCreator(createSelector("node",arguments[2]+1),currentColour))
    except :
        pass

    return returnData

def dfs(grid,start):
    snapArray.append(snapshot(grid,0,start))
    snapArray.append(snapshot(grid,1,start))
    if(start not in visited):
        # print(start)
        visited.append(start)
        snapArray.append(snapshot(grid,2))
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
	dfs(grid,start)
	returnResponse['error'] = False
	returnResponse['data'] = snapArray
	print(len(snapArray))
	for i in range(len(snapArray)):
		print(i)
		print(snapArray[i])
		print("\n\n\n\n")
	# print(snapArray[1])
	# style={
	# 'content': 'data(id)',
	# 'text-opacity': 0.2,
	# 'text-valign': 'center',
	# 'text-halign': 'right',
	# 'background-color': '#11479e'
	# }
	# returnResponse['style'] = style
	# print(returnResponse)

	return JsonResponse(returnResponse)