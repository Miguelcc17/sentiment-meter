import React, { Component } from 'react'

export default class Prueba extends Component {
    render() {
        const { text, emotions } = this.props;

    // console.log('Texto:', text);
    // console.log('Emociones:', emotions);
    return (
        
            <div className="card" >
                <div className="card-header text-center">
                    {text}
                </div>
                <div className="card-body">
                    <p className='text-center'>{emotions[0].label} {emotions[0].score.toFixed(2)}%</p>
                    <p className='text-center'>{emotions[1].label} {emotions[1].score.toFixed(2)}%</p>
                </div>
            </div> 
    )
    }
}
