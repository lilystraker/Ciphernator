
// document.querySelector('.triangle-button').addEventListener('click', function() {
// document.getElementById('cipherType').focus() 
// });

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var submitBtn = document.getElementById('submitBtn');

    // when submit button clicked
    submitBtn.addEventListener("click", function(event) {
        // Prevent the default form submission behavior (if needed)

        form.submit();
        // Form has been submitted; you can perform actions here
        document.getElementById('results-container').style.display = 'block'; // Show

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
    
    // document.getElementById('results-container').style.display = 'none'; // Show

    
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
