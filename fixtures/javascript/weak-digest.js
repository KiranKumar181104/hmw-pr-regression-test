const crypto = require('node:crypto');

function probe(value) {
  return crypto.createHash('md5').update(value).digest('hex');
}
