import jwt from "jsonwebtoken";

let token;

function writeJWT() {
    token = jwt.sign({ /* Payload data */ }, 'secret_key');
    document.cookie = `jwt=${token}; SameSite=None; Secure`;
}

function readJWT() {
    const cookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('jwt='));
    const token = cookie ? cookie.split('=')[1] : null;
}