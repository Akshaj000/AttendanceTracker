const keyForm = document.getElementById("key-form");
const logoutButton = document.getElementById("logout-btn");
let access = localStorage.getItem("accessToken");
let refresh = localStorage.getItem("refreshToken");

function handleAttendanceSubmission(key) {
  verifyToken(access)
    .then((isValid) => {
      if (isValid) {
        return recordAttendance(access, key);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      return refreshToken(refresh)
        .then((data) => {
          if (data.access && data.refresh) {
            localStorage.setItem("accessToken", data.access);
            localStorage.setItem("refreshToken", data.refresh);
            access = data.access;
            refresh = data.refresh;
            return recordAttendance(access, key);
          } else {
            throw new Error("Token refresh failed");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          throw new Error("Attendance recording failed");
        });
    })
    .then((data) => {
      if (data.message) {
        showAlert(data.message);
      } else {
        showAlert("Something went wrong. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

keyForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const key = document.getElementById("key").value;
  handleAttendanceSubmission(key);
});

logoutButton.addEventListener("click", () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  access = null;
  refresh = null;
  window.location.href = "login.html";
});
