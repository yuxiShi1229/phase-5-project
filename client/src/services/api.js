import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api',  // Make sure this points to your Flask API
  withCredentials: true,  // Allow cookies/credentials to be sent
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

api.interceptors.request.use(request => {
  console.log('Starting Request', JSON.stringify(request, null, 2));
  return request;
});

api.interceptors.response.use(response => {
  console.log('Response:', JSON.stringify(response, null, 2));
  return response;
}, error => {
  console.log('Error:', error);
  if (error.response) {
    console.log('Error Data:', error.response.data);
    console.log('Error Status:', error.response.status);
    console.log('Error Headers:', error.response.headers);
  }
  return Promise.reject(error);
});

export default api;
