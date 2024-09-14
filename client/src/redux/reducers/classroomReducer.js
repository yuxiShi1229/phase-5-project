const initialState = {
    classrooms: [],
    currentClassroom: null,
    loading: false,
    error: null
  };
  
  const classroomReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'FETCH_CLASSROOMS_REQUEST':
      case 'FETCH_CLASSROOM_DETAIL_REQUEST':
      case 'JOIN_CLASSROOM_REQUEST':
        return { ...state, loading: true };
  
      case 'FETCH_CLASSROOMS_SUCCESS':
        return { ...state, classrooms: action.payload, loading: false };
  
      case 'FETCH_CLASSROOM_DETAIL_SUCCESS':
        return { ...state, currentClassroom: action.payload, loading: false };
  
      case 'JOIN_CLASSROOM_SUCCESS':
        return { ...state, loading: false };
  
      case 'FETCH_CLASSROOMS_FAILURE':
      case 'FETCH_CLASSROOM_DETAIL_FAILURE':
      case 'JOIN_CLASSROOM_FAILURE':
        return { ...state, error: action.payload, loading: false };
  
      default:
        return state;
    }
  };
  
  export default classroomReducer;
  