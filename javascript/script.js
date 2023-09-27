document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const themeToggleButton = document.getElementById("theme-toggle-button");
    const themeMenu = document.getElementById("theme-menu");

    // Check the user's preference for theme (light or dark) from localStorage
    const userThemePreference = localStorage.getItem("theme");

    // Apply the user's theme preference or default to auto
    if (userThemePreference === "dark") {
        body.classList.add("dark-theme");
    } else if (userThemePreference === "light") {
        body.classList.remove("dark-theme");
    } else {
        // Auto theme based on system preference
        if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
            body.classList.add("dark-theme");
        }
    }

    // Function to toggle the theme menu
    function toggleThemeMenu() {
        // Toggle the visibility class
        themeMenu.classList.toggle("visible");
    }

    // Event listener for theme toggle button
    themeToggleButton.addEventListener("click", toggleThemeMenu);

    // Function to toggle between dark and light themes
    function toggleTheme(event) {
        if (event.target.id === "dark-theme") {
            body.classList.add("dark-theme");
            localStorage.setItem("theme", "dark");
        } else if (event.target.id === "light-theme") {
            body.classList.remove("dark-theme");
            localStorage.setItem("theme", "light");
        }
        // Close the theme menu
        toggleThemeMenu();
    }

    // Event listeners for theme menu items
    const themeMenuItems = document.querySelectorAll(".theme-menu a");
    themeMenuItems.forEach((item) => {
        item.addEventListener("click", toggleTheme);
    });
});


