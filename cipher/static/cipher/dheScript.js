
// JavaScript for DHE
// Contains form validation, AJAX submission, and dynamic HTML rendering/CSS styling

let form_id = document.getElementById('form_id')
var isEncryptInvalid = false;
var isDecryptInvalid = false;
var prime_modulus = document.getElementById('id_prime_modulus').value;
var generator = document.getElementById('id_generator').value;
var xa = document.getElementById('id_xa').value;
var xb = document.getElementById('id_xb').value;

var form = document.getElementById("form");
var submitBtn = document.getElementById('submitBtn');
var resultsContainer = document.getElementById('results-container')

encryptionForm = document.getElementById("encryption-form-placeholder")
resultsTable = document.getElementById("results-table")


// Following code is used to get my CSS variables
// Get the root element
var root = document.documentElement;

// Get the computed style of the root element
var css = getComputedStyle(root);
// Get the value of the CSS colour variables
var encryptColor = css.getPropertyValue('--encrypt');
// var decryptColor = css.getPropertyValue('--decrypt');


document.addEventListener("DOMContentLoaded", function() {
    resultsContainer.style.display  = 'block'; 
    // if (window.location.href.includes('decryption')) {
    //     // show the dercyption form
    //     // decryptionForm.style.display = "block";
    //     encryptionForm.style.display = "none";
    //     resultsContainer.style.display  = 'block'; 
    //     // change the colour of the results table border
    //     resultsTable.style.borderColor = "#FDF5BF";
    //     // toggle decryption selection button
    //     // $(".decrypt-button").toggleClass("custom-active");
    //     $(".encrypt-button").removeClass("custom-active")
    // } else 
    if (window.location.href.includes('encryption')) {
        // show the encryption form by default
        encryptionForm.style.display = "block";
        // decryptionForm.style.display = "none";
        resultsContainer.style.display  = 'block'; 

        // change the colour of the results table border
        resultsTable.style.borderColor = "#bfb2ff";

        // toggle encryption selection button
        $(".encrypt-button").toggleClass("custom-active");
        // $(".decrypt-button").removeClass("custom-active");
    }
    // show encryption form by default
    else {
        encryptionForm.style.display = "block";
        // decryptionForm.style.display = "none";
        resultsContainer.style.display  = 'none';

        // toggle encryption selection button 
        $(".encrypt-button").toggleClass("custom-active");
        // $(".decrypt-button").removeClass("custom-active")
    }

    $(".encrypt-button").click(function(){
        $(this).toggleClass("custom-active");
        // $(".decrypt-button").removeClass("custom-active")

    });

    // $(".decrypt-button").click(function(){
    //     $(this).toggleClass("custom-active");
    //     $(".encrypt-button").removeClass("custom-active")
    // });


    var errorMessages = document.querySelectorAll('.error-message');

    errorMessages.forEach(function(errorMessages) {
        errorMessages.style.display = 'none';
    });


    // when submit button clicked
    form.addEventListener('submit', function() {
        // prevent submission before running validation
        document.getElementById('results-container').style.display = 'block';
      });
});


function showForm(selectedOption) {

    encryptionForm = document.getElementById("encryption-form-placeholder")
    encryptionForm.style.display = selectedOption === "encryption" ? "block" : "none";
    // decryptionForm = document.getElementById("decryption-form-placeholder")
    // decryptionForm.style.display = selectedOption === "decryption" ? "block" : "none";
    
    isEncryption = (encryptionForm === "block") ? true : false;
    // isDecryption = (decryptionForm === "block") ? true : false;

    var encryptionButton = document.getElementsByClassName("encrypt-button")

    if (isEncryption) {
        encryptionButton.style.backgroundColor = encryptColor;
    }
    // else if (isDecryption) {
    //     decryptionButton.style.backgroundColor = decryptColor;
    // }
}

// Check input is a valid integer between the min and max number of digits
function isInteger(input, min_digits, max_digits) {
    var regex = new RegExp(`^[0-9]{${min_digits},${max_digits}}$`);
    return regex.test(input);
}

function validate(type) {
    
    // Check the inputs are valid before submission

    if (type == 'encryption') {
        if (!isInt(prime_modulus, 1, 50)) {
            // Display error message
            document.getElementById("prime-modulus-error").style.display = "block";

        }
        if (!isInt(generator, 1, 10)) {
            // Display error message
            document.getElementById("generator-error").style.display = "block";
        }
        if (!isInt(xa, 1, 10)) {
            // Display error message
            document.getElementById("xa-error").style.display = "block";
        }
        if (!isInt(xb, 1, 10)) {
            // Display error message
            document.getElementById("xb-error").style.display = "block";
        }
    }
    // if (type == 'decryption') {
    //     var ciphertext = document.getElementById('id_ciphertext').value;
    //     var cipherkey = document.getElementById('id_cipherkey').value;
    //     if (!isBinary(ciphertext, 8)) {
    //         // Display error message
    //         document.getElementById("ciphertext-error").style.display = "block";
    //     }

    //     if (!isBinary(cipherkey, 10)) {
    //         // Display error message
    //         document.getElementById("keycipher-error").style.display = "block";
    //     }
}


    document.getElementById('encryption-form-placeholder').addEventListener('submit', function(event) {
        var isEncryptInvalid = false;
        var prime_modulus = document.getElementById('id_prime_modulus').value;
        var generator = document.getElementById('id_generator').value;
        var xa = document.getElementById('id_xa').value;
        var xb = document.getElementById('id_xb').value;
        var errorColour = css.getPropertyValue('--error');

    
        this.action += '?form=encryption';
    
        // Check the inputs are valid
        if (!isInteger(prime_modulus, 1, 50)) {
            // Display error message
            document.getElementById("prime-modulus-error").style.display = "block";
            document.getElementById("id_prime_modulus").style.borderColor = errorColour;

            // prevent submit
            event.preventDefault();
            isEncryptInvalid = true;
        }
        else {
            document.getElementById("prime-modulus-error").style.display = "none";
            document.getElementById("id_prime_modulus").style.borderColor = encryptColor;

        }
        if (!isInteger(generator, 1, 10)) {
            // Display error message
            document.getElementById("generator-error").style.display = "block";
            document.getElementById("id_generator").style.borderColor = errorColour;

            // prevent submit
            event.preventDefault();
            isEncryptInvalid = true;
        }
        else {
            document.getElementById("generator-error").style.display = "none";
            document.getElementById("id_generator").style.borderColor = encryptColor;

        }
    
        if (!isInteger(xa, 1, 10)) {
            // Display error message
            document.getElementById("xa-error").style.display = "block";
            document.getElementById("id_xa").style.borderColor = errorColour;

            // prevent submit
            event.preventDefault();
            isEncryptInvalid = true;
        }
        else {
            document.getElementById("xa-error").style.display = "none";
            document.getElementById("id_xa").style.borderColor = encryptColor;

        }
    
        if (!isInteger(xb, 1, 10)) {
            // Display error message
            document.getElementById("xb-error").style.display = "block";
            document.getElementById("id_xb").style.borderColor = errorColour;

            // prevent submit
            event.preventDefault();
            isEncryptInvalid = true;
        }
        else {
            document.getElementById("xb-error").style.display = "none";
            document.getElementById("id_xb").style.borderColor = encryptColor;

        }

    
        // Submit the form using AJAX
        if (!isEncryptInvalid) {
            $.ajax({
                type: 'POST',
                url:  $(this).attr('action'), 
                data: {
                    'prime_modulus': prime_modulus,
                    'generator': generator,
                    'xa': xa,
                    'xb': xb,
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(response) {
                    // The server sends back some HTML to display in the 'resultsContainer':
                    $('#resultsContainer').html(response);
                }
            });
        } else {
            // Hide the results 
            document.querySelector('#results-container').style.display = 'none';
        }
    
    });

// When a form is submitted, the page will reload and the results will be displayed
if (!isEncryptInvalid) {
    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $('#encryption-form-placeholder').serialize(),
        success: function(response) {
            // Update the DOM with the new results
            $('#id_prime_modulus').text(response.prime_modulus);
            $('#id_generator').text(response.generator);
            $('#id_xa').text(response.xa);
            $('#id_xb').text(response.xb);
            $('#id_ya').text(response.ya);
            $('#id_yb').text(response.yb);
            $('#id_k1').text(response.k1);
        }
    });
}



// =======================

