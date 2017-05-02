import React from "react";


export default class DijkstraAlgorithm extends React.Component 
{

	constructor(props)
	{
		super(props)
		this.state = {
			line: this.props.line,
			content : []
		}
	}
	componentWillMount()
	{
		var content = []
		content.push("from heapq import heappush,heappop")
		content.push(<br></br>)
		content.push("def DijkstraAlgorithm(grid,StartPoint)")
		content.push("    PriorityQueue = [(StartPoint,0)]")
		content.push("    distance=[INFINITY]*(n)")
		content.push("    distance[StartPoint]=0")
		content.push("    while(PriorityQueue):")
		content.push("        TopElement,Cost=heappop(PriorityQueue)")
		content.push("        if(Cost>distance[TopElement]):")
		content.push("            pass")
		content.push("        for to,weight in graph[TopElement]:")
		content.push("            if((distance[TopElement]+weight)<=distance[to]):")
		content.push("                distance[to]=(distance[TopElement]+weight)")
		content.push("                heappush(PriorityQueue,(to,distance[to]))")
		
		// console.log(this.state.content.length,"length 2 is here")
		this.setState({
			content: content
		})
	}


	componentWillReceiveProps(nextProps)
	{
		this.setState({line:nextProps.line});
	}


	render()
	{
		var codeHtml = []
		
		//codeHtml.push(<br></br>)
		// console.log(this.state.content.length,"length is here")
		for(let i = 0; i <this.state.content.length;i++ )
		{
			if(i==this.state.line)
			{
				codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>{this.state.content[i]}</span>)
			}
			else
			{
				codeHtml.push(<span>{this.state.content[i]}</span>)
			}
			codeHtml.push(<br></br>)
		}
		codeHtml.push(<br></br>)
		codeHtml.push(<br></br>)
		if(this.state.line==-1)
		{
        console.log(this.state.content.length,"length is here")
			codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>DijkstraAlgorithm(graph,StartPoint)</span>)
		}
		else
		{
			codeHtml.push(<span>DijkstraAlgorithm(grid,StartPoint)</span>)
		}
		return(<div>
			<pre>
			{codeHtml}
			</pre>
			</div>)
	}
}