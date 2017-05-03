from django.http import JsonResponse
from collections import OrderedDict

INFINITY=10**18

snapArray  = []
graph = []
distance = []

visitedColour = "#FF0000"
defaultColour = "#11479e"
currentColour = "#bbbbbb"

snapArrayDefault = OrderedDict()
snapArrayDefault['style'] = [
	{
		'selector': 'node',
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

def getNodes(nodes):
	nodesArray= []
	for i in range(0,nodes):
		nodesArray.append({'data':{'id':"n"+str(i+1)}})
	return nodesArray

def getEdge(nodes,grid):
	edgeArray = []
	for i in range(nodes):
		for j in range(i+1,nodes):
			if(grid[i][j]):
				edgeArray.append({'data':{'id':"e"+str(i+1)+str(j+1),'source':'n'+str(i+1),'target':'n'+str(j+1)}})
	return edgeArray

def elementCreator(nodes,grid):
	elements = OrderedDict()
	elements['nodes'] = getNodes(nodes)
	elements['edges'] = getEdge(nodes,grid)
	return elements

def snapshot(nodes,grid,line,currentNode,currentNodeChild,dist):
	returnData = OrderedDict()
	returnData['style']=list(snapArrayDefault['style'])
	returnData['elements'] = elementCreator(nodes,grid)
	returnData['line'] = line
	if(currentNode!=-1):
		returnData['style'].append(styleCreator(createSelector("node",currentNode+1),currentColour,"node"))
		if(currentNodeChild!=-1):
			returnData['style'].append(styleCreator(createSelector("node",currentNodeChild+1),visitedColour,"node"))
			returnData['style'].append(styleCreator(createSelector("edge",currentNode+1,currentNodeChild+1),visitedColour,"edge"))

	returnData['arr'] = []
	if(dist!=-1):
		tempDict = {}
		tempDict['type'] = "1D"
		tempDict['name'] = "Distance from starting point(n1) to every other point"
		tempvis = []
		for val in dist:
		    tempvis.append(val)
		tempDict['content'] = list(tempvis)
		returnData['arr'].append(tempDict)
	return returnData

def buildGraph(grid):
	# print(type(grid))
	for i in range(len(grid)):
		for j in range(len(grid)):
			if(grid[i][j]):
				graph.append([i,j,grid[i][j]])

def bellmanFordSolve(src,nodes,grid):
	snapArray.append(snapshot(nodes,grid,-1,-1,-1,-1))
	snapArray.append(snapshot(nodes,grid,6,-1,-1,-1))
	global distance
	distance = [INFINITY]*nodes
	snapArray.append(snapshot(nodes,grid,7,-1,-1,distance))
	distance[src] = 0
	snapArray.append(snapshot(nodes,grid,8,-1,-1,distance))

	for i in range(nodes-1) :
		snapArray.append(snapshot(nodes,grid,9,-1,-1,distance))
		for u,v,w in graph:
			snapArray.append(snapshot(nodes,grid,10,-1,-1,distance))
			snapArray.append(snapshot(nodes,grid,11,u,v,distance))
			if( distance[u] + w < distance[v]):
				distance[v] = distance[u] + w
				snapArray.append(snapshot(nodes,grid,12,u,v,distance))

def checkNegativeCycle(nodes):
	global distance
	for u,v,w in graph:
		if( distance[u] + w < distance[v]):
			return True
	return False

def bellmanFord(grid,start):
	returnResponse = OrderedDict()
	global snapArray
	global graph
	global distance
	graph = []
	snapArray = []
	returnResponse['error'] = False
	# print (grid,"hsgdh")
	buildGraph(grid)
	bellmanFordSolve(start,len(grid),grid)
	returnResponse['data'] = snapArray
	# print (distance)
	if(checkNegativeCycle(len(grid))):
		returnResponse['error'] = True
		returnResponse['errorDescription'] = 'Found Negative cycle'
	return JsonResponse(returnResponse)