const tableButtons = document.querySelectorAll('.table-button');

tableButtons.forEach((button) => {
  button.addEventListener('click', (event) => {
    const tableNumber = event.target.dataset.table;
    window.location.href = `../order/order.html?table=${tableNumber}`;
  });
});
