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

