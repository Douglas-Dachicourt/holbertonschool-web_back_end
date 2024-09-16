process.stdin.setEncoding('utf-8');

process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const input = process.stdin.read();
  const yourNameIs = 'Your name is: ';
  if (input !== null) {
    process.stdout.write(`${yourNameIs}${input.trim()}\n`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
