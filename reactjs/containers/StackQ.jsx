import React from "react";

export default class StackQ extends React.Component {
	constructor(props)
	{
		super(props);
		this.state = {
			arr: this.props.arr,
			arrName: this.props.arrName
		}
	}

	componentWillReceiveProps(nextProps){
		this.setState({
			arr: nextProps.arr,
			arrName: nextProps.arrName
		})
	}

	render(){
		var array = [] ;
		for (let i = 0 ; i < this.state.arr.length ; i++)
		{
			let x  = this.state.arr[i];
			if(1000000000000000000 == x)
			{
				// x = &infin;
				array.push(<div style={{border:"1px solid",width:"26px",display:"inline-block",textAlign:"center"}}>inf</div>)
			}
			else
			{
				array.push(<div style={{border:"1px solid",width:"26px",display:"inline-block",textAlign:"center"}}>{x}</div>)
			}
		}
		return (
			<div >{this.state.arrName}<br/>
			{array}
			</div>
		);
	}
}