// login.js
const loginForm = document.getElementById("login-form");

function showAlert(message) {
  const customAlert = document.getElementById("custom-alert");
  const customAlertMessage = document.querySelector(".custom-alert-message");
  const customAlertCloseBtn = document.getElementById("custom-alert-close-btn");

  customAlertMessage.textContent = message;
  customAlert.style.display = "flex";

  customAlertCloseBtn.addEventListener("click", function () {
    customAlert.style.display = "none";
  });
}

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  fetch("http://localhost:8000/api/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      if (data.access && data.refresh) {
        localStorage.setItem("accessToken", data.access);
        localStorage.setItem("refreshToken", data.refresh);
        window.location.href = "attendance.html";
      } else {
        showAlert("Invalid email or password. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
