import express from 'express';
import { createClient, print } from 'redis';
import { promisify } from 'util';
const app = express();
const port = 1245;
const client = createClient();
const getAsync = promisify(client.get).bind(client);


const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];


const getItemById = (id) => {
  return listProducts.find(({ itemId }) => itemId === id);
};


const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, (err, reply) => {
    if (err) {
      print(`Reply: ${err}`);
    } else {
      print(`Reply: ${reply}`);
    }
  });
};


const getCurrentReservedStockById = async (itemId) => {
  const stock = await(getAsync(`item.${itemId}`));
  return stock;
};


app.get('/list_products', (_, res) => {
  res.status(200).json(listProducts);
});


app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product) {
    const { initialAvailableQuantity: stock } = product;
    let currentStock = await getCurrentReservedStockById(itemId);
    currentStock = currentStock ? currentStock : stock;
    res.status(200).json({ ...product, currentQuantity: currentStock });
  } else {
    res.status(404).json({"status":"Product not found"});
  }
});


app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product) {
    const { initialAvailableQuantity: stock } = product;
    let currentStock = await getCurrentReservedStockById(itemId);
    currentStock = currentStock ? currentStock : stock;
    if (currentStock < 1) {
      res.json({ status:"Not enough stock available", itemId })
    } else {
      reserveStockById(itemId, currentStock - 1);
      res.status(200).json({ status:"Reservation confirmed", itemId });
    }
  } else {
    res.status(404).json({"status":"Product not found"})
  }
});


app.listen(port, () => {
  console.log(`Server listening on port ${port}...`);
});


client.on('connect', () => {
  console.log('Redis client connected to the server');
})
.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
