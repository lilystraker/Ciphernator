
// document.querySelector('.triangle-button').addEventListener('click', function() {
// document.getElementById('cipherType').focus() 
// });

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var submitBtn = document.getElementById('submitBtn');

    // when submit button clicked
    form.addEventListener('submit', function() {
        // prevent reload
        event.preventDefault()
        document.getElementById('results-container').style.display = 'block'; // or 'flex'
      });
});

$(document).ready(function () {
    // Hide both form placeholders initially
    document.getElementById('encryption-form-placeholder').style.display = 'block'; // Show
    document.getElementById('decryption-form-placeholder').style.display = 'none'; // Hide
    
    // document.getElementById('results-container').style.display = 'none'; // Show

    
    $('#cipherType').change(function () {
        // event.preventDefault();

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
