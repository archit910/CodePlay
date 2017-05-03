import React from "react";


export default class KruskalMstAlgorithm extends React.Component {
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
		content.push("def FindParent(parent,key):")
		content.push("    if(parent[key]==key):")
		content.push("        return key")
		content.push("    return FindParent(parent,parent[key])")
		content.push("              ")
		content.push("def Union(rank,parent,u,v):")
		content.push("    u=FindParent(parent,u)")
		content.push("    v=FindParent(parent,v)")
		content.push("    if(rank[u]>rank[v]):")
		content.push("        parent[v]=u")
		content.push("    elif(rank[v]>rank[u]):")
		content.push("        parent[u]=v")
		content.push("    else:")
		content.push("        parent[v]=u")
		content.push("        rank[u]+=1")
		content.push("              ")
		content.push("def KruskalMst(graph,nodes):")
		content.push("    graph=sorted(graph,key=lambda item: item[2])")
		content.push("    rank=[0]*(nodes)")
		content.push("    parent=[0]*(nodes)")
		content.push("    ResultantMst=[]")
		content.push("    for i in range(nodes):")
		content.push("        parent[i]=i")
		content.push("    i=0")
		content.push("    start=0")
		content.push("    while(start<nodes-1):")
		content.push("        u,v,weight=graph[i]")
		content.push("        i=i+1")
		content.push("        ParentU=FindParent(parent,u)")
		content.push("        ParentV=FindParent(parent,v)")
		content.push("        if(ParentU!=ParentV):")
		content.push("            start=start+1")
		content.push("            ResultantMst.append([u,v,weight])")
		content.push("            Union(rank,parent,ParentU,ParentV)")
		content.push("    print(ResultantMst)")

		this.setState({	
			content: content
		})
		
	}

	componentWillReceiveProps(nextProps) {
    	this.setState({line: nextProps.line});
	}

	render(){
		var codeHtml = []
		//codeHtml.push(<span>visited =  [] </span>)
		//codeHtml.push(<br></br>)
		
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
		if(this.state.line==-1)
		{
			codeHtml.push(<span style={{'border':'1px solid','background':'#8f939b','color':'white'}}>KruskalMst(graph,nodes)</span>)
		}
		else
		{
			codeHtml.push(<span>KruskalMst(graph,nodes)</span>)
		}
		return(<div>
			<pre>
			{codeHtml}
			</pre>
			</div>)
	}
}