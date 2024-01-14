import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InitialPage from './Initial_page.jsx';
import Register from '../components/Register.jsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InitialPage />} />
        <Route path="/register" element={<Register />} />

      </Routes>
    </Router>
  );
}

export default App;
