//document.addEventListener("DOMContentLoaded", function() {
//    document.querySelectorAll(".nav-link").forEach(link => {
//        link.addEventListener("click", function(e) {
//            e.preventDefault();  // Prevent default navigation
//
//            fetch(this.href) // Fetch the new page
//                .then(response => response.text())
//                .then(html => {
//                    document.querySelector("#content").innerHTML = html; // Replace content
//                    window.history.pushState({}, "", this.href); // Update URL
//
//                    // ✅ Force Tailwind to reapply styles
//                    if (window.tailwind) {
//                        setTimeout(() => window.tailwind.init(), 0);
//                    }
//                });
//        });
//    });
//});


const download = document.getElementById("download");
const menuButtons = document.querySelectorAll('#menu button');

document.getElementById("menu-btn").addEventListener("click", function() {
    const menu = document.getElementById("menu");
    menu.classList.toggle("hidden");
});

download.addEventListener('click', function(){
    const file = "../files/Lacap, Karl Bastian Cunanan CV.pdf";

    const fileName = "CV";

    const link = document.createElement("a");

    link.href = file;

    link.download = fileName;

    link.click();

});

menuButtons.forEach(button => {
    button.addEventListener('click', function() {
        const menu = document.getElementById("menu");
        menu.classList.add("hidden");
    });
});
