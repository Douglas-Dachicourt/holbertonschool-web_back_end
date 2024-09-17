const { argv } = require('process');
const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-type': 'text/plain' });
  const { url } = req;

  if (url === '/') {
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(argv[2])
      .then((data) => {
        res.end(data);
      });
  }
});

app.listen(1245);

module.exports = app;
