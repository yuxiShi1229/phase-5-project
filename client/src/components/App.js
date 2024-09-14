import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import Login from './Auth/Login';
import Signup from './Auth/Signup';
import ClassroomList from './Classroom/ClassroomList';
import ClassroomDetail from './Classroom/ClassroomDetail';

function PrivateRoute({ children }) {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated);
  return isAuthenticated ? children : <Navigate to="/auth" />;
}

function AuthPage() {
  return (
    <div>
      <Login />
      <Signup />
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/auth" element={<AuthPage />} />
          <Route path="/" element={
            <PrivateRoute>
              <ClassroomList />
            </PrivateRoute>
          } />
          <Route path="/classroom/:id" element={
            <PrivateRoute>
              <ClassroomDetail />
            </PrivateRoute>
          } />
          <Route path="*" element={<Navigate to="/auth" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;