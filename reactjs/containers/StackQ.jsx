import React from "react";

export default class StackQ extends React.Component {
	constructor(props)
	{
		super(props);
		this.state = {
			arr: this.props.arr,
			arrType: this.props.arrType
		}
	}

	componentWillReceiveProps(nextProps){
		this.setState({
			arr: nextProps.arr,
			arrType: nextProps.arrType
		})
	}

	render(){
		var array = [] ;
		for (let i = 0 ; i < this.state.arr.length ; i++)
		{
			array.push(<div style={{border:"1px solid",width:"26px",display:"inline-block",textAlign:"center"}}>{this.state.arr[i]}</div>)
		}
		return (
			<div >{this.state.arrType}<br/>
			{array}
			</div>
		);
	}
}