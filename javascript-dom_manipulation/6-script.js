document.addEventListener('DOMContentLoaded', function() {
  // Select the element to display the character's name
  const characterElement = document.getElementById('character');
  
  // Star Wars API URL for character with ID 5
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  
  // Using Fetch API to get the data
  fetch(apiUrl)
    .then(response => {
      // Check if the response is OK (status 200)
      if (!response.ok) {
        throw new Error('Error fetching character data');
      }
      // Convert response to JSON
      return response.json();
    })
    .then(data => {
      // Update the element's content with the character's name
      characterElement.textContent = data.name;
    })
    .catch(error => {
      // Error handling
      console.error('Error:', error);
      characterElement.textContent = 'Failed to load character';
    });
});