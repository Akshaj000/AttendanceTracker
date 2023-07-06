const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  loginUser(email, password)
    .then((data) => {
      // console.log("Success:", data);
      if (data.access && data.refresh) {
        localStorage.setItem("accessToken", data.access);
        localStorage.setItem("refreshToken", data.refresh);
        getUser(data.access)
          .then((user) => {
            if (user.is_staff) {
              window.location.href = "session.html";
            } 
            else if(user.is_staff === false) {
              window.location.href = "attendance.html";
            }
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      } else {
        showAlert("Invalid email or password. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});