// src/server.js

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const HOST_DIR = process.env.HOST_DIR || '/mounted';

// Endpoint to list files
app.get('/files', (req, res) => {
    fs.readdir(HOST_DIR, (err, files) => {
        if (err) {
            return res.status(500).json({ error: 'Unable to read directory' });
        }
        res.json(files);
    });
});

// Endpoint to get a specific file's contents
app.get('/files/:filename', (req, res) => {
    const filePath = path.join(HOST_DIR, req.params.filename);
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(404).json({ error: 'File not found' });
        }
        res.send(data);
    });
});

app.listen(PORT, () => {
    console.log(`File Viewer API running on http://localhost:${PORT}`);
    console.log(`Serving files from ${HOST_DIR}`);
});
