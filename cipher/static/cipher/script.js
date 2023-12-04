
let form_id = document.getElementById('form_id')

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var submitBtn = document.getElementById('submitBtn');
    document.getElementById('results-container').style.display = 'block'; 
    encryptionForm = document.getElementById("encryption-form-placeholder")
    decryptionForm = document.getElementById("decryption-form-placeholder")

    if (window.location.href.includes('encryption')) {
        encryptionForm.style.display = "block";
        decryptionForm.style.display = "none";
    } else {
        decryptionForm.style.display = "block";
        encryptionForm.style.display = "none";
    }

    $(".encrypt-button").click(function(){
        $(this).toggleClass("custom-active");
        $(".decrypt-button").removeClass("custom-active")

    });

    $(".decrypt-button").click(function(){
        $(this).toggleClass("custom-active");
        $(".encrypt-button").removeClass("custom-active")
    });

    var errorMessages = document.querySelectorAll('.error-message');

    errorMessages.forEach(function(errorMessages) {
        errorMessages.style.display = 'none';
    });


    // when submit button clicked
    form.addEventListener('submit', function() {
        document.getElementById('results-container').style.display = 'block';
      });
});


function showForm(selectedOption) {

    // Following code is used to get my CSS variables
    // Get the root element
    var root = document.documentElement;

     // Get the computed style of the root element
    var css = getComputedStyle(root);

    // Get the value of the CSS colour variables
    var encryptColor = css.getPropertyValue('--encrypt');
    var decryptColor = css.getPropertyValue('--decrypt');

    encryptionForm = document.getElementById("encryption-form-placeholder")
    encryptionForm.style.display = selectedOption === "encryption" ? "block" : "none";
    decryptionForm = document.getElementById("decryption-form-placeholder")
    decryptionForm.style.display = selectedOption === "decryption" ? "block" : "none";
    
    isEncryption = (encryptionForm === "block") ? true : false;
    isDecryption = (decryptionForm === "block") ? true : false;

    var encryptionButton = document.getElementsByClassName("encrypt-button")

    if (isEncryption) {
        encryptionButton.style.backgroundColor = encryptColor;
    }
    else if (isDecryption) {
        decryptionButton.style.backgroundColor = decryptColor;
    }
}

function isInputValid(input, bits) {
    var regex = new RegExp(`^[01]{${bits}}$`);
    return regex.test(input);
}

function validate(type) {
    
    // Check the inputs are valid

    if (type == 'encryption') {
        var plaintext = document.getElementById('id_plaintext').value;
        var key = document.getElementById('id_key').value;
        if (!isInputValid(plaintext, 8)) {
            // Display error message
            document.getElementById("plaintext-error").style.display = "block";
        }
        if (!isInputValid(key, 10)) {
            // Display error message
            document.getElementById("key-error").style.display = "block";
        }
    }
    if (type == 'decryption') {
        var ciphertext = document.getElementById('id_ciphertext').value;
        var cipherkey = document.getElementById('id_cipherkey').value;
        if (!isInputValid(ciphertext, 8)) {
            // Display error message
            document.getElementById("ciphertext-error").style.display = "block";
        }

        if (!isInputValid(cipherkey, 10)) {
            // Display error message
            document.getElementById("keycipher-error").style.display = "block";
        }
    }

}
document.getElementById('encryption-form-placeholder').addEventListener('submit', function(event) {
    var isEncryptInvalid = false;
    var plaintext = document.getElementById('id_plaintext').value;
    var key = document.getElementById('id_key').value;
    this.action += '?form=encryption';

    // Check the inputs are valid
    if (!isInputValid(plaintext, 8)) {
        // Display error message
        document.getElementById("plaintext-error").style.display = "block";
        // prevent submit
        event.preventDefault();
        isEncryptInvalid = true;
    }
    else {
        document.getElementById("plaintext-error").style.display = "none";
    }
    if (!isInputValid(key, 10)) {
        // Display error message
        document.getElementById("key-error").style.display = "block";
        // prevent submit
        event.preventDefault();
        isEncryptInvalid = true;
    }
    else {
        document.getElementById("key-error").style.display = "none";
    }


    // Submit the form using AJAX
    if (!isEncryptInvalid) {
        $.ajax({
            type: 'POST',
            url:  $(this).attr('action'), 
            data: {
                'plaintext': plaintext,
                'key': key,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                // The server sends back some HTML to display in the 'resultsContainer':
                $('#resultsContainer').html(response);
            }
        });
    }

});

document.getElementById('decryption-form-placeholder').addEventListener('submit', function(event) {

    var ciphertext = document.getElementById('id_ciphertext').value;
    var cipherkey = document.getElementById('id_cipherkey').value;
    this.action += '?form=decryption';
    var isDecryptInvalid = false;
    
    // Check the inputs are valid
    if (!isInputValid(ciphertext, 8)) {
        // Display error message
        document.getElementById("ciphertext-error").style.display = "block";
        // prevent submit
        event.preventDefault();
        isDecryptInvalid = true;
    }
    else {
        document.getElementById("ciphertext-error").style.display = "none";
    }

    if (!isInputValid(cipherkey, 10)) {
        // Display error message
        document.getElementById("keycipher-error").style.display = "block";
        // prevent submit
        event.preventDefault();
        isDecryptInvalid = true;
    }
    else {
        document.getElementById("keycipher-error").style.display = "none";

    }

    // Submit the form using AJAX

    if (!isDecryptInvalid) {
        $.ajax({
            type: 'POST',
            url:  $(this).attr('action') + '?form=decryption', 
            data: {
                'ciphertext': ciphertext,
                'cipherkey': cipherkey,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                $('#resultsContainer').html(response);
    
            }
        });
    }

});

// When a form is submitted, the page will reload and the results will be displayed
if (!isEncryptInvalid && !isDecryptInvalid) {
    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $('#encryption-form-placeholder').serialize(),
        success: function(response) {
            // Update the DOM with the new results
            $('#id_plaintext').text(response.plaintext);
            $('#id_k1').text(response.k1);
            $('#id_k2').text(response.k2);
            $('#id_ciphertext').text(response.ciphertext);
            $('#id_key').text(response.key);
            $('#id_cipherkey').text(response.cipherkey);
        }
    });
}
