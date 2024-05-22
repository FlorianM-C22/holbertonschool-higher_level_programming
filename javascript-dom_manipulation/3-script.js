const headerElement = document.querySelector('header');
const toggleElement = document.getElementById('toggle_header');

toggleElement.addEventListener('click', function() {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else if (headerElement.classList.contains('green')) {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  } else {
    headerElement.classList.add('red');
  }
});
