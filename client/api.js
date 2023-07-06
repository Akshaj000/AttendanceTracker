async function loginUser(email, password) {
    const response = await fetch("http://localhost:8000/api/login/", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
        return response.json();
    } else {
        return {};
    }
}

async function getUser(accessToken){
    const response = await fetch("http://localhost:8000/api/user/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    });
    if (response.ok) {
        return response.json();
    } else {
        throw new Error("User retrieval failed");
    }
}

async function verifyToken(accessToken) {
    const response = await fetch("http://localhost:8000/api/token/verify/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ token: accessToken }),
    });
    if (response.status === 200) {
        return true; // Token is valid
    } else {
        throw new Error("Token verification failed");
    }
  }
  
async function refreshToken(refreshToken) {
    const response = await fetch("http://localhost:8000/api/token/refresh/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ refresh: refreshToken }),
    });
    if (response.ok) {
        return response.json();
    } else {
        throw new Error("Token refresh failed");
    }
  }


async function recordAttendance(accessToken, key) {
    const response = await fetch("http://localhost:8000/api/session/record/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({ key }),
    });
    return response.json();
}

async function createSession(accessToken, sessionData) {
    const response = await fetch('http://localhost:8000/api/session/create/', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify(sessionData),
    });
    if(response.status == 200){
        return response.json()
    }
    return {}
}
