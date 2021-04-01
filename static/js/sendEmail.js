var emailjs;
function sendMail(contactForm){
    emailjs.send("gmail","bazaar",{
"from_name": contactForm.name.value,
"from_email": contactForm.emailaddress.value,
"projectsummary": contactForm.projectsummary.value
})
        .then(
            function(response) {
                var sentButton = document.getElementById("contact-button");
                sentButton.style.backgroundColor = "Green";
                sentButton.innerHTML = "Feedback Sent!";
                alert("Your feedback is submitted");
                },
                function(error) {
               alert("try again");
            });
       // Clear form after submission
            document.getElementById("contactForm").reset();
            return false;
    }
