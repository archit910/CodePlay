import React from "react";

export default class Input extends React.Component {

	constructor(props){
		super(props);
		this.state = {
			value : this.renderDefault(this.props.value, '')
		}
		// console.log("dsfsdfsdf",this.props.value,"dsfsd",this.state.value);
		this.renderDefault = this.renderDefault.bind(this);
		this.handleOnChange = this.handleOnChange.bind(this);
	}

	handleOnChange(event) {
        this.setState({value: event.target.value});

        if (this.props.onChange){
            this.props.onChange(event);
        }
    }

	renderDefault(value , defaultValue){
		// console.log("dsfj334432")
		return typeof value !== 'undefined' ? value : defaultValue;
	}

	componentWillReceiveProps(nextProps) {
    this.setState({value: nextProps.value});
	}

	render(){

		return(<input type="text"
                      size={this.renderDefault(this.props.size, 1)}
                     value={this.state.value}
                  onChange={this.handleOnChange}
               placeholder={this.renderDefault(this.props.placeholder, '')}
               style={{width:"40px"}}
                    />)
	}

}