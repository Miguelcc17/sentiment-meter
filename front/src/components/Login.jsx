// Login.jsx

import { Link } from 'react-router-dom';
import React, { Component } from 'react'
import axios from 'axios'
import Cookies from 'universal-cookie'

const BaseUrl = 'http://127.0.0.1:8000/api/user/'

const cookies = new Cookies()

export default class Login extends Component {
    state={
        form:{
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
    }
    iniciarSeccion= async()=>{
        console.log("Iniciando sesión...");
        await axios.get(BaseUrl, {params: {email: this.state.form.email, password: this.state.form.password}})
        .then(response=>{
            return response.data
        })
        .then(response =>{
            if (response.length>0){
                var respuesta = response[0]
                cookies.set('id', respuesta.id, {path: "/"})
                cookies.set('name', respuesta.name, {path: "/"})

                window.location.href = './menu'
            }else{
                alert('The user or password are not correct')
            }}
          )
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
        <div className="row justify-content-center">
        <div className="col-xl-10 col-lg-12 col-md-9">
          <div className="card o-hidden border-0 shadow-lg my-5">
            <div className="card-body p-0">
              <div className="row">
                <div className="col-lg-6 d-none d-lg-block bg-login-image"></div>
                <div className="col-lg-6">
                  <div className="p-5">
                    <div className="text-center">
                      <h1 className="h4 text-gray-900 mb-4">Welcome Back!</h1>
                    </div>
                    <form className="user" 
                    > 
                      <div className="form-group">
                        <input
                          type="email"
                          name='email'
                          className="form-control form-control-user"
                          id="exampleInputEmail"
                          aria-describedby="emailHelp"
                          placeholder="Enter Email Address..."
  
                          // value={email}
                          onChange={this.handleChange}
                        />
                      </div>
                      <div className="form-group">
                        <input
                          type="password"
                          name='password'
                          className="form-control form-control-user"
                          id="exampleInputPassword"
                          placeholder="Password"
                        
                          // value={password}
                          onChange={this.handleChange}
                        />
                      </div>
                      <div className="form-group">
                        <div className="custom-control custom-checkbox small">
                          <input
                            type="checkbox"
                            className="custom-control-input"
                            id="customCheck"
                          />
                          <label className="custom-control-label" htmlFor="customCheck">
                            Remember Me
                          </label>
                        </div>
                      </div>
                      <button type="submit" className="btn btn-primary btn-user btn-block" onClick={(e) => {e.preventDefault(); this.iniciarSeccion()}}>
                          Login
                      </button>
                      <hr />
                      <a href="index.html" className="btn btn-google btn-user btn-block disabled">
                        <i className="fab fa-google fa-fw"></i> Login with Google
                      </a>
                      <a href="index.html" className="btn btn-facebook btn-user btn-block disabled" >
                        <i className="fab fa-facebook-f fa-fw"></i> Login with Facebook
                      </a>
                    </form>
                    <hr />
                    <div className="text-center">
                      {/* <a className="small" href="forgot-password.html">
                        Forgot Password? 
                      </a> */}
                      <Link to="/register" className="small" >
                        Create an Account
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* <Routers /> */}
      </div>
    )
  }
}
