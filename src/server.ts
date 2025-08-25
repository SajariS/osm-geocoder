import express from "express";

const app = express();
const PORT = parseInt(process.env.PORT as string, 10);
const IP = process.env.IP || "127.0.0.1";

app.use(express.json());

//Kirjoita rajapinnat tähän

app.listen(PORT, IP, () => {
    console.log(`Server running on http://${ip}:${PORT}`);
})