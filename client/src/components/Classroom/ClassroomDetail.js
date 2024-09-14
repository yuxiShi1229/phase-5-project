import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchClassroomDetail, joinClassroom } from '../../redux/actions/classroomActions';
import DyteComponent from './DyteComponent';

function ClassroomDetail() {
  const { id } = useParams();
  const dispatch = useDispatch();
  const classroom = useSelector(state => state.classrooms.currentClassroom);
  const [message, setMessage] = useState('');
  const [dyteConfig, setDyteConfig] = useState(null);

  useEffect(() => {
    dispatch(fetchClassroomDetail(id));
  }, [dispatch, id]);

  useEffect(() => {
    if (classroom) {
      dispatch(joinClassroom(id)).then(response => {
        setDyteConfig({
          meetingId: response.dyte_meeting_id,
          participantToken: response.participant_token
        });
      });
    }
  }, [dispatch, id, classroom]);

  const handleSendMessage = (e) => {
    e.preventDefault();
    setMessage('');
  };

  if (!classroom) return <div>Loading...</div>;

  return (
    <div>
      <h2>{classroom.name}</h2>
      <p>{classroom.description}</p>
      <div>
        {dyteConfig && <DyteComponent meetingId={dyteConfig.meetingId} participantToken={dyteConfig.participantToken} />}
      </div>
      <div>
        <h3>Chat</h3>
        <form onSubmit={handleSendMessage}>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type a message..."
          />
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
}

export default ClassroomDetail;
