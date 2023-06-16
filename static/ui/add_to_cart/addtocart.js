const product = [
  {
    id: 0,
    image: '/image/shirt.jpg',
    title: 'Shirt',
    price: 80,
  },
  {
    id: 1,
    image: 'image/kurta.jpg',
    title: 'Kurta',
    price: 60,
  },
  {
    id: 2,
    image: 'image/saree.jpg',
    title: 'Saree Normal',
    price: 150,
  },
  {
    id: 3,
    image: 'image/saree.jpg',
    title: 'Saree goldzari',
    price: 300,
  },
  {
    id: 4,
    image: 'image/Tshirt.jpg',
    title: 'Tshirt',
    price: 100,
  },
  {
    id: 5,
    image: 'image/jeans.jpg',
    title: 'Jeans',
    price: 100,
  },
  {
    id: 6,
    image: 'image/short.jpg',
    title: 'Short',
    price: 80,
  },
  {
    id: 7,
    image: 'image/shirt.jpg',
    title: 'Shirt Designer',
    price: 100,
  }

];
const categories = [...new Set(product.map((item) => item))];
let i = 0;

document.getElementById('root').innerHTML = categories
  .map((item) => {
    var { image, title, price } = item;
    const priceInINR = price * 1; // Assuming 1 USD = 74.5 INR
    return (
      `<div class='box'>
        <div class='img-box'>
          <img class='images' src=${image}></img>
        </div>
        <div class='bottom'>
          <p>${title}</p>
          <h2>Rs ${priceInINR}.00</h2>` +
      `<button onclick='addtocart(${i++})'>Add to cart</button>` +
      `</div>
      </div>`
    );
  })
  .join('');

var cart = [];

function addtocart(a) {
  cart.push({ ...categories[a] });
  displaycart();
}

function delElement(a) {
  cart.splice(a, 1);
  displaycart();
}

function displaycart() {
  let j = 0,
    total = 0;
  document.getElementById('count').innerHTML = cart.length;
  if (cart.length == 0) {
    document.getElementById('cartItem').innerHTML = 'Your cart is empty';
    document.getElementById('total').innerHTML = 'Rs ' + 0 + '.00';
  } else {
    document.getElementById('cartItem').innerHTML = cart
      .map((items) => {
        var { image, title, price } = items;
        const priceInINR = price * 1;
        total = total + priceInINR;
        document.getElementById('total').innerHTML = 'Rs ' + total + '.00';
        return (
          `<div class='cart-item'>
          <div class='row-img'>
            <img class='rowimg' src=${image}>
          </div>
          <p style='font-size:12px;'>${title}</p>
          <h2 style='font-size: 15px;'>Rs ${priceInINR}.00</h2>` +
          `<i class='fa-solid fa-trash' onclick='delElement(${j++})'></i></div>`
        );
      })
      .join('');
  }
}
