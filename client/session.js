const sessionForm = document.getElementById('sessionForm');
const logoutButton = document.getElementById('logout-btn');
let access = localStorage.getItem('accessToken');
let refresh = localStorage.getItem('refreshToken');

function handleSessionCreation(sessionData) {
  return verifyToken(access)
    .then((isValid) => {
      if (isValid) {
        return createSession(access, sessionData);
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      return refreshToken(refresh)
        .then((data) => {
          if (data.access && data.refresh) {
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            access = data.access;
            refresh = data.refresh;
            return createSession(access, sessionData);
          } else {
            throw new Error('Token refresh failed');
          }
        });
    });
}


sessionForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const name = document.getElementById('name').value;
  const startTime = new Date(document.getElementById('startTime').value);
  const endTime = new Date(document.getElementById('endTime').value);

  const sessionData = {
    name,
    start_time: {
      year: startTime.getFullYear(),
      month: startTime.getMonth() + 1,
      day: startTime.getDate(),
      hour: startTime.getHours(),
      minute: startTime.getMinutes(),
    },
    end_time: {
      year: endTime.getFullYear(),
      month: endTime.getMonth() + 1,
      day: endTime.getDate(),
      hour: endTime.getHours(),
      minute: endTime.getMinutes(),
    },
  };

  try {
    let data = await handleSessionCreation(sessionData);
    console.log(data);
    document.getElementById("sessionKeyField").style.display = "block";
    document.getElementById("sessionKey").value = data?.key
  } catch (error) {
    console.error('Error:', error);
  }
});

logoutButton.addEventListener('click', () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  access = null;
  refresh = null;
  window.location.href = 'index.html';
});
