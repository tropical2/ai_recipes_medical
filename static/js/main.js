console.log("Start of main.js script");

function updateInfo() {
    const dropdown = document.getElementById("dropdown");
    const info = document.getElementById("info");

    if (dropdown.value === "LPR") {
        info.innerHTML = "Will avoid typical reflux trigger foods like garlic, spicy foods, fried foods, chocolate, etc. Also avoids low pH foods which can reactivate the stomach enzyme pepsin in the throat.";
    } else if (dropdown.value === "GERD") {
        info.innerHTML = "Will avoid typical reflux trigger foods like garlic, spicy foods, fried foods, chocolate, etc.";
    } else if (dropdown.value === "SIBO") {
        info.innerHTML = "Avoids SIBO trigger foods. Will create low FODMAP recipes. Avoids sugar.";
    }

    if (dropdown.value) {
        info.style.display = "block";
    } else {
        info.style.display = "none";
    }
}

document.getElementById("dropdown").addEventListener("change", updateInfo);

document.getElementById("my-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Hide the form and show the loading message
    document.getElementById("form-container").style.display = "none";
    console.log("stopped displaying form");
    document.getElementById("loading").style.display = "block";
    console.log("Started displaying loading block");
    sendHeightToParent();

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
        sendHeightToParent();

    })
    .catch(error => {
        console.error("Error:", error);
    });
});

updateInfo(); // Update the info text when the page loads


// give height information to hosting page so that the iframe can be displayed without scrolling. Needs to be triggered during functions that lead to resizing of the page.
function sendHeightToParent() {
  const height = document.documentElement.scrollHeight;
  window.parent.postMessage({ type: 'adjustHeight', height: height }, '*');
}

// Send the initial height.
sendHeightToParent();
