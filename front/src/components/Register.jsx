import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import axios from 'axios'
import Cookies from 'universal-cookie'
const cookies = new Cookies()

const BaseUrl = 'http://127.0.0.1:8000/api/user/'
export default class Register extends Component {
    state={
        form:{
            name:'',
            email:'',
            password:''
        }
    }
    handleChange=async e=>{
        await this.setState({
            form:{
                ...this.state.form,
                [e.target.name]: e.target.value
            }
        });
        console.log(this.state.form)
    }
    registrarUsuario= async()=>{
        console.log("registrando...");
        const formData = new FormData();

        formData.append('name', this.state.form.name);
        formData.append('password', this.state.form.password);
        formData.append('email', this.state.form.email);
        await axios.post(BaseUrl, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        })
        .then(response=>{
            return response.data
        })
        .then(response =>{
            if (response.length>0){
                var respuesta = response[0]
                alert('successfully registered user')
                window.location.href = './'
            }})
            .catch (error =>{
            if (error.response && error.response.status === 404) {
                alert('The user or password are not correct');
            } 
        })
    }
    componentDidMount(){
        if(cookies.get('id')){
            window.location.href = './menu'
        }
    }

    render() {
    return (
        <div className="bg-gradient-primary ">
            <div className="container" >
                <div className="card o-hidden border-0 shadow-lg my-5">
                    <div className="card-body p-0">
                    {/* <!-- Nested Row within Card Body --> */}
                        <div className="row">
                            <div className="col-lg-5 d-none d-lg-block bg-register-image"></div>
                            <div className="col-lg-7">
                                <div className="p-5">
                                    <div className="text-center">
                                        <h1 className="h4 text-gray-900 mb-4">Create an Account!</h1>
                                    </div>
                                    <form className="user">
                                        <div className="form-group ">
                                                <input type="text" className="form-control form-control-user" name='name' id="exampleFirstName" placeholder="Name" onChange={this.handleChange}/>
                                        </div>
                                        <div className="form-group">
                                            <input type="email" name='email' className="form-control form-control-user" id="exampleInputEmail" placeholder="Email Address" onChange={this.handleChange}/>
                                        </div>
                                        <div className="form-group">
                                                <input type="password" className="form-control form-control-user" name='password' id="exampleInputPassword" placeholder="Password" onChange={this.handleChange}/>
                                        </div>
                                        <button type="submit" className="btn btn-primary btn-user btn-block" onClick={(e) => {e.preventDefault(); this.registrarUsuario()}}>
                                            Register Account
                                        </button>
                                        <hr/>
                                        <a href="index.html" className="btn btn-google btn-user btn-block disabled">
                                            <i className="fab fa-google fa-fw"></i> Register with Google
                                        </a>
                                        <a href="index.html" className="btn btn-facebook btn-user btn-block disabled">
                                            <i className="fab fa-facebook-f fa-fw"></i> Register with Facebook
                                        </a>
                                    </form>
                                    <hr/>
                                    <div className="text-center disabled">
                                            <a className="small disabled" href="#">Forgot Password?</a>
                                    </div>
                                    <div className="text-center">
                                        <Link to="/" className="text-center small" >
                                            Already have an account? Login!
                                        </Link>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
    }
}
