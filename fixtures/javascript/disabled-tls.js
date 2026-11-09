const https = require('node:https');

function probe() {
  return new https.Agent({ rejectUnauthorized: false });
}
