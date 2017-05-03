from django.http import JsonResponse
from collections import OrderedDict

from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from heapq import heappush,heappop
INFINITY=10**18



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

def styleCreator(selector, color, type):
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




def snapshot(nodes,grid,line,currentNode,currentNodeChild,pq,dist):
    returnData = OrderedDict()
    returnData['style']=list(snapArrayDefault['style'])
    returnData['elements'] = elementCreator(nodes,grid)
    returnData['line'] = line
    returnData['arr'] = []
    # for i in visited:
    #     returnData['style'].append(styleCreator(nodes,createSelector(nodes,"node",i+1),visitedColour))
    # for i in range(nodes):
    #     for j in range(i+1,nodes):
    #         if(i in visited and j in visited):
    #             returnData['style'].append(styleCreator(nodes,createSelector(nodes,"edge",i+1,j+1),visitedColour))
    if(currentNode!=-1):
        returnData['style'].append(styleCreator(createSelector("node",currentNode+1),currentColour,"node"))
        if(currentNodeChild!=-1):
            returnData['style'].append(styleCreator(createSelector("node",currentNodeChild+1),visitedColour,"node"))
            returnData['style'].append(styleCreator(createSelector("edge",currentNode+1,currentNodeChild+1),visitedColour,"edge"))
    if(pq!=-1):
        tempDict = {}
        tempDict['type'] = "1D"
        tempDict['name'] = "Priority Queue ( point, distance ) "
        tempvis = []
        for val in pq:
            tempvis.append(str(val[0]+1) + ", " +str(val[1]))
        tempDict['content'] = list(tempvis)
        returnData['arr'].append(tempDict)
    if(dist!=-1):
        tempDict = {}
        tempDict['type'] = "1D"
        tempDict['name'] = "Distance from starting point to other point"
        tempvis = []
        for val in dist:
            tempvis.append(val)
        tempDict['content'] = list(tempvis)
        returnData['arr'].append(tempDict)
    return returnData

def MakeListFromMatrix(grid,n):
    graph=[[] for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if(grid[i][j]):
                graph[i].append((j,grid[i][j]))
                graph[j].append((i,grid[i][j]))
    return graph

def validGrid(grid):
    for i in grid:
        for j in i:
            if(j<0):
                return False
    return True

def DijkstraAlgorithm(grid,StartPoint):
    global visited
    visited = []
    global snapArray
    snapArray = []
    #Matrix = parseMatrix(request)
    nodes = len(grid[0])
    if(not validGrid(grid)):
        return JsonResponse({'error':True,'errorDescription':'Graph contains negative weighted edge'})
    #visited = [False]*nodes
    returnResponse = OrderedDict()    
    #snapArray.append(snapshot(nodes,Matrix,0))
    #visited.append(Start)
    snapArray.append(snapshot(nodes,grid,-1,-1,-1,-1,-1))
    snapArray.append(snapshot(nodes,grid, 2,-1,-1,-1,-1))
    graph=MakeListFromMatrix(grid,nodes)
    PriorityQueue=[(StartPoint,0)]
    snapArray.append(snapshot(nodes,grid, 3,StartPoint,-1,PriorityQueue,-1))
    distance=[INFINITY]*(nodes)
    snapArray.append(snapshot(nodes,grid, 4,-1,-1,PriorityQueue,distance))
    distance[StartPoint]=0
    snapArray.append(snapshot(nodes,grid, 5,StartPoint,-1,PriorityQueue,distance))
    snapArray.append(snapshot(nodes,grid, 6,-1,-1,PriorityQueue,distance))
    while(PriorityQueue):
        TopElement,Cost=heappop(PriorityQueue)
        snapArray.append(snapshot(nodes,grid, 7, TopElement,-1,PriorityQueue,distance))
        #print(TopElement,Cost)
        snapArray.append(snapshot(nodes,grid, 8, TopElement,-1,PriorityQueue,distance))
        if(Cost>distance[TopElement]):
            snapArray.append(snapshot(nodes,grid, 9, TopElement,-1,PriorityQueue,distance))
            pass
        snapArray.append(snapshot(nodes,grid, 10, TopElement,-1,PriorityQueue,distance))
        for to,weight in graph[TopElement]:
            snapArray.append(snapshot(nodes,grid, 11, TopElement,to,PriorityQueue,distance))
            if((distance[TopElement]+weight)<=distance[to]):
                distance[to]=(distance[TopElement]+weight)
                snapArray.append(snapshot(nodes,grid, 11, TopElement,to,PriorityQueue,distance))
                heappush(PriorityQueue,(to,distance[to]))
                snapArray.append(snapshot(nodes,grid, 11, to,-1,PriorityQueue,distance))
    # print(*distance)
    returnResponse['error'] = False
    returnResponse['data'] = snapArray
    #print(len(snapArray))
    #print(snapArray[0])
    #print("\n\n\n\n")
    #print(snapArray[1])

    return JsonResponse(returnResponse)