import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchClassrooms, createClassroom } from '../../redux/actions/classroomActions'; // Add createClassroom
import { Link } from 'react-router-dom';

function ClassroomList() {
  const dispatch = useDispatch();
  const { classrooms, loading, error } = useSelector(state => state.classrooms);
  const { user } = useSelector(state => state.auth);  // Access the authenticated user
  const [newClassroom, setNewClassroom] = useState({ name: '', description: '' });

  useEffect(() => {
    dispatch(fetchClassrooms());
  }, [dispatch]);

  const handleCreateClassroom = () => {
    if (user.isTeacher) {
      dispatch(createClassroom(newClassroom));
      setNewClassroom({ name: '', description: '' }); // Clear form
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Classrooms</h1>
      {user.isTeacher && (
        <div>
          <h3>Create Classroom</h3>
          <input
            type="text"
            value={newClassroom.name}
            onChange={e => setNewClassroom({ ...newClassroom, name: e.target.value })}
            placeholder="Classroom Name"
          />
          <input
            type="text"
            value={newClassroom.description}
            onChange={e => setNewClassroom({ ...newClassroom, description: e.target.value })}
            placeholder="Classroom Description"
          />
          <button onClick={handleCreateClassroom}>Create</button>
        </div>
      )}
      <ul>
        {classrooms.map(classroom => (
          <li key={classroom.id}>
            <Link to={`/classroom/${classroom.id}`}>{classroom.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ClassroomList;
