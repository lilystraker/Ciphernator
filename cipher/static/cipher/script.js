
// document.querySelector('.triangle-button').addEventListener('click', function() {
// document.getElementById('cipherType').focus() 
// });
let form_id = document.getElementById('form_id')

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var submitBtn = document.getElementById('submitBtn');
    document.getElementById('results-container').style.display = 'block'; // or 'flex'
    encryptionForm = document.getElementById("encryption-form-placeholder")
    decryptionForm = document.getElementById("decryption-form-placeholder")

    if (window.location.href.includes('encryption')) {
        encryptionForm.style.display = "block";
        decryptionForm.style.display = "none";
    } else {
        decryptionForm.style.display = "block";
        encryptionForm.style.display = "none";
    }
    // var plaintext = document.getElementById('plaintext').value;
    // console.log('Plaintext:', plaintext);

    // when submit button clicked
    form.addEventListener('submit', function() {
        // prevent reload
        // event.preventDefault()
        document.getElementById('results-container').style.display = 'block'; // or 'flex'
      });
});


function showForm(selectedOption) {

    encryptionForm = document.getElementById("encryption-form-placeholder")
    encryptionForm.style.display = selectedOption === "encryption" ? "block" : "none";
    decryptionForm = document.getElementById("decryption-form-placeholder")
    decryptionForm.style.display = selectedOption === "decryption" ? "block" : "none";
    
    isEncryption = (encryptionForm === "block") ? true : false;
    isDecryption = (decryptionForm === "block") ? true : false;

    console.log(selectedOption)
}

document.getElementById('encryption-form-placeholder').addEventListener('submit', function(event) {
    // event.preventDefault();

    var plaintext = document.getElementById('id_plaintext').value;
    var key = document.getElementById('id_key').value;
    this.action += '?form=encryption';

    // Submit the form using AJAX
    $.ajax({
        type: 'POST',
        url:  $(this).attr('action'), 
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

document.getElementById('decryption-form-placeholder').addEventListener('submit', function(event) {
    // event.preventDefault();

    var ciphertext = document.getElementById('id_ciphertext').value;
    var key = document.getElementById('id_key').value;
    this.action += '?form=decryption';

    // Submit the form using AJAX
    $.ajax({
        type: 'POST',
        url:  $(this).attr('action') + '?form=decryption', // Replace with your actual decryption URL
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

$.ajax({
    type: 'POST',
    url: $(this).attr('action'),
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

// $.ajax({
//     type: 'POST',
//     url:  window.location.href,
//     data: $('#decryption-form-placeholder').serialize(),
//     success: function(response) {
//         // Update the DOM with the new values
//         $('#id_plaintext').text(response.plaintext);
//         $('#id_k1').text(response.k1);
//         $('#id_k2').text(response.k2);
//         $('#id_ciphertext').text(response.ciphertext);
//         $('#id_key').text(response.key);
//         $('#encryption-form-placeholder').hide();
//         $('#decryption-form-placeholder').show();

//     }
// });