const loginForm = document.getElementById('login-form');

function login(e) {
    e.preventDefault();
    let access = document.getElementById('access-code').value;

    fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "same-origin",
        body: JSON.stringify({ access: access }),
    })
    .then((res) => res.json())
    .then((output) => {
        if (output['success']) {
            document.location.href = "/upload/" + output['data']['content_id']
        } else {
            message = 'Access code not found! Try again.';
            info = document.getElementById('status-info');
            info.innerText = message;
            info.style.visibility = "visible"
        }
    })
    .catch((err) => {
        console.log(err);
    });
};

loginForm.addEventListener('submit', login);
