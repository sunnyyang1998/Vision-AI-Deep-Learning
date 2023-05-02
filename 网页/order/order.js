const backButton = document.getElementById("back-button");
const tableNumberSpan = document.getElementById("order-table-number");
const params = new URLSearchParams(window.location.search);
const tableNumber = params.get("table");
const orderNumberSpan = document.getElementById("order-id");
const orderContentSpan = document.getElementById("order-content");
const orderTotalSpan = document.getElementById("order-total");
const submitOrderButton = document.getElementById("submit-order-button");
const orderNotesTextarea = document.getElementById("order-notes");
const signatureCuisineButton = document.querySelector('[data-category="Signature Chengdu Cuisine"]');
const dryDishesButton = document.querySelector('[data-category="Dry Dishes"]');
const snackButton = document.querySelector('[data-category="Snack"]');
const beveragesButton = document.querySelector('[data-category="Beverages"]');
const signatureCuisineContainer = document.querySelector('.signature-cuisine-container');
const dryDishesContainer = document.querySelector('.dry-dishes-container');
const snackContainer = document.querySelector('.snack-container');
const beveragesContainer = document.querySelector('.beverages-container');

let orderContent = [];

// Call the generateOrderNumber function to get a unique order number
const orderNumber = generateOrderNumber();

tableNumberSpan.textContent = "Table " + tableNumber;

// Set the order number as the text content of the "order-id" element
orderNumberSpan.textContent = orderNumber;

backButton.addEventListener("click", () => {
  window.location.href = "../table/table.html";
});

signatureCuisineButton.addEventListener("click", () => {
  displayMenuItems("Signature Chengdu Cuisine");
});

dryDishesButton.addEventListener("click", () => {
  displayMenuItems("Dry Dishes");
});

snackButton.addEventListener("click", () => {
  displayMenuItems("Snack");
});

beveragesButton.addEventListener("click", () => {
  displayMenuItems("Beverages");
});

submitOrderButton.addEventListener("click", () => {
  const order = {
    tableNumber: tableNumber,
    orderNumber: orderNumber,
    orderContent: orderContent,
    orderNotes: orderNotesTextarea.value,
    orderTotal: calculateTotalPrice(orderContent)
  };

  const existingOrders = localStorage.getItem("orders");
  const orders = existingOrders ? JSON.parse(existingOrders) : [];

  orders.push(order);

  localStorage.setItem("orders", JSON.stringify(orders));

  window.location.href = `../confirmation/confirmation.html?table=${tableNumber}&order=${orderNumber}`;
});

function generateOrderNumber() {
  const timestamp = Date.now(); // 获取当前时间戳
  const randomNum = Math.floor(Math.random() * 1000000); // 生成随机数
  const orderNumber = `ORD-${timestamp}-${randomNum}`; // 拼接订单号
  return orderNumber;
}
function displayMenuItems(category) {
  signatureCuisineContainer.innerHTML = '';
  dryDishesContainer.innerHTML = '';
  snackContainer.innerHTML = '';
  beveragesContainer.innerHTML = '';

  const menuItems = data.menuItems;

  menuItems.forEach(item => {
    const itemName = item.name;
    const itemPrice = item.price;
    const itemDescription = item.description;
    const itemImg = item.img;

    if (item.category === category) {
      const menuItem = document.createElement('div');
      menuItem.classList.add('menu-item');
      menuItem.innerHTML = `
        <div class="menu-item-img">
          <img src="${itemImg}" alt="${itemName}">
        </div>
        <div class="menu-item-details">
          <h3 class="menu-item-name">${itemName}</h3>
          <p class="menu-item-description">${itemDescription}</p>
          <p class="menu-item-price">${itemPrice}</p>
          <button class="add-to-order-button">Add to order</button>
        </div>
      `;
    

      const addToOrderButton = menuItem.querySelector('.add-to-order-button');
      addToOrderButton.addEventListener('click', () => {
        const orderItem = {
          name: itemName,
          price: itemPrice
        };
        orderContent.push(orderItem);
        displayOrderContent();
      });

      switch (category) {
        case 'Signature Chengdu Cuisine':
          signatureCuisineContainer.appendChild(menuItem);
          break;
        case 'Dry Dishes':
          dryDishesContainer.appendChild(menuItem);
          break;
        case 'Snack':
          snackContainer.appendChild(menuItem);
          break;
        case 'Beverages':
          beveragesContainer.appendChild(menuItem);
          break;
        default:
          break;
      }
    }
  });
}

function calculateTotalPrice(orderContent) {
  let totalPrice = 0;
  orderContent.forEach(item => {
    totalPrice += parseFloat(item.price);
  });
  return totalPrice.toFixed(2);
}

function displayOrderContent() {
  let orderContentHTML = '';
  orderContent.forEach(item => {
    orderContentHTML += `
      <div class="order-item">
        <div class="order-item-name">${item.name}</div>
        <div class="order-item-price">${item.price}</div>
      </div>
    `;
  });

  orderContentSpan.innerHTML = orderContentHTML;
  orderTotalSpan.textContent = calculateTotalPrice(orderContent);
}

displayMenuItems('Signature Chengdu Cuisine');

