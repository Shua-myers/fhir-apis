import { createServer } from 'http';
import dotenv from 'dotenv';
import { createPatientHandler, getPatientsHandler, getPatientByIdHandler } from './routes/patientRoutes.js';
import { notFoundHandler } from './routes/errorHandler.js';
import { logger } from './utils/logger.js';
import { jsonMiddleware } from './middlewares/jsonMiddleware.js';

dotenv.config();

const PORT = process.env.PORT;

const patients = [
    {id: 1, name: 'John Doe'},
    {id: 2, name: 'Jane Smith'},
    {id: 3, name: 'Josh Myers'}
];

const server = createServer((req, res) => {
    logger(req, res, () => {
        jsonMiddleware(req, res, () => {
            if (req.url === '/api/users' && req.method === 'GET') {
                getPatientsHandler(req, res, patients);
            } else if (req.url.match(/\/api\/users\/([0-9]+)/) && req.method === 'GET') {
                getPatientByIdHandler(req, res, patients);
            } else if (req.url === '/api/users' && req.method === 'POST') {
                createPatientHandler(req, res, patients);
            } else {
                notFoundHandler(req, res, "Route not found");
            };
        });
    });
 });

 server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
