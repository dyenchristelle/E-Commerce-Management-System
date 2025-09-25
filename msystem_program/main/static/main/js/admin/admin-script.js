// for admin 
// try lang, pero wala pa db kaya di natapos
document.addEventListener("DOMContentLoaded", function() {
    const admin_login = document.getElementById("admin-login");

    const form = document.getElementById("admin-login");
    if (!form) {
        console.error("Form not found!");
        return;
    }
    console.log("Form loaded successfully!");

    if(admin_login) {
        admin_login.addEventListener("click", async function (event) {
        event.preventDefault();

        const admin_username = document.getElementById("admin-username")
        const admin_pass = document.getElementById("admin-pass")
        const errorMessage = document.getElementById("errorMessage");

        if (admin_username == "admin" && admin_pass == "admincpe6"){
            window.location.href = "admin/homepage.html";
        } if (!admin_username || !admin_pass) {
            errorMessage.style.display = "block";
            errorMessage.textContent = "Please fill out both fields.";
            return; 
        } else {
            errorMessage.style.display = "block";
            errorMessage.textContent = "Username and Password doesn't match.";
            return; 
        }
        });
    }
});