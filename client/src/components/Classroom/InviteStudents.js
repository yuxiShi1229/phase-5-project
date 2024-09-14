import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { inviteStudent } from '../../redux/actions/classroomActions';  // Assuming you have inviteStudent action

function InviteStudents({ classroomId }) {
  const [email, setEmail] = useState('');
  const dispatch = useDispatch();

  const handleInvite = () => {
    if (email) {
      dispatch(inviteStudent(classroomId, email));  // Dispatch invite action
      setEmail('');  // Clear the input field after sending
    }
  };

  return (
    <div>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Student Email"
      />
      <button onClick={handleInvite}>Invite</button>
    </div>
  );
}

export default InviteStudents;
