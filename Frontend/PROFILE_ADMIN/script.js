document.getElementById('search').addEventListener('keyup', function() {
    let filter = this.value.toUpperCase();
    let rows = document.querySelector("#studentTable").rows;
    
    for (let i = 0; i < rows.length; i++) {
        let firstCell = rows[i].cells[0];
        if (firstCell) {
            let textValue = firstCell.textContent || firstCell.innerText;
            if (textValue.toUpperCase().indexOf(filter) > -1) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
});


function toggleMenu() {
    var menu = document.getElementById("mobileMenu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}
