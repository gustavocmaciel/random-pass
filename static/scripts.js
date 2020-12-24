document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#copy-button').addEventListener('click', Copy);
  
});
  
function Copy() {

  /* Get the text field */
  var copyText = document.getElementById("text");
 
  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");
 
  /* Alert the copied text */
  alert("Password Copied: " + copyText.value); 
}
