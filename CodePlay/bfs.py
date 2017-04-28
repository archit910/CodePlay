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
#nodes = 10
Queue=[]
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

def styleCreator(nodes,selector, color):
    returnStyle = OrderedDict()
    returnStyle['selector'] = selector
    returnStyle['style'] = OrderedDict()
    returnStyle['style']['background-color'] = color
    # print returnStyle
    return returnStyle

def createSelector(nodes,type,*elements):
    if(type=="node"):
        return "#n"+str(elements[0])
    else:
        return "#e"+str(elements[0])+str(elements[1])

def getNodes(nodes):
    nodesArray= []
    for i in range(0,nodes):
        nodesArray.append({'data':{'id':"n"+str(i+1)}})
    return nodesArray

def getEdge(nodes,grid):
	edgeArray = []
	for i in range(nodes):
		for j in range(i+1,nodes):
			#print(i,j,nodes)
			if(grid[i][j]):
				edgeArray.append({'data':{'id':"e"+str(i+1)+str(j+1),'source':'n'+str(i+1),'target':'n'+str(j+1)}})
	return edgeArray

def elementCreator(nodes,grid):
    elements = OrderedDict()
    elements['nodes'] = getNodes(nodes)
    elements['edges'] = getEdge(nodes,grid)
    return elements




def snapshot(nodes,*arguments):
    returnData = OrderedDict()
    returnData['style']=list(snapArrayDefault['style'])
    returnData['elements'] = elementCreator(nodes,arguments[0])
    returnData['line'] = arguments[1]
    for i in visited:
        returnData['style'].append(styleCreator(nodes,createSelector(nodes,"node",i+1),visitedColour))
    for i in range(nodes):
        for j in range(i+1,nodes):
            if(i in visited and j in visited):
                returnData['style'].append(styleCreator(nodes,createSelector(nodes,"edge",i+1,j+1),visitedColour))
    try:
        if(arguments[2]):
            returnData['style'].append(styleCreator(nodes,createSelector(nodes,"node",arguments[2]+1),currentColour))
    except :
        pass
    returnData['arr'] = []
    tempDict = {}
    tempDict['type'] = "1D"
    tempDict['name'] = "Visited"
    tempvis = []
    for val in visited:
        tempvis.append(val+1)
    tempDict['content'] = list(tempvis)
    returnData['arr'].append(tempDict)

    tempDict1 = {}
    tempDict1['type'] = "1D"
    tempDict1['name'] = "Queue"
    tempvis1 = []
    for val in Queue:
        tempvis1.append(val+1)
    tempDict1['content'] = list(tempvis1)
    returnData['arr'].append(tempDict1)

    return returnData

def BreadthFirstSearch(request,Start):
    global visited
    visited = []
    global snapArray
    snapArray = []
    Matrix = parseMatrix(request)
    nodes = len(Matrix[0])
    # visited = [False]*nodes
    returnResponse = OrderedDict()    
    snapArray.append(snapshot(nodes,Matrix,0))
    visited.append(Start)
    snapArray.append(snapshot(nodes,Matrix,1))
    Queue.append(Start)
    snapArray.append(snapshot(nodes,Matrix,2))
    snapArray.append(snapshot(nodes,Matrix,3))
    while(Queue):
        FrontElement = Queue.pop(0)
        snapArray.append(snapshot(nodes,Matrix,4))
        for i in range(0,nodes):
            snapArray.append(snapshot(nodes,Matrix,6,i))
            if(FrontElement!=i and Matrix[FrontElement][i]):
                snapArray.append(snapshot(nodes,Matrix,7,i))
                if(i not in visited):
                    visited.append(i)
                    snapArray.append(snapshot(nodes,Matrix,8))
                    Queue.append(i)
                    snapArray.append(snapshot(nodes,Matrix,9))
    returnResponse['error'] = False
    returnResponse['data'] = snapArray
    # print(len(snapArray))
    # print(snapArray[0])
    # print("\n\n\n\n")
    # print(snapArray[1])

    return JsonResponse(returnResponse)