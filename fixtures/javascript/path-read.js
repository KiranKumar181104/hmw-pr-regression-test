const fs = require('node:fs');

function probe(req) {
  return fs.readFileSync(req.query.path, 'utf8');
}
