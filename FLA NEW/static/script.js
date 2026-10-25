/**
 * Frontend JavaScript for Automata Spam Detection Project
 * B.Tech IT - Formal Language and Automata (21CSC301T)
 */

document.addEventListener("DOMContentLoaded", () => {
    // CSV file upload filename preview
    const fileInput = document.getElementById("csv_file");
    if (fileInput) {
        fileInput.addEventListener("change", (e) => {
            const fileName = e.target.files[0] ? e.target.files[0].name : "No file chosen";
            console.log("Selected file for schema inspection:", fileName);
        });
    }
});
