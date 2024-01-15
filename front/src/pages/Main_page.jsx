import React, { Component} from 'react'
import Cookies from 'universal-cookie'
import Navar from '../components/Navar'
import Navarhead from '../components/Navarhead'
import RequestFile from '../components/RequestFile'


const cookies = new Cookies()

export default class Main_page extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: cookies.get('name'),
        };
    }

    cerrarSesion = () => {
        console.log('Cerrando sesión...');
        cookies.remove('id', {path: "/"})
        cookies.remove('name', {path: "/"})
        window.location.href = './'
    };

    componentDidMount(){
        if(!cookies.get('id')){
            window.location.href = './'
        }
    }
    render() {
        return (
            <div id="wrapper">
                <Navar/>
                <div id="content-wrapper" className="d-flex flex-column">
                    <div id="content">
                        <Navarhead name = {this.state.name} cerrarSesion={this.cerrarSesion}/>
                        <RequestFile/>
                    </div>
                </div>
            </div>
        )
    }
}
