import { combineReducers } from 'redux';
import authReducer from './authReducer';
import classroomReducer from './classroomReducer';

const rootReducer = combineReducers({
  auth: authReducer,
  classrooms: classroomReducer,
});

export default rootReducer;