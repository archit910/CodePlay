import React from "react";
import cytoscape from 'cytoscape';
import cytoscapeDagre from 'cytoscape-dagre'

import Headline from "../components/Headline"

cytoscapeDagre(cytoscape);

export default class App1Container extends React.Component {
  constructor(props){
    super(props);

    this.renderCytoscapeElement = this.renderCytoscapeElement.bind(this);
  }

  renderCytoscapeElement(){

        console.log('* Cytoscape.js is rendering the graph..');

        this.cy = cytoscape(
        {
            container: document.getElementById('cy1'),

            boxSelectionEnabled: false,
            autounselectify: true,

            style: cytoscape.stylesheet()
                .selector('node')
                .css({
                    'content': 'data(id)',
                    'text-opacity': 0.5,
                    'text-valign': 'center',
                    'text-halign': 'right',
                    'background-color': '#11479e'
                })
                .selector('edge')
                .css({
                    'width': 4,
                    'target-arrow-shape': 'triangle',
                    'line-color': '#9dbaea',
                    'target-arrow-color': '#9dbaea',
                    'curve-style': 'bezier'
                })
                ,
            elements: {
                nodes: [
              { data: { id: 'n0' } },
              { data: { id: 'n1' } },
              { data: { id: 'n2' } },
              { data: { id: 'n3' } },
              { data: { id: 'n4' } },
              { data: { id: 'n5' } },
              { data: { id: 'n6' } },
              { data: { id: 'n7' } },
              { data: { id: 'n8' } },
              { data: { id: 'n9' } },
              { data: { id: 'n10' } },
              { data: { id: 'n11' } },
              { data: { id: 'n12' } },
              { data: { id: 'n13' } },
              { data: { id: 'n14' } },
              { data: { id: 'n15' } },
              { data: { id: 'n16' } }
            ],
                edges: [
              { data: { source: 'n0', target: 'n1' } },
              { data: { source: 'n1', target: 'n2' } },
              { data: { source: 'n1', target: 'n3' } },
              { data: { source: 'n4', target: 'n5' } },
              { data: { source: 'n4', target: 'n6' } },
              { data: { source: 'n6', target: 'n7' } },
              { data: { source: 'n6', target: 'n8' } },
              { data: { source: 'n8', target: 'n9' } },
              { data: { source: 'n8', target: 'n10' } },
              { data: { source: 'n11', target: 'n12' } },
              { data: { source: 'n12', target: 'n13' } },
              { data: { source: 'n13', target: 'n14' } },
              { data: { source: 'n13', target: 'n15' } },
              { data: { source: 'n0', target: 'n15' } },
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
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Sample App!</Headline>
            <div className="row">
              <div className="col-sm-4 col-md-4 border">
                <h4>Control Panel</h4>
              </div>
              <div className="col-sm-4 col-md-4 border" style={cyStyle1}>
                <h4>Visual</h4>
                <button className="btn btn-primary"> - Previous </button>
                <button className="btn btn-primary"> Next - </button>
                <div id="cy-container" >
                          <div style={cyStyle} id="cy1"></div>
                    </div>
              </div>
              <div className="col-sm-4 col-md-4 border">
                <h4>Code Panel</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}