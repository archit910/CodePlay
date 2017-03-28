import React from "react";
import axios from 'axios';

import cytoscape from 'cytoscape';
import cytoscapeDagre from 'cytoscape-dagre'

import Headline from "../components/Headline"
import ControlPanel from "./ControlPanel"

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
      x : y,
      start: 'n0',
      end: 'n0',
      data: '',
      style: '',
      elements:''
    }

    //Functions bindings
    this.renderCytoscapeElement = this.renderCytoscapeElement.bind(this);
    this.onClickPrevButton = this.onClickPrevButton.bind(this);
    this.onClickNextButton = this.onClickNextButton.bind(this);
    this.updateAlgo = this.updateAlgo.bind(this);
    this.updateNumberOfNodes = this.updateNumberOfNodes.bind(this);
    this.updateMatrix = this.updateMatrix.bind(this);
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
    console.log("dsfs");
    var qs = require('qs');
    axios.post('/solve/',
      qs.stringify({
        id : 1234,
        matrix : this.state.matrix,
        algo : this.state.algo,
        nodes : this.state.nodes,
        step : this.state.step,
        start: 0,
        
      })
    )
    .then(function (response){
      console.log(response.data)
      this.setState({
        data: response.data.data,
        step: 0
      })
    }.bind(this))
  }


  onClickNextButton(){
    var step = this.state.step;
    this.setState({
      step: step + 1,
      style:this.state.data[step].style,
      elements: this.state.data[step].elements
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

    return (
          <div>
            <div className="row">
              <div className="col-sm-5 col-md-5 border" style={cyStyle1}>
                <ControlPanel updateAlgo={this.updateAlgo} updateNumberOfNodes={this.updateNumberOfNodes} updateMatrix={this.updateMatrix}/>
              </div>
              <div className="col-sm-4 col-md-4 border" style={cyStyle1}>
                <h4>Visual</h4>
                <button className="btn btn-primary" onClick={this.onClickPrevButton}> - Previous </button>
                <button className="btn btn-primary" onClick={this.onClickNextButton}> Next - </button>
                <div id="cy-container" >
                          <div style={cyStyle} id="cy1"></div>
                    </div>
              </div>
              <div className="col-sm-3 col-md-3 border" style={cyStyle1}>
                <h4>Code Panel</h4>
              </div>
            </div>
            <h4>Description of The Algorithm : {this.state.algo} {this.state.nodes} {this.state.description} {this.state.matrix}</h4>
          </div>
    )
  }
}