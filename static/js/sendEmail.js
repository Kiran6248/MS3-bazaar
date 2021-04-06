//Javascript code to send email through emailjs.init
//The JS code for this section is referred from my Milestone 2 project

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
                alert("Your feedback is submitted", response);
                },
                function(error) {
               alert("try again", error);
            });
       // Clear form after submission
            document.getElementById("contactForm").reset();
            return false;
    }
