const contactForm = document.getElementById('contact-form');

function contact(e) {
    e.preventDefault(); // not sure if needed here

    // Get values from form fields
    let name = document.getElementById('contact-name').value;
    let email = document.getElementById('email').value;
    let hp_no = document.getElementById('phone-number').value;
    let offering_type = document.getElementById('service-type').value;

    console.log("Initiating API call to Lambda to handle contact form...")

    const payload = {
        name: name,
        email: email,
        hp_no: hp_no,
        offering_type: offering_type
    }

    console.log(payload)
    fetch("/api/contact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "same-origin",
        body: JSON.stringify({"body": payload}),
    })
    .then((res) => res.json())
    .then((output) => {
        if (output['success']) {
          console.log("api call success")
          console.log(output)
          let access_token = output['data']['access_token']
          // what does this do
          // document.location.href = "/upload/" + output['data']['content_id']
        } else {
          console.log("api call failed")
          // message = 'Access code not found! Try again.';
          // info = document.getElementById('status-info');
          // info.innerText = message;
          // info.style.visibility = "visible"
        }
    })
    .catch((err) => {
        console.log(err);
    });
};

const el = document.getElementById('contact-form');
if (el) {
  el.addEventListener('submit', contact);
}
