// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the element with id 'red_header'
  const redHeader = document.getElementById('red_header');
  
  // Add click event listener
  redHeader.addEventListener('click', function() {
    // Get the header element and change its color to red
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
  });
});
