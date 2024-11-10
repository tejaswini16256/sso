const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 9000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// MySQL database configuration
const db = mysql.createConnection({
    host: 'localhost',      // or use '127.0.0.1'
    user: 'root',           // MySQL root user
    password: 'Mahesh@123', // Root password you set when creating the container
    database: 'mydatabase', // Database name you initialized
    port: 3308              // Port that the container is exposing
  });
  
  // Connect to the database
  db.connect((err) => {
    if (err) {
      console.error('Database connection failed:', err.stack);
      return;
    }
    console.log('Connected to MySQL database');
  });

// Route to display the HTML form
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route to handle form submission
app.post('/submit', (req, res) => {
  const { name, email } = req.body;

  if (name && email) {
    const sql = "INSERT INTO users (name, email) VALUES (?, ?)";
    db.query(sql, [name, email], (err, result) => {
      if (err) throw err;
      console.log("Record inserted successfully");
      res.send("Record inserted successfully!");
    });
  } else {
    res.send("Please enter both name and email");
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
