import api from '../../services/api';

export const signup = (userData) => async (dispatch) => {
  dispatch({ type: 'SIGNUP_REQUEST' });
  try {
    console.log('Attempting signup with:', userData);
    const response = await api.post('/auth/signup', userData);
    console.log('Signup response:', response.data);
    dispatch({ type: 'SIGNUP_SUCCESS', payload: response.data });
  } catch (error) {
    console.error('Signup error:', error);
    if (error.response) {
      console.error('Error response:', error.response.data);
      dispatch({ type: 'SIGNUP_FAILURE', payload: error.response.data.error });
    } else if (error.request) {
      console.error('No response received:', error.request);
      dispatch({ type: 'SIGNUP_FAILURE', payload: 'No response from server' });
    } else {
      console.error('Error setting up request:', error.message);
      dispatch({ type: 'SIGNUP_FAILURE', payload: 'Error setting up request' });
    }
  }
};

export const login = (credentials) => async (dispatch) => {
  dispatch({ type: 'LOGIN_REQUEST' });
  try {
    console.log('Attempting login with:', credentials);
    const response = await api.post('/auth/login', credentials);
    console.log('Login response:', response.data);
    dispatch({ type: 'LOGIN_SUCCESS', payload: response.data });
  } catch (error) {
    console.error('Login error:', error);
    if (error.response) {
      console.error('Error response:', error.response.data);
      dispatch({ type: 'LOGIN_FAILURE', payload: error.response.data.error });
    } else if (error.request) {
      console.error('No response received:', error.request);
      dispatch({ type: 'LOGIN_FAILURE', payload: 'No response from server' });
    } else {
      console.error('Error setting up request:', error.message);
      dispatch({ type: 'LOGIN_FAILURE', payload: 'Error setting up request' });
    }
  }
};
