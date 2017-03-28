import React from "react";


export default class DfsCode extends React.Component {
	constructor(props){
		super(props);
		// console.log(this.props.line)
		this.state= {
			line: this.props.line,
			content : []
		}
	}
	componentWillMount(){
		var content = [];
		content.push("def dfs(grid,start):")
		content.push("    if(start not in visited):")
		content.push("        visited.append(start)")
		content.push("        for i in range(0,nodes):")
		content.push("            if(grid[start][i]):")
		content.push("                if(i not in visited):")
		content.push("                    dfs(grid,i)")
		this.setState({	
			content: content
		})
		
	}

	componentWillReceiveProps(nextProps) {
    	this.setState({line: nextProps.line});
	}

	render(){
		var codeHtml = []
		codeHtml.push(<span>visited =  [] </span>)
		codeHtml.push(<br></br>)
		codeHtml.push(<br></br>)
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
			codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>dfs(grid,start)</span>)
		}
		else
		{
			codeHtml.push(<span>dfs(grid,start)</span>)
		}
		return(<div>
			<pre>
			{codeHtml}
			</pre>
			</div>)
	}
}