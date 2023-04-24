console.log("Start of main.js script");
document.getElementById("my-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Hide the form and show the loading message
    document.getElementById("form-container").style.display = "none";
    console.log("stopped displaying form");
    document.getElementById("loading").style.display = "block";
    console.log("Started displaying loading block");

    // Send a POST request with the form data
    fetch(submit_form_url, {
        method: "POST",
        body: new FormData(event.target)
    })
    .then(response => response.text())
    .then(output => {
        // Hide the loading icon and message
        document.getElementById("loading").style.display = "none";
        console.log("Stopped displaying loading block");

        // Display the generated output text
        document.getElementById("output").style.display = "block";
        document.getElementById("output").innerText = output;
        console.log("Started displaying output text");

    })
    .catch(error => {
        console.error("Error:", error);
    });
});
