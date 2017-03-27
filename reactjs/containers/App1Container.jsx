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
      end: 'n0'
    }

    //Functions bindings
    this.renderCytoscapeElement = this.renderCytoscapeElement.bind(this);
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

  onClickNextButton(){
    console.log("dsfs");
    var qs = require('qs');
    axios.post('/solve/',
      qs.stringify({
        id : 1234,
        matrix : this.state.matrix,
        algo : this.state.algo,
        nodes : this.state.nodes,
        step : this.state.step
      })
    )
    .then(function (response){
      console.log(response.data)
      this.setState({
        x: response.data.style
      })
    }.bind(this))
    this.setState({
      abc:'false'
    })
  }

  renderCytoscapeElement(){

        console.log('* Cytoscape.js is rendering the graph..');

        

        this.cy = cytoscape(
        {
            container: document.getElementById('cy1'),

            boxSelectionEnabled: false,
            autounselectify: true,

            style: [
            {
              selector: 'node',
              style: this.state.x
            },

            {
              'selector': 'edge',
              style: {
                width: 3,
                'target-arrow-shape': 'triangle',
                'line-color': '#9dbaea',
                'target-arrow-color': '#9dbaea',
                'curve-style': 'bezier',
                // 'opacity' : '0',
              }
            },


          ]
                ,
            elements: {
                nodes: [
              { data: { id: 'n0' } },
              { data: { id: 'n1' } },
              { data: { id: 'n2' } },
              { data: { id: 'n3' } },
              { data: { id: 'n4' } },
              { data: { id: 'n5' } },
              

              
            ],
                edges: [
              
              { data: { source: 'n1', target: 'n5' } },
              { data: { source: 'n0', target: 'n3' } },
              { data: { source: 'n0', target: 'n4' } },
              { data: { source: 'n4', target: 'n5' } },
              
              { data: { source: 'n3', target: 'n4' } },
              { data: { source: 'n4', target: 'n1' } },
              { data: { source: 'n3', target: 'n1' } },
              { data: { source: 'n0', target: 'n5' } },
              
              { data: { source: 'n3', target: 'n5' } },
              
              
              
              
              
            ]
            },

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
                <button className="btn btn-primary" onClick={this.onClickNextButton}> - Previous </button>
                <button className="btn btn-primary"> Next - </button>
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