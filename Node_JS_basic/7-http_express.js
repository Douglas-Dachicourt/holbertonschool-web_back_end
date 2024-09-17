const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.end('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.writeHead(200, { 'Content-type': 'text/plain' });
  res.write('This is the list of our students\n');
  countStudents('./database.csv')
    .then((data) => {
      res.end(data);
    });
});

app.listen(1245);

module.exports = app;
