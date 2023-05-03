const orderList = {}; // 用来存储订单数据的数组
const backButton = document.getElementById("back-to-table");
const submitOrderButton = document.getElementById("submit-order");
const orderListParam = encodeURIComponent(JSON.stringify(orderList));
// Initialize Firebase
firebase.initializeApp(firebaseConfig);


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
        categories[categoryName].forEach((item) => {
            const menuItem = document.createElement("div");
            menuItem.classList.add("menu-item");
            menuItem.innerHTML = `
              <p>${item.name}<p>
              <p>${categoryName}</p>
              <p>价格：${item.price}</p>
            `;
            // Add the "Add to Order" button to the menu item
            menuItem.appendChild(createAddToOrderButton(item));
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

function createAddToOrderButton(item) {
  const button = document.createElement("button");
  button.textContent = " + ";
  button.classList.add("add-button"); // 添加类名
  button.addEventListener("click", () => {
    addToOrder(item);
  });
  return button;
}

function removeFromOrder(itemId) {
  if (orderList[itemId]) {
    orderList[itemId].quantity -= 1;
    if (orderList[itemId].quantity === 0) {
      delete orderList[itemId];
    }
  }
  updateOrderList();
}
  
backButton.addEventListener("click", () => {
  window.location.href = "../table/table.html";
});

  // 监听窗口滚动事件，根据滚动距离来调整卡片的位置
  window.addEventListener('scroll', () => {
    const orderListEl = document.getElementById('order-list');
    const topOffset = 50;
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    orderListEl.style.top = `${topOffset + scrollTop}px`;
  });
  

  function addToOrder(item) {
    if (orderList[item.id]) {
      orderList[item.id].quantity += 1;
    } else {
      orderList[item.id] = { ...item, quantity: 1 };
    }
    updateOrderList();
  }

  function updateOrderList() {
    const orderListEl = document.getElementById("order-list-content");
    
    // 创建一个新的 div 元素来存放订单列表项
    const orderItemsEl = document.createElement("div");
    orderItemsEl.classList.add("order-items");
  
    let totalPrice = 0; // 定义一个变量来存储总价格
  
    if (Object.keys(orderList).length === 0) {
      totalPrice = 0;
    } else {
      for (const itemId in orderList) {
        const item = orderList[itemId];
        const orderItemEl = document.createElement("div");
        orderItemEl.classList.add("order-item");
    
        const totalItemPrice = parseFloat(item.price) * item.quantity;
    
        orderItemEl.textContent = `${item.name} x ${item.quantity} $${totalItemPrice.toFixed(2)}`;
    
        totalPrice += totalItemPrice;
    
        const removeButton = document.createElement("button");
        removeButton.textContent = " - ";
        removeButton.classList.add("remove-button");
        removeButton.addEventListener("click", () => {
          removeFromOrder(itemId);
        });
        orderItemEl.appendChild(removeButton);
    
        orderItemsEl.appendChild(orderItemEl); // 将订单项添加到新的 div 元素中，而不是直接添加到 orderListEl
      }
    }
  
    const totalPriceEl = document.getElementById("total-price");
    totalPriceEl.textContent = `总价：$${totalPrice.toFixed(2)}`;
  
    // 保留标题和提交按钮，并替换旧的订单列表项
    const oldOrderItemsEl = orderListEl.querySelector(".order-items");
    if (oldOrderItemsEl) {
      orderListEl.replaceChild(orderItemsEl, oldOrderItemsEl);
    } else {
      const submitButton = orderListEl.querySelector(".submit-order-button");
      orderListEl.insertBefore(orderItemsEl, submitButton);
    }
  }

function getQueryParam(param) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
}

submitOrderButton.addEventListener("click", () => {
  const tableNumber = getQueryParam("table");
  // 在这里处理订单提交逻辑，例如发送数据到服务器
  // ...
  // 然后将用户重定向到order.html页面
  window.location.href = `../order/order.html?table=${tableNumber}`;
});

submitOrderButton.addEventListener("click", () => {
  const tableNumber = getQueryParam("table");
  const orderListArray = Object.values(orderList); // Convert the order list object to an array
  const orderListString = JSON.stringify(orderListArray); // Convert the order list array to a string
  localStorage.setItem('orderList', orderListString); // Store the order list in localStorage
  window.location.href = `../order/order.html?table=${tableNumber}`;
});



