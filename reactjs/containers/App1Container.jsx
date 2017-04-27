import React from "react";
import axios from 'axios';

import cytoscape from 'cytoscape';
import cytoscapeDagre from 'cytoscape-dagre'

import Headline from "../components/Headline"
import ControlPanel from "./ControlPanel"
import DfsCode from "./DfsCode"
import BfsCode from "./BfsCode"
import DijkstraAlgorithm from "./Dijkstra"
import StackQ from "./StackQ"

cytoscapeDagre(cytoscape);

export default class App1Container extends React.Component {
  constructor(props){
    super(props);
    var y = {
                'content': 'data(id)',
                'text-opacity': 0.9,
                'text-valign': 'center',
                'text-halign': 'right',
                'background-color': '#11479e'
              };
    this.state = {
      abc: 'true',
      matrix: [[0]],
      nodes : 1,
      algo : 'bfs',
      step : 0,
      description: 'Will be returned from database',
      start: 'n0',
      end: 'n0',
      data: '',
      style: '',
      elements:'',
      line : -1,
      loading: 'none',
      arrType: 'Stack : ',
      arr: ''
    }
    this.renderCytoscapeElement = this.renderCytoscapeElement.bind(this);
    this.onClickPrevButton = this.onClickPrevButton.bind(this);
    this.onClickNextButton = this.onClickNextButton.bind(this);
    this.updateAlgo = this.updateAlgo.bind(this);
    this.updateNumberOfNodes = this.updateNumberOfNodes.bind(this);
    this.updateMatrix = this.updateMatrix.bind(this);
    this.onClickSubmitButton = this.onClickSubmitButton.bind(this);
    this.onClickResetButton = this.onClickResetButton.bind(this);
  }


  onClickSubmitButton(){
    this.setState({
      loading: ''
    })
    console.log("dsfs");
    var qs = require('qs');
    axios.post('/solve/',
      qs.stringify({
        matrix : this.state.matrix,
        algo : this.state.algo,
        nodes : this.state.nodes,
        start: 0,
        
      })
    )
    .then(function (response){
      this.setState({
        data: response.data.data,
        step: 0,
        loading: 'none',
        line: response.data.data[0].line,
        style: response.data.data[0].style,
        elements: response.data.data[0].elements
      })
    }.bind(this))
    // for(var i= 0; i<i+1;i++)
    // {
    //   if(this.state.data!='' && this.state.step==0)
    //   {
    //     this.setState({
    //   loading: 'none'
    // })
    //   }
    // }
    // this.setState({
    //   loading: 'none'
    // })


  }

  onClickResetButton(){
    this.setState({
      abc: 'true',
      matrix: [[0]],
      nodes : 1,
      algo : 'bfs',
      step : 0,
      description: 'Will be returned from database',
      start: 'n0',
      end: 'n0',
      data: '',
      style: '',
      elements:'',
      line : -1,
      loading: 'none'
    })
  }

  updateAlgo(e){
    this.setState({
      algo:e,
      step:0
    })
  }

  updateNumberOfNodes(e){
    var node = ("n").concat(String(e));
    // console.log(node,"===============")
    this.setState({
      nodes:e,
      step : 0,
      end : node
    })
  }

  updateMatrix(e){
    this.setState({
      matrix: e,
      step : 0
    })
  }

  onClickPrevButton(){
    var step = this.state.step;
    var line = this.state.line;
    this.setState({
      step: step-1,
      line: this.state.data[step-2].line,
      style:this.state.data[step-2].style,
      elements: this.state.data[step-2].elements,
      arr : this.this.state.data[step-2].arr
    })
  }


  onClickNextButton(){
    var step = this.state.step;
    var line = this.state.line;
    this.setState({
      step: step + 1,
      line: this.state.data[step].line,
      style:this.state.data[step].style,
      elements: this.state.data[step].elements,
      arr : this.this.state.data[step].arr
    })
  }


  renderCytoscapeElement(){

        console.log('* Cytoscape.js is rendering the graph..');

        

        this.cy = cytoscape(
        {
            container: document.getElementById('cy1'),

            boxSelectionEnabled: false,
            autounselectify: true,

            'style': this.state.style
                ,
            'elements': this.state.elements,

            layout: {
                name: 'dagre',
                directed: true,
                padding: 10
            }
            }); 
    }

    componentDidMount(){
        this.renderCytoscapeElement();
    }
    componentDidUpdate(){
      console.log("asdas")
      this.renderCytoscapeElement();
    }

  render() {
	let cyStyle = {
		height: '300px',
		width: 'auto',
		margin: '20px 0px',
		border: '1px dashed'
	};
	let cyStyle1 = {
		height: '500px',
	};
	var code = <div>Hello I am nothing</div>;
	if(this.state.algo=='dfs')
	{
		code = <DfsCode line={this.state.line}/>;
	}
	else if(this.state.algo=="bfs")
	{
		code = <BfsCode line={this.state.line}/>;
	}
	else if(this.state.algo=="dikjastra")
	{
		code = <DijkstraAlgorithm line={this.state.line}/>;
	}
	else
	{
		code = <div>Wrong Option</div>;
	}
	var arrayCode = [];
	for(let i=0; i<this.state.arr.length;i++)
	{
		arrayCode.push(<StackQ arrType={this.state.arr[i].type} arr={this.state.arr.content}/>)
	}

    
    return (
          <div>
          <p style={{'textAlign':'center'}}>Only Dfs and Bfs is Working Right Now </p>
            <div className="row">
              <div className="col-sm-4 col-md-4 border" style={cyStyle1}>
                <ControlPanel updateAlgo={this.updateAlgo} 
                              updateNumberOfNodes={this.updateNumberOfNodes} 
                              updateMatrix={this.updateMatrix} 
                              onClickSubmitButton={this.onClickSubmitButton} 
                              onClickResetButton={this.onClickResetButton}
                              nodes={this.state.nodes}
                              algo={this.state.algo}
                              matrix={this.state.matrix}
                              loading={this.state.loading}/>
              </div>
              <div className="col-sm-4 col-md-4 border" style={cyStyle1}>
                <h4>Visual</h4>
               
                <span style={{'display':this.state.loading}}>Loading...</span>
                <br></br>
                <button className="btn btn-primary" onClick={this.onClickPrevButton}> - Previous </button>
                <button className="btn btn-primary" onClick={this.onClickNextButton}> Next - </button>
                <div id="cy-container" >
                  <div style={cyStyle} id="cy1"></div>
                </div>
                <div>
                  <StackQ arrType={this.state.arrType} arr={this.state.arr}/>
                  {arrayCode}
                </div>                
              </div>
              <div className="col-sm-4 col-md-4 border" style={cyStyle1}>
                <h4>Code Panel</h4>
                <br/>
                {code}
              </div>
            </div>
            <h4>Description of The Algorithm : {this.state.algo} {this.state.nodes} {this.state.description} {this.state.matrix}</h4>
          </div>
    )
  }
}