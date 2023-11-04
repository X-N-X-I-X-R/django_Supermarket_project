# django_Supermarket_project


echo "# django_Supermarket_project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/01001110IR/django_Supermarket_project.git
git push -u origin main



https://github.com/01001110IR/django_Supermarket_project.git# django_Supermarket_for_etid










      function buyItem(itemId) {
            const product = res.data.find(prod => prod.id === itemId);
            if (product) {
                const existingCartItem = purchasedItems.find(item => item.id === product.id);
                if (existingCartItem) {
                    existingCartItem.quantity += 1;
                } else {
                    product.quantity = 1;
                    purchasedItems.push(product);
                }
                localStorage.setItem("purchasedItems", JSON.stringify(purchasedItems));
                displayCart();
                displayCartInConsole();
                updateTotalPrice();
        }
        function removeItem(itemId) {
            localStorage.getItem("purchasedItems", JSON.stringify(purchasedItems));
            const index = purchasedItems.find(item => item.id === itemId);
        
            if (index !== -1) {
                // If the product exists, reduce the quantity by 1
                purchasedItems[index].quantity -= 1;
        
                // If the quantity is zero, remove the product from the array
                if (purchasedItems[index].quantity === 0) {
                    purchasedItems.splice(index, 1);
                }
        
                // Update the local storage
                localStorage.setItem("purchasedItems", JSON.stringify(purchasedItems));
        
                // Display the updated cart
                displayCart();
                displayCartInConsole();
                updateTotalPrice();
            }
        }
        
        
        function displayCart() {
            const cart = document.getElementById("cart");
            cart.innerHTML = "<h2>My Cart</h2>";
            purchasedItems.forEach(item => {
                cart.innerHTML += `<p>${item.name} - ${item.quantity}</p>`;
            });
        }

        function displayCartInConsole() {
            console.log("My Cart:");
            console.table(purchasedItems);
            
        }

        displayCart();

        function displayLocalStorageData() {
            const displayTableBody = document.querySelector("#display table tbody");
        
            // Clear existing table rows
            displayTableBody.innerHTML = "";
        
            const purchasedItems = JSON.parse(localStorage.getItem("purchasedItems"));
        
            if (purchasedItems && purchasedItems.length > 0) {
                purchasedItems.forEach(item => {
                    // Calculate the total price for the item
                    const product_price_total = item.quantity * item.price;
        
                    // Create a new row for the item in the table
                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                        <td>${item.name}</td>
                        <td>${item.quantity}</td>
                        <td>${item.price}</td>
                        <td>${ product_price_total}</td>
                    
                    `;
        
                    displayTableBody.appendChild(newRow);
                });
            } else {
                // If there are no items, display a message in the table
                const newRow = document.createElement("tr");
                newRow.innerHTML = `
                    <td colspan="4">No items in the cart.</td>
                `;
        
                displayTableBody.appendChild(newRow);
            }
        }
        
        // Call the function when the page loads
        displayLocalStorageData();
        
        function updateTotalPrice() {
            let totalPrice = 0;
            purchasedItems.forEach(item => {
                totalPrice += item.quantity * item.price;
            });
            const totalAmountElement = document.getElementById("total-amount");
            totalAmountElement.textContent = totalPrice;
        }
        
    }