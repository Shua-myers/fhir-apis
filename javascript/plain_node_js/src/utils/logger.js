// usually in a separate file, Logger middleware
const logger = (req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();   // we're done, move on to the next middleware
};

export { logger };
