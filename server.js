const express = require('express');
const app = express();

app.post('/asfshfdjfgfhkbhmvbwebhofdgdfgfdgdfgzbdrrteuernfggok', (req, res) => {
  console.log('Webhook received!');
  // handle the webhook event
});

app.listen(3000, () => console.log('Server started'));
