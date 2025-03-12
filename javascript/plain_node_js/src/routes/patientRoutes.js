import { notFoundHandler } from "./errorHandler.js";

// Route handler for GET /api/patients
const getPatientsHandler = (req, res, patients) => {
    res.write(JSON.stringify(patients));
    res.end();
};

// Route handler for GET /api/patients/:id
const getPatientByIdHandler = (req, res, patients) => {
    const id = req.url.split('/')[3];
    const user = patients.find((user) => user.id === parseInt(id));
    if (user) {
        res.write(JSON.stringify(user));
        res.end();
    } else {
        notFoundHandler(req, res, "Patient not found")
    }
};

// Route handler for a POST request to /api/patients
const createPatientHandler = (req, res, patients) => {
    let body = '';
    // Listen for data
    req.on('data', (chunk) => {
        body += chunk.toString();
    });
    req.on('end', () => {
        const newPatient = JSON.parse(body);
        // TODO: add database call instead
        patients.push(newPatient);
        res.statusCode = 201;
        res.write(JSON.stringify(newPatient));
        res.end();
    })
}

export  {
    createPatientHandler,
    getPatientsHandler,
    getPatientByIdHandler
}
