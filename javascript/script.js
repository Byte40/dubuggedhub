document.addEventListener("DOMContentLoaded", function () {
    const prevButton = document.querySelector(".prev-button");
    const nextButton = document.querySelector(".next-button");
    const nav = document.querySelector(".navigation-bar nav");
    const ul = document.querySelector(".navigation-bar ul");

    let scrollPosition = 0;

    // Function to scroll to the left
    prevButton.addEventListener("click", function () {
        scrollPosition -= 200; // Adjust the scrolling distance as needed
        if (scrollPosition < 0) {
            scrollPosition = 0;
        }
        nav.scrollTo({
            left: scrollPosition,
            behavior: "smooth",
        });
    });

    // Function to scroll to the right
    nextButton.addEventListener("click", function () {
        scrollPosition += 200; // Adjust the scrolling distance as needed
        if (scrollPosition > ul.offsetWidth - nav.offsetWidth) {
            scrollPosition = ul.offsetWidth - nav.offsetWidth;
        }
        nav.scrollTo({
            left: scrollPosition,
            behavior: "smooth",
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    // Get references to the search input and button
    const searchInput = document.getElementById("search-input");
    const searchButton = document.getElementById("search-button");

    // Function to perform the search
    function performSearch() {
        const query = searchInput.value.trim(); // Get the trimmed query

        // Perform your search logic here
        // You can redirect to a search results page or display results on the same page

        // For demonstration purposes, let's alert the query
        alert(`Searching for: ${query}`);
    }

    // Attach the search function to the button click event
    searchButton.addEventListener("click", performSearch);

    // Attach the search function to the Enter key press in the input field
    searchInput.addEventListener("keyup", function (event) {
        if (event.key === "Enter") {
            performSearch();
        }
    });
});




