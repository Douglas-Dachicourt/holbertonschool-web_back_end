const express = require('express');

const app = express();

app.all('*', () => {
  console.log('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
