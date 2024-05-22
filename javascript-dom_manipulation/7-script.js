const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

fetch(url).then((response) => {
  if (!response.ok) {
    throw new Error(response.statusText)
  }
  return response.json();
})
  .then((data) => {
    const listElement = document.getElementById('list_movies');
    for (const film of data.results) {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listElement.appendChild(listItem);
    }
  });
