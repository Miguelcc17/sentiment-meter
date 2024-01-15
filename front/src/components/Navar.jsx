import React from 'react'

function Navar() {
  return (
    <div>
        <ul className="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

        {/* <!-- Sidebar - Brand --> */}
        <a className="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
            <div className="sidebar-brand-icon rotate-n-15">
                <i className="fas fa-laugh-wink"></i>
            </div>
            <div className="sidebar-brand-text mx-3">Setiment Emotion <sup>1.0</sup></div>
        </a>

        {/* <!-- Divider --> */}
        <hr className="sidebar-divider my-0"/>

        {/* <!-- Nav Item - Dashboard --> */}
        <li className="nav-item disabled">
            <a className="nav-link disabled" href="index.html">
                <i className="fas fa-fw fa-tachometer-alt"></i>
                <span>Dashboard</span></a>
        </li>

        {/* <!-- Divider --> */}
        <hr className="sidebar-divider"/>

        {/* <!-- Heading --> */}
        <div className="sidebar-heading">
            Interface
        </div>

        
    

        {/* <!-- Nav Item - Utilities Collapse Menu --> */}
        <li className="nav-item">
            <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities"
                aria-expanded="true" aria-controls="collapseUtilities">
                <i className="fas fa-fw fa-wrench"></i>
                <span>Utilities</span>
            </a>
            <div id="collapseUtilities" className="collapse" aria-labelledby="headingUtilities"
                data-parent="#accordionSidebar">
                <div className="bg-white py-2 collapse-inner rounded">
                    <h6 className="collapse-header">Custom Utilities:</h6>
                    <a className="collapse-item" href="utilities-color.html">Colors</a>
                    <a className="collapse-item" href="utilities-border.html">Borders</a>
                    <a className="collapse-item" href="utilities-animation.html">Animations</a>
                    <a className="collapse-item" href="utilities-other.html">Other</a>
                </div>
            </div>
        </li>


       

        </ul>
    </div>
  )
}

export default Navar