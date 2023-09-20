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
