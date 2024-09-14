import React, { useEffect } from 'react';
import { useDyteMeeting, DyteProvider } from '@dytesdk/react-web-core';
import { DyteMeeting } from '@dytesdk/react-ui-kit';

function DyteComponent({ meetingId, participantToken }) {
  const { meeting, initMeeting } = useDyteMeeting();

  useEffect(() => {
    const init = async () => {
      await initMeeting({
        roomName: meetingId,
        authToken: participantToken,
        defaults: {
          audio: false,
          video: false,
        },
      });
    };

    init();
  }, [meetingId, participantToken, initMeeting]);

  if (!meeting) {
    return <div>Loading...</div>;
  }

  return (
    <DyteProvider value={meeting}>
      <DyteMeeting meeting={meeting} />
    </DyteProvider>
  );
}

export default DyteComponent;