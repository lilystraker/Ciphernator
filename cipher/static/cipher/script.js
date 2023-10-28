
// document.querySelector('.triangle-button').addEventListener('click', function() {
// document.getElementById('cipherType').focus() 
// });

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");

    form.addEventListener("submit", function(event) {
        console.log("DOM is loaded.");  // Check if this message appears
        // Prevent the default form submission behavior (if needed)
        event.preventDefault();

        // Form has been submitted; you can perform actions here
        $('#results-container').show();

        // Access form data if needed
        // var formData = new FormData(form);
        // for (var pair of formData.entries()) {
        //     console.log(pair[0] + ': ' + pair[1]);
        // }
    });
});

$(document).ready(function () {
    // Hide both form placeholders initially
    document.getElementById('encryption-form-placeholder').style.display = 'block'; // Show
    document.getElementById('decryption-form-placeholder').style.display = 'none'; // Hide
    
    $('#results-container').hide();
    
    $('#cipherType').change(function () {
        var selectedOption = $(this).val();
        
        if (selectedOption === 'encryption') {
            document.getElementById('encryption-form-placeholder').style.display = 'block'; // Show
            document.getElementById('decryption-form-placeholder').style.display = 'none'; // Hide
            
        } else if (selectedOption === 'decryption') {
            document.getElementById('encryption-form-placeholder').style.display = 'none'; // Show
            document.getElementById('decryption-form-placeholder').style.display = 'block'; // Hide
            
        }
    });

});
