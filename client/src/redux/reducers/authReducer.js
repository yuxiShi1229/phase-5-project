const initialState = {
    user: null,
    isAuthenticated: false,
    loading: false,
    error: null
  };
  
  const authReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'LOGIN_REQUEST':
        return { ...state, loading: true };
      case 'LOGIN_SUCCESS':
        return { ...state, user: action.payload, isAuthenticated: true, loading: false };
      case 'LOGIN_FAILURE':
        return { ...state, error: action.payload, loading: false };
      case 'LOGOUT':
        return { ...initialState };
      default:
        return state;
    }
  };
  
  export default authReducer;