
import { ref, set, onValue } from "firebase/database";

// Store order data in Firebase
function storeOrderData(order) {
  const orderRef = ref(database, "orders/" + order.orderId);
  set(orderRef, order);
}

// Retrieve order data from Firebase
function getOrderData(callback) {
  const ordersRef = ref(database, "orders");
  onValue(ordersRef, (snapshot) => {
    const orders = snapshot.val();
    callback(orders);
  });
}

document.addEventListener("DOMContentLoaded", () => {
    // Retrieve the submitted orders from storage (e.g., localStorage or server)
    // Replace getSubmittedOrders() with the function or method you use to get the submitted orders
    const orders = getSubmittedOrders();
  
    const orderList = document.querySelector(".order-list");
  
    orders.forEach((order) => {
      const orderCard = document.createElement("div");
      orderCard.classList.add("order-card");
  
      const orderCardHeading = document.createElement("h2");
      orderCardHeading.classList.add("order-card-heading");
      orderCardHeading.textContent = `订单 #${order.orderId}`;
      orderCard.appendChild(orderCardHeading);
  
      const orderTableNumber = document.createElement("div");
      orderTableNumber.classList.add("order-card-details");
      orderTableNumber.innerHTML = `<span>桌号：</span><span>${order.tableNumber}</span>`;
      orderCard.appendChild(orderTableNumber);
  
      const orderStatus = document.createElement("div");
      orderStatus.classList.add("order-card-details");
      orderStatus.innerHTML = `<span>状态：</span><span>${order.status}</span>`;
      orderCard.appendChild(orderStatus);
  
      const orderItemsContainer = document.createElement("div");
      orderItemsContainer.classList.add("order-items");
      order.orderItems.forEach((item) => {
        const orderItem = document.createElement("p");
        orderItem.textContent = `${item.name} x ${item.quantity}`;
        orderItemsContainer.appendChild(orderItem);
      });
      orderCard.appendChild(orderItemsContainer);
  
      orderList.appendChild(orderCard);
    });
  });
  