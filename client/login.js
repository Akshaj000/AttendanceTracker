const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  loginUser(email, password)
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