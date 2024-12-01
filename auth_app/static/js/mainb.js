const navTElement = document.querySelector(".menu_icon");
const flexContainer = document.querySelector(".hide");
const listItem = document.querySelectorAll(".li_mobile");
navTElement.addEventListener("click", () => {
    flexContainer.classList.toggle("unhide");
});
listItem.forEach((liItem) => {
    liItem.addEventListener("click", () => {
        flexContainer.classList.remove("unhide");
    });
});