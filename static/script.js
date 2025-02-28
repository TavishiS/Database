document.getElementById("signupForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const userData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
    };

    const response = await fetch("/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData),
    });

    const result = await response.json();
    document.getElementById("message").textContent = result.message;
    document.getElementById("message").style.color = response.ok ? "green" : "red";
});
