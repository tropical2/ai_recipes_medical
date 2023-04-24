document.getElementById("my-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Hide the form and show the loading message
    document.getElementById("form-container").style.display = "none";
    document.getElementById("loading").style.display = "block";

    // Send a POST request with the form data
    fetch(submit_form_url, {
        method: "POST",
        body: new FormData(event.target)
    })
    .then(response => response.text())
    .then(output => {
        // Hide the loading icon and message
        document.getElementById("loading").style.display = "none";

        // Display the generated output text
        document.getElementById("output").style.display = "block";
        document.getElementById("output").innerText = output;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
