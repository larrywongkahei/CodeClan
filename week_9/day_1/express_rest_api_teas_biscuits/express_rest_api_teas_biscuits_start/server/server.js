const express = require('express');
const app = express();
const cors = require('cors');

const teas = [
  { name: "Early Grey", brand: "Twinings" },
  { name: "Irish Breakfast", brand: "Barry's Tea" },
  { name: "Lemon and Ginger", brand: "Lipton" },
  { name: "Rooibos", brand: "Tick Tock" },
  { name: "Green", brand: "Clipper" }
];

const biscuits = [
  { name: "Digestives", brand: "McVitie's" },
  { name: "Hobnobs", brand: "McVitie's" },
  { name: "Shortbreads", brand: "Walkers" },
  { name: "Jammy Dodgers", brand: "Burton's" },
  { name: "Custard Creams", brand: "Crawford's" }
];

app.use(cors());
app.use(express.json());

const createRouter = require('./helpers/create_router.js')
const teasRouter = createRouter(teas)
const biscuistRouter = createRouter(biscuits)

app.use('/api/teas', teasRouter)
app.use('/api/biscuits', biscuistRouter)

app.listen(9000, function () {
  console.log(`App running on port ${ this.address().port }`);
});
