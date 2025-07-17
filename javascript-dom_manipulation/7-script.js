document.addEventListener('DOMContentLoaded', function() {
  // Select the ul element where we'll list the movies
  const listMovies = document.getElementById('list_movies');
  
  // Star Wars API URL for films
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
  // Using Fetch API to get the list of movies
  fetch(apiUrl)
    .then(response => {
      // Check if the response is OK (status 200)
      if (!response.ok) {
        throw new Error('Error fetching movie data');
      }
      // Convert response to JSON
      return response.json();
    })
    .then(data => {
      // Get the array of movies from the response
      const movies = data.results;
      
      // For each movie, create a list item and add it to the ul
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => {
      // Error handling
      console.error('Error:', error);
      const errorItem = document.createElement('li');
      errorItem.textContent = 'Failed to load movies';
      listMovies.appendChild(errorItem);
    });
});