document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#copy-button').addEventListener('click', Copy);
  
});

function Copy() {
  /*
  Copy the password to clipboard.

  https://www.w3schools.com/howto/howto_js_copy_clipboard.asp
  */

  // Get the text field
  var copyText = document.getElementById("text");
 
  // Select the text field
  copyText.select();
  copyText.setSelectionRange(0, 99999); // For mobile devices

  // Copy the text inside the text field
  document.execCommand("copy");
 
  // Alert the copied text
  alert("Copied: " + copyText.value); 
}
