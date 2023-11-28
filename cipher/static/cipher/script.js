
// document.querySelector('.triangle-button').addEventListener('click', function() {
// document.getElementById('cipherType').focus() 
// });

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var submitBtn = document.getElementById('submitBtn');
    // var plaintext = document.getElementById('plaintext').value;
    // console.log('Plaintext:', plaintext);

    // when submit button clicked
    form.addEventListener('submit', function() {
        // prevent reload
        // event.preventDefault()
        document.getElementById('results-container').style.display = 'block'; // or 'flex'
      });
});

$(document).ready(function () {
    // Hide both form placeholders initially
    document.getElementById('encryption-form-placeholder').style.display = 'block'; // Show
    document.getElementById('decryption-form-placeholder').style.display = 'none'; // Hide
    
//     // document.getElementById('results-container').style.display = 'none'; // Show

    
//     $('#cipherType').change(function () {
//         // event.preventDefault();

//         var selectedOption = $(this).val();
        
//         if (selectedOption === 'encryption') {
//             document.getElementById('encryption-form-placeholder').style.display = 'block'; // Show
//             document.getElementById('decryption-form-placeholder').style.display = 'none'; // Hide
            
//         } else if (selectedOption === 'decryption') {
//             document.getElementById('encryption-form-placeholder').style.display = 'none'; // Show
//             document.getElementById('decryption-form-placeholder').style.display = 'block'; // Hide
            
//         }
//     });



});


// function showForm() {
//     event.preventDefault()
//     var selectedOption = document.getElementById("cipherType").value;
//     document.getElementById("encryption-form-placeholder").style.display = selectedOption === "encryption" ? "block" : "none";
//     document.getElementById("decryption-form-placeholder").style.display = selectedOption === "decryption" ? "block" : "none";
// }

function showForm(selectedOption) {

    encryptionForm = document.getElementById("encryption-form-placeholder")
    encryptionForm.style.display = selectedOption === "encryption" ? "block" : "none";
    decryptionForm = document.getElementById("decryption-form-placeholder")
    decryptionForm.style.display = selectedOption === "decryption" ? "block" : "none";
    
    isEncryption = (encryptionForm === "block") ? true : false;
    isDecryption = (decryptionForm === "block") ? true : false;

    console.log(selectedOption)
}

document.getElementById('decryption-form-placeholder').addEventListener('submit', function(event) {
    event.preventDefault();

    var ciphertext = document.getElementById('id_ciphertext').value;
    var key = document.getElementById('id_key').value;

    // Submit the form using AJAX
    $.ajax({
        type: 'POST',
        url: window.location.href,  // Replace with your actual decryption URL
        data: {
            'ciphertext': ciphertext,
            'key': key,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            // This function runs when the server sends a response
            // You can use the 'response' variable to access the data sent by the server

            // For example, if the server sends back some HTML to display in the 'resultsContainer':
            $('#resultsContainer').html(response);
        }
    });
});

document.getElementById('encryption-form-placeholder').addEventListener('submit', function(event) {
    // event.preventDefault();

    var plaintext = document.getElementById('id_plaintext').value;
    var key = document.getElementById('id_key').value;

    // Submit the form using AJAX
    $.ajax({
        type: 'POST',
        url: window.location.href,  // Replace with your actual decryption URL
        data: {
            'plaintext': plaintext,
            'key': key,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            // This function runs when the server sends a response
            // You can use the 'response' variable to access the data sent by the server

            // For example, if the server sends back some HTML to display in the 'resultsContainer':
            $('#resultsContainer').html(response);
        }
    });
});

// This is just an example. You'll need to adjust this code to match your actual AJAX call.
$.ajax({
    type: 'POST',
    url:  window.location.href,
    data: $('#encryption-form-placeholder').serialize(),
    success: function(response) {
        // Update the DOM with the new values
        $('#id_plaintext').text(response.plaintext);
        $('#id_k1').text(response.k1);
        $('#id_k2').text(response.k2);
        $('#id_ciphertext').text(response.ciphertext);
        $('#id_key').text(response.key);
    }
});