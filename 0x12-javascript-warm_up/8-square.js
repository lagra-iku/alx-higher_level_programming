#!/usr/bin/node

if (parseInt(process.argv[2])) {
  for (let x = 0; x < process.argv[2]; x++) {
    let row = '';
    for (let i = 0; i < process.argv[2]; i++) row += 'X';
    console.log(row);
  }
} else {
  console.log('Missing size');
}
