function probe(req) {
  return new Function(req.query.expression)();
}
