import React from "react";


export default class BfsCode extends React.Component 
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
		content.push("def BreadthFirstSearch(Matrix,start)")
		content.push("    visited.append(start)")
		content.push("    Queue.append(start)")
		content.push("    While(Queue):")
		content.push("        FrontElement=Queue.pop(0)")
		content.push("        for i in range(nodes):")
		content.push("            if(Matrix[FrontElement][i]):")
		content.push("                if(i not in visited):")
		content.push("                    visited.append(i)")
		content.push("                    Queue.append(i)")
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
		codeHtml.push(<span>visited =  [] </span>)
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
        console.log(this.state.content.length,"length is here")
			codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>BreadthFirstSearch(Matrix,start)</span>)
		}
		else
		{
			codeHtml.push(<span>BreadthFirstSearch(Matrix,start)</span>)
		}
		return(<div>
			<pre>
			{codeHtml}
			</pre>
			</div>)
	}
}