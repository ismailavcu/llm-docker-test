const textInput = document.getElementById("textInput");
const summarizeButton = document.getElementById("summarizeButton");
const summary = document.getElementById("summary");
const loading = document.getElementById("loading");

summarizeButton.addEventListener("click", async () => {

    const text = textInput.value.trim();

    if (!text) {
        summary.textContent = "Please enter some text.";
        return;
    }

    loading.style.display = "block";
    summary.textContent = "";

    try {
        const response = await fetch("http://localhost:8000/summarize", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        summary.textContent = data.summary;

    } catch (error) {
        summary.textContent = "Error: " + error.message;
    }

    loading.style.display = "none";
});