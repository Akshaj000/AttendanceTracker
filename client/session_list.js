// Fetch the access token from local storage
const accessToken = localStorage.getItem('accessToken');

// Function to format the date and time
function formatDate(dateTime) {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
  return new Date(dateTime).toLocaleDateString('en-US', options);
}

// Fetch session data from the API
listSessions(accessToken)
  .then((sessions) => {
    const sessionList = document.getElementById('session-list');
    const cardContainer = document.createElement('div');
    cardContainer.className = 'card-container';
    
    sessions.forEach((session) => {
      // Create a card element for each session
      const card = document.createElement('div');
      card.className = 'card';

      // Fill in session details
      const name = document.createElement('h2'); // Render name as a header
      name.textContent = session.name;
      card.appendChild(name);

      const startTime = document.createElement('p');
      startTime.textContent = `Start Time: ${formatDate(session.start_time)}`; // Process start time
      card.appendChild(startTime);

      const endTime = document.createElement('p');
      endTime.textContent = `End Time: ${formatDate(session.end_time)}`; // Process end time
      card.appendChild(endTime);

      const isAvailable = document.createElement('p');
      isAvailable.textContent = `Is Available: ${session.is_available}`;
      card.appendChild(isAvailable);
      if(session.is_available){
        card.style.border = "solid #00FF00";
      } else {
        card.style.border = "solid #FF0000";
      }
      
      const author = document.createElement('p');
      author.textContent = `Instructor: ${session.instructor}`; // Assuming 'author' field represents the instructor
      card.appendChild(author);

      // Append the card to the card container
      cardContainer.appendChild(card);
    });

    // Append the card container to the session list
    sessionList.appendChild(cardContainer);
  })
  .catch((error) => {
    console.error('Error fetching session data:', error);
  });
