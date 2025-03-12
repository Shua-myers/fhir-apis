// Not found handler
const notFoundHandler = (req, res, message) => {
    res.statusCode = 404;
    res.write(JSON.stringify({ message: `${message}`}));
    res.end();
};

export {
    notFoundHandler
}
