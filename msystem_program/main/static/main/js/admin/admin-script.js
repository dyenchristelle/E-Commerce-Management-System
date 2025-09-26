// for admin 
// try lang, pero wala pa db kaya di natapos
document.addEventListener("DOMContentLoaded", function() {
    const login_button = document.getElementById("login_button");

    const form = document.getElementById("admin-login");
    if (!form) {
        console.error("Form not found!");
        return;
    }
    console.log("login loaded successfully!");

    if(login_button) {
        login_button.addEventListener("click", async function (event) {
        event.preventDefault();

        const admin_username = document.getElementById("admin_username").value;
        const admin_pass = document.getElementById("admin_pass").value;
        const errorMessage = document.getElementById("errorMessage");

        if (!admin_username || !admin_pass) {
            errorMessage.style.display = "block";
            errorMessage.textContent = "Please fill out both fields.";
        } else if (admin_username === "admin" && admin_pass === "admincpe6") {
            window.location.href = admin_home;
        } else {
            errorMessage.style.display = "block";
            errorMessage.textContent = "Input doesn't match.";
        }

        });
    }
});


// admin login successful > products
document.addEventListener("DOMContentLoaded", function() {
    const products = document.getElementById("products");

    if (products) {
        products.addEventListener("click", async function (event) {
            event.preventDefault();

            window.location.href = products_page;
        })
    }
});