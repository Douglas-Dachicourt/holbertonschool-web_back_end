const { argv } = require('process');
const countStudents = require('./3-read_file_async');

const http = require('http');

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-type': 'plain/text' });
    const url = req.url;

    if (url === '/') {
        res.end('Hello Holberton School!');
    } else if (url === '/students') {
        console.log('This is the list of our students')
        countStudents(argv[2])
        .then(data => res.end(data));
    }
})

app.listen(1245);

module.exports = app;
