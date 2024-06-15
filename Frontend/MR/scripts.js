document.getElementById('leave-request-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const studentName = document.getElementById('student-name').value;
    const roomNumber = document.getElementById('room-number').value;
    const sharing = document.getElementById('sharing').value;
    const reason = document.getElementById('reason').value;
    const location = document.getElementById('location').value;
    const fromDate = document.getElementById('from-date').value;
    const toDate = document.getElementById('to-date').value;
    const emergencyContactName = document.getElementById('emergency-contact-name').value;
    const emergencyContactNumber = document.getElementById('emergency-contact-number').value;

    alert(`Leave request submitted successfully:
    Student Name: ${studentName}
    Room Number: ${roomNumber}
    Sharing: ${sharing}
    Reason: ${reason}
    Location: ${location}
    From: ${fromDate}
    To: ${toDate}
    Emergency Contact Name: ${emergencyContactName}
    Emergency Contact Number: ${emergencyContactNumber}`);
});


function toggleMenu() {
    var menu = document.getElementById("mobileMenu");
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}
