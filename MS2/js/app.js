const API = "http://127.0.0.1:5000";

async function signup() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    await fetch(API + "/auth/signup", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    });

    alert("Signup successful!");
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(API + "/auth/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (data.token) {
        localStorage.setItem("token", data.token);

        if (data.role === "admin") {
            window.location = "admin.html";
        } else {
            window.location = "dashboard.html";
        }
    } else {
        alert("Login failed");
    }
}