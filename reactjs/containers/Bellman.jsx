import React from "react";


export default class Bellman extends React.Component 
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
		content.push("def buildGraph(grid):")
		content.push("    for i in range(len(grid)):")
		content.push("        for j in range(len(grid))")
		content.push("            if(grid[i][j]):")
		content.push("                graph.append([i,j,grid[i][j]])")
		content.push(<br></br>)
		content.push("def bellmanFordSolve(src,nodes):")
		content.push("    distance = [INFINITY]*nodes")
		content.push("    distance[src] = 0")
		content.push("    for i in range(nodes-1) :")
		content.push("        for u,v,w in graph:")
		content.push("            if( distance[u] + w < distance[v]):")
		content.push("                distance[v] = distance[u] + w")
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
		codeHtml.push(<span>graph =  [] </span>)
		codeHtml.push(<br></br>)
		codeHtml.push(<br></br>)
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
        // console.log(this.state.content.length,"length is here")
        	codeHtml.push(<span>buildGraph(grid)</span>)

			codeHtml.push(<br></br>)
			codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>bellmanFordSolve(start,nodes,Matrix)</span>)
		}
		else
		{
        	codeHtml.push(<span>buildGraph(grid)</span>)
			codeHtml.push(<br></br>)
			codeHtml.push(<span>bellmanFordSolve(start,nodes)</span>)
		}
		return(<div>
			<pre>
			{codeHtml}
			</pre>
			</div>)
	}
}