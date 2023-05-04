function bindTableButtons() {
  const tableButtons = document.querySelectorAll('.table-button');

  tableButtons.forEach((button) => {
    button.addEventListener('click', (event) => {
      const tableNumber = event.target.dataset.table;
      window.location.href = `../menu/menu.html?table=${tableNumber}`;
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  bindTableButtons();
});