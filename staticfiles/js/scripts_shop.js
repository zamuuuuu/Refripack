// variables
let cart = [];
const cartCount = document.getElementById('cart-count');

// Actualizar el contador de elementos en el carrito
function updateCartCount() {
    cartCount.textContent = cart.length;
}

// Añadir producto al carrito
function addToCart(name, price) {
    const item = {
        name: name,
        price: price
    };
    cart.push(item);
    updateCartCount();
    alert(`${name} ha sido añadido al carrito!`);
}

// Asignar evento a los botones "Add to cart"
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function() {
        const name = this.dataset.name;
        const price = parseFloat(this.dataset.price);
        addToCart(name, price);
    });
});

// Mostrar el carrito al hacer clic en el botón del carrito
document.getElementById('cart-button').addEventListener('click', function() {
    if (cart.length === 0) {
        alert('El carrito está vacío.');
    } else {
        let cartItems = 'Artículos en el carrito:\n';
        cart.forEach(item => {
            cartItems += `${item.name} - $${item.price}\n`;
        });
        alert(cartItems);
    }
});
