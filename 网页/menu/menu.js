let orderList = [];

document.addEventListener('DOMContentLoaded', () => {
  fetch('products.csv')
    .then(response => response.text())
    .then(csv => {
      const lines = csv.split('\n').slice(1);
      const categories = {};

      lines.forEach(line => {
        const [id, productId, name, price, category] = line.split(',');

        if (!categories[category]) {
          categories[category] = [];
        }

        categories[category].push({ id, productId, name, price });
      });

      for (const categoryName in categories) {
        const categoryClass = categoryName.replace(/\s+/g, '');
        const categoryElement = document.querySelector(`.menu.${categoryClass}`);
        categories[categoryName].forEach(item => {
          const menuItem = document.createElement('div');
          menuItem.classList.add('menu-item');
          menuItem.innerHTML = `
            <p>${item.name}<p> 
            <p>${categoryName}</p>
            <p>Price：${item.price}</p>
            <button class="add-to-order">+</button>
          `;
          menuItem.querySelector('.add-to-order').addEventListener('click', () => addToOrder(item));
          categoryElement.appendChild(menuItem);
        });
      }
      displayCategory('All');
    });

  const navLinks = document.querySelectorAll('nav ul li a');
  navLinks.forEach(link =>
    link.addEventListener('click', event => {
      event.preventDefault();
      displayCategory(link.dataset.category);
    })
  );

  function displayCategory(category) {
    const categoryElements = document.querySelectorAll('.menu-container .menu');

    categoryElements.forEach(element => {
      if (category === 'All') {
        element.closest('.category').style.display = 'block';
      } else {
        element.closest('.category').style.display = element.classList.contains(category) ? 'block' : 'none';
      }
    });
  }
});

function addToOrder(item) {
  orderList.push(item);
  console.log('订单列表:', orderList);
}
