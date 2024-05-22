document.addEventListener('DOMContentLoaded', function() {
  const updateHeaderText = document.getElementById('update_header');
  updateHeaderText.addEventListener('click', function() {
    document.querySelector('header').textContent = 'New Header!!!';
  });
});
