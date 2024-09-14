import api from '../../services/api';

export const fetchClassrooms = () => async (dispatch) => {
  dispatch({ type: 'FETCH_CLASSROOMS_REQUEST' });
  try {
    const response = await api.get('/classrooms');
    dispatch({ type: 'FETCH_CLASSROOMS_SUCCESS', payload: response.data });
  } catch (error) {
    dispatch({ type: 'FETCH_CLASSROOMS_FAILURE', payload: error.message });
  }
};

export const createClassroom = (classroomData) => async (dispatch) => {
  dispatch({ type: 'CREATE_CLASSROOM_REQUEST' });
  try {
    const response = await api.post('/classrooms', classroomData);
    dispatch({ type: 'CREATE_CLASSROOM_SUCCESS', payload: response.data });
  } catch (error) {
    dispatch({ type: 'CREATE_CLASSROOM_FAILURE', payload: error.message });
  }
};

// Add the missing actions below:

// Fetch details of a specific classroom
export const fetchClassroomDetail = (id) => async (dispatch) => {
  dispatch({ type: 'FETCH_CLASSROOM_DETAIL_REQUEST' });
  try {
    const response = await api.get(`/classrooms/${id}`);
    dispatch({ type: 'FETCH_CLASSROOM_DETAIL_SUCCESS', payload: response.data });
  } catch (error) {
    dispatch({ type: 'FETCH_CLASSROOM_DETAIL_FAILURE', payload: error.message });
  }
};

// Join a classroom
export const joinClassroom = (classroomId) => async (dispatch) => {
  dispatch({ type: 'JOIN_CLASSROOM_REQUEST' });
  try {
    const response = await api.post(`/classrooms/${classroomId}/join`);
    dispatch({ type: 'JOIN_CLASSROOM_SUCCESS', payload: response.data });
    return response.data;
  } catch (error) {
    dispatch({ type: 'JOIN_CLASSROOM_FAILURE', payload: error.message });
    throw error;
  }
};
