const contactForm = document.getElementById('contact-form');

function contact(e) {
    e.preventDefault(); // not sure if needed here

    // Get values from form fields
    let name = document.getElementById('contact-name');
    let email = document.getElementById('email');
    let hp_no = document.getElementById('phone-number');
    let offering_type = document.getElementById('service-type');

    // only reads in null values weird
    console.log("Name: " + name)
    console.log("Email: " + email)
    console.log("Phone Number: " + hp_no)
    console.log("Offering Type: " + offering_type)
    console.log("Initiating API call to Lambda to handle contact form...")

    // fetch("/api/contact", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //     },
    //     credentials: "same-origin",
    //     body: JSON.stringify({ access: access }),
    // })
    // .then((res) => res.json())
    // .then((output) => {
    //     if (output['success']) {
    //         document.location.href = "/upload/" + output['data']['content_id']
    //     } else {
    //         message = 'Access code not found! Try again.';
    //         info = document.getElementById('status-info');
    //         info.innerText = message;
    //         info.style.visibility = "visible"
    //     }
    // })
    // .catch((err) => {
    //     console.log(err);
    // });
};

const el = document.getElementById('contact-form');
if (el) {
  el.addEventListener('submit', contact);
}
