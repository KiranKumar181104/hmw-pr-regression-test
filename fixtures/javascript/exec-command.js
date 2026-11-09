const { exec } = require('node:child_process');

function probe(req) {
  return exec(req.query.command);
}
