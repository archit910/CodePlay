import React from "react";

export default class App1Container extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			nodes : 1,
			algo : 'bfs'
		}
		this.onNumberOfNodesChange = this.onNumberOfNodesChange.bind(this);
		this.onAlgoChange = this.onAlgoChange.bind(this);
	}

	onNumberOfNodesChange(e){
		// console.log(e.target.value);
		this.setState({
			nodes : e.target.value
		})
	}

	onAlgoChange(e){
		// console.log(e.target.value);
		this.setState({
			algo : e.target.value
		})
	}

	render() {
		var nodesHtml = [];
		for (var i = 1; i <= 8; i++) {
			nodesHtml.push( <option value={i}>{i}</option>);
		}
		//console.log(nodes);
		var inputMatrixHtml = [];
		for (var i = 0; i <= this.state.nodes ; i++) {
			var temporaryRow = [];
			// console.log("i = ",i);
			if(i == 0){
				for(var j = 0 ; j <= this.state.nodes ; j++) {
					// console.log("j = ",j);
					if(j==0)
					{
						temporaryRow.push(<td></td>);
					}
					else
					{
						temporaryRow.push(<td>n{j}</td>);
					}
				}
			}
			else
			{
				for(var j = 0 ; j <= this.state.nodes ; j++) {
					// console.log("j = ",j);
					if(j==0)
					{
						temporaryRow.push(<td>n{i}</td>);
					}
					else
					{
						temporaryRow.push(<td><input type="text" style={{width:"70px",dispaly:"block"}} name="matrix[0][]" value=""/> </td>);
					}
				}
			}
			inputMatrixHtml.push(<tr>{temporaryRow}</tr>);
		}
		// console.log(inputMatrixHtml);
		// for (var i = inputMatrixHtml.length - 1; i >= 0; i--) {
		// 	console.log(inputMatrixHtml[i])
		// }


		return (
			<div>
				<h4>Control Panel</h4>
					
					<form>
						Select The Algo : 
						<select name="algo" onChange={this.onAlgoChange}>
					        <option value='bfs'>Breadth-First-Search</option>
					        <option value='dfs'>Depth-First-Search</option>
					        <option value='dikjastra'>Dikjastra</option>
					        <option value='belman'>BelmennFord</option>
				      	</select>
				      	<br/>
				      	Select The Nodes : 
						<select name="nodes" onChange={this.onNumberOfNodesChange}>
					        {nodesHtml}

				      	</select>
					</form>

				<table>
					<tbody>
	                	{inputMatrixHtml}
	                	
	                </tbody>
                </table>
			</div>
		);
	}
}