import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InitialPage from './Initial_page.jsx';
import Register from '../components/Register.jsx';
import Main_page from './Main_page.jsx';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InitialPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/menu" element={<Main_page />} />
      </Routes>
    </Router>
  );
}

export default App;
