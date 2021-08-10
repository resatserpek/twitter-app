import Graph from "react-graph-vis";
import React from "react";

const Network = (props) => {
  
  const processData = (input) => {
    var nodes = []
    var edges = []
    input.nodes.forEach(element => {
      const node = {
        id: element.id,
        label: element.id,
        shape: "circularImage", 
        image: element.data.pic
      }
      nodes.push(node)
    });
        
    input.links.forEach(el =>{
      const edge = {
        from: el.target,
        to: el.source
      }
      edges.push(edge)
    })

    return {nodes: nodes, edges: edges}
  }
    
    
      const options = {
        layout: {
          hierarchical: false
        },
        edges: {
          color: "#000000"
        },
        height: "450px"
      };
    
    const events = {
      select: function(event) {
        var { nodes, edges } = event;
      }
    };
    return (
        <div>
            <Graph
              key
              graph={processData(props.data)}
              options={options}
              events={events}
              getNetwork={network => {
                //  if you want access to vis.js network api you can set the state in a parent component using this property
              }}
            />
        </div>
    )
}


export default React.memo(Network);