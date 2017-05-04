import React from "react";
import Input from "./Input"
import axios from 'axios';

export default class App1Container extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			nodes : this.props.nodes,
			algo : this.props.algo,
			matrix : this.props.matrix,
			loading : this.props.loading,
			algoInfo : '',
			links : '',

		}
		this.onNumberOfNodesChange = this.onNumberOfNodesChange.bind(this);
		this.onAlgoChange = this.onAlgoChange.bind(this);
		this.handelMatrixFieldChange = this.handelMatrixFieldChange.bind(this);
		this.onClickSubmitButton = this.onClickSubmitButton.bind(this);
		this.onClickResetButton = this.onClickResetButton.bind(this);
		var url = "/getalgodescription/?algo=".concat(this.state.algo)
		// console.log(url)
		axios.get(url)
		.then(function(response){
			console.log(response.data)
			var links = []
			console.log(response.data.links)
			for(let i=0 ; i< response.data.links.length ; i++)
			{
				links.push(<a href={response.data.links[i]}>{response.data.links[i]}</a>)
				links.push(<br></br>)
			}
			this.setState({
				algoInfo : response.data,
				links: links
			})
		}.bind(this))
	}

	componentWillReceiveProps(nextProps){
		// console.log("next props",nextProps.nodes,nextProps.algo,nextProps.matrix)
		this.setState({
			nodes: nextProps.nodes,
			algo: nextProps.algo,
			matrix: nextProps.matrix,
			loading : this.props.loading
		},()=>{
			var url = "/getalgodescription/?algo=".concat(this.state.algo)
			// console.log(url)
			axios.get(url)
			.then(function(response){
				console.log(response.data)
				var links = []
				console.log(response.data.links)
				for(let i=0 ; i< response.data.links.length ; i++)
				{
					links.push(<a href={response.data.links[i]}>{response.data.links[i]}</a>)
					links.push(<br></br>)
				}
				this.setState({
					algoInfo : response.data,
					links: links
				})
			}.bind(this))
		})
	}

	onClickSubmitButton(){
		// console.log("dsfddsfdfdgffd")
		this.props.onClickSubmitButton();
	}

	onClickResetButton(){
		this.props.onClickResetButton();
  	}

	handelMatrixFieldChange(i,j,e){
		// console.log(i,j,e.target.value);
		var tempMatrix = this.state.matrix;
		// console.log("=======",tempMatrix[i][j]);
		tempMatrix[i][j] = e.target.value;
		this.setState({
			matrix: tempMatrix
		})
		this.props.updateMatrix(tempMatrix);

	}

	onNumberOfNodesChange(e){
		// console.log(e.target.value);
		var tempMatrix = [];
		for (var i = 0; i < e.target.value ; i++) {
			var row = [];
			for (var j = 0; j < e.target.value; j++) {
				row.push(0);
			}
			tempMatrix.push(row);
		}
		this.setState({
			nodes : e.target.value,
			matrix: tempMatrix
		})
		this.props.updateMatrix(tempMatrix);
		this.props.updateNumberOfNodes(e.target.value);
	}

	onAlgoChange(e){
		// console.log(e.target.value);
		this.setState({
			algo : e.target.value
		})
		var url = "/getalgodescription/?algo=".concat(e.target.value)
		// console.log(url)
		axios.get(url)
		.then(function(response){
			console.log(response.data)
			var links = []
			console.log(response.data.links)
			for(let i=0 ; i< response.data.links.length ; i++)
			{
				links.push(<a href={response.data.links[i]}>{response.data.links[i]}</a>)
				links.push(<br></br>)
			}
			this.setState({
				algoInfo : response.data,
				links: links
			})
		}.bind(this))
		this.props.updateAlgo(e.target.value);
	}

	render() {
		var nodesHtml = [];
		for (var i = 1; i <= 8; i++) {
			nodesHtml.push( <option value={i}>{i}</option>);
		}
		//console.log(nodes);
		var inputMatrixHtml = [];
		for (let i = 0; i <= this.state.nodes ; i++) {
			let temporaryRow = [];
			// console.log("i = ",i);
			if(i == 0){
				for(let j = 0 ; j <= this.state.nodes ; j++) {
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
				for(let j = 0 ; j <= this.state.nodes ; j++) {
					// console.log("j = ",j);
					if(j==0)
					{
						temporaryRow.push(<td>n{i}</td>);
					}
					else
					{
						temporaryRow.push(<td><input type="text" style={{width:"40px"}} onChange={(e)=>this.handelMatrixFieldChange(i-1,j-1,e)} value={this.state.matrix[i-1][j-1]}/> </td>);
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
					        <option value='dijkstra'>Dijkstra</option>
					        <option value='bellman'>BelmennFord</option>
					        <option value='prims'>Prims-Mst</option>
					        <option value='kruskal'>Kruskal-Mst</option>
				      	</select>
				      	<br/>
				      	Select The Nodes : 
						<select name="nodes" onChange={this.onNumberOfNodesChange}>
					        {nodesHtml}

				      	</select>
					</form>

					<button className="btn btn-primary" onClick={this.onClickSubmitButton}>Submit</button>
				    <button className="btn btn-warning" onClick={this.onClickResetButton}>Reset</button>
				    
				<table>
					<tbody>
	                	{inputMatrixHtml}
	                	
	                </tbody>
                </table>

                <h4>Name of The Algorithm : </h4> <p>{this.state.algoInfo.name} </p>
                <h4>Description of The Algorithm : </h4> <p>{this.state.algoInfo.descript}</p>
                <h4>Space complexity : </h4> <p>{this.state.algoInfo.spaceComplexity} </p>
                <h4>Time complexity : </h4> <p>{this.state.algoInfo.timeComlexity} </p>
                <h4>Suggested Links : </h4>
                {this.state.links}
			</div>
		);
	}
}