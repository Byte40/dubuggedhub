import { createRoot } from 'react-dom/client';

// Clear the existing HTML content
document.body.innerHTML = '<div id="app"></div>';

// Render your React component instead
const root = createRoot(document.getElementById('app'));
root.render(<h1>Hello, world</h1>);



// Function to handle scrolling
function handleScrolling() {
    const prevButton = document.querySelector(".prev-button"); // Get prev button
    const nextButton = document.querySelector(".next-button"); // Get next button
    const nav = document.querySelector(".navigation-bar nav"); // Get nav element
    const ul = document.querySelector(".navigation-bar ul"); // Get ul element

    let scrollPosition = 0; // Initialize scroll position

    // Function to scroll to the left
    prevButton.addEventListener("click", function () {
        scrollPosition -= 200; // Adjust scrolling distance
        if (scrollPosition < 0) {
            scrollPosition = 0; // Set minimum scroll position
        }
        nav.scrollTo({ // Scroll to the left
            left: scrollPosition,
            behavior: "smooth",
        });
    });

    // Function to scroll to the right
    nextButton.addEventListener("click", function () {
        scrollPosition += 200; // Adjust scrolling distance
        if (scrollPosition > ul.offsetWidth - nav.offsetWidth) {
            scrollPosition = ul.offsetWidth - nav.offsetWidth; // Set maximum scroll position
        }
        nav.scrollTo({ // Scroll to the right
            left: scrollPosition,
            behavior: "smooth",
        });
    });
}

// Call the function
handleScrolling();


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




