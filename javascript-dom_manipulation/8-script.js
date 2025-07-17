// This ensures the code runs after the DOM is fully loaded
function fetchHello() {
  // Select the element where we'll display the translation
  const helloElement = document.getElementById('hello');
  
  // API URL for fetching the French translation of "hello"
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
  // Using Fetch API to get the translation
  fetch(apiUrl)
    .then(response => {
      // Check if the response is OK (status 200)
      if (!response.ok) {
        throw new Error('Error fetching translation');
      }
      // Convert response to JSON
      return response.json();
    })
    .then(data => {
      // Display the translation in the hello element
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      // Error handling
      console.error('Error:', error);
      helloElement.textContent = 'Failed to load translation';
    });
}

// Run the function when the DOM is fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', fetchHello);
} else {
  // If the document is already loaded, run immediately
  fetchHello();
}
