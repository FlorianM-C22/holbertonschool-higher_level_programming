document.addEventListener('DOMContentLoaded', function() {
  const addItemButton = document.getElementById('add_item');
  const myList = document.querySelector('.my_list');

  addItemButton.addEventListener('click', function() {
    const newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    myList.appendChild(newListItem);
  });
});
