const backButton = document.getElementById("back-button");
const tableNumberSpan = document.getElementById("order-table-number");
const params = new URLSearchParams(window.location.search);
const tableNumber = params.get("table");
const orderNumberSpan = document.getElementById("order-id");
const orderContentSpan = document.getElementById("order-content");
const orderTotalSpan = document.getElementById("order-total");
const orderNotesTextarea = document.getElementById("order-notes");

document.addEventListener('DOMContentLoaded', () => {
  const tableNumber = getQueryParam("table");
  document.getElementById("order-table-number").textContent = tableNumber;

  const orderListString = localStorage.getItem('orderList'); // Retrieve the order list from localStorage
  const orderListArray = JSON.parse(orderListString); // Convert the order list string back to an array

  // Display the order items and total price
  let totalPrice = 0;
  const orderItemsContainer = document.getElementById("order-items");

  for (const item of orderListArray) {
    const totalItemPrice = parseFloat(item.price) * item.quantity;
    totalPrice += totalItemPrice;

    const orderItemEl = document.createElement("p");
    orderItemEl.textContent = `${item.name} x ${item.quantity} $${totalItemPrice.toFixed(2)}`;
    orderItemsContainer.appendChild(orderItemEl);
  }

  document.getElementById("order-total").textContent = `$${totalPrice.toFixed(2)}`;

  // Add a function to get the query param
  function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
  }
});

// Call the generateOrderNumber function to get a unique order number
const orderNumber = generateOrderNumber();

tableNumberSpan.textContent = "Table " + tableNumber;

// Set the order number as the text content of the "order-id" element
orderNumberSpan.textContent = orderNumber;

backButton.addEventListener("click", () => {
  window.location.href = "../table/table.html";
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







