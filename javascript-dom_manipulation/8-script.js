document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText);
      }
      return response.json();
    })
    .then((data) => {
      document.getElementById('hello').textContent = data.hello;
    });
});
