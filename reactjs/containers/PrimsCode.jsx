import React from "react";


export default class PrimsMstAlgorithm extends React.Component {
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
		content.push("INFINITY=10**18")
		content.push("def MinKey(key,MstSet,n):")
		content.push("    MinElement=INFINITY")
		content.push("    MinElementIndex=-1")
		content.push("    for i in range(n):")
		content.push("        if(MstSet[i]==0 and key[i]<MinElement):")
		content.push("            MinElement=key[i]")
		content.push("            MinElementIndex=i")
		content.push("    return MinElementIndex")
		content.push("def PrimsMst(graph,n):")
		content.push("    parent=[-1]*n")
		content.push("    key=[INFINITY]*(n)")
		content.push("    MstSet=[0]*(n)")
		content.push("    key[0]=0")
		content.push("    for i in range(n-1):")
		content.push("        u=MinKey(key,MstSet,n)")
		content.push("        MstSet[u]=1")
		content.push("        for j in range(n):")
		content.push("            if(graph[u][j] and MstSet[j]==0 and graph[u][j]<key[j]):")
		content.push("            parent[j]=u")
		content.push("            key[j]=graph[u][j]")
		content.push("    for i in range(1,n):")
		content.push("        print(parent[i],i,graph[i][parent[i]])")
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
			codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>PrimsMst(graph,nodes)</span>)
		}
		else
		{
			codeHtml.push(<span>PrimsMst(graph,nodes)</span>)
		}
		return(<div>
			<pre>
			{codeHtml}
			</pre>
			</div>)
	}
}