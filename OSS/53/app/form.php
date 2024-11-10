<?php
$servername = "localhost";  // Keep as localhost because you're connecting to MySQL from within the same container
$username = "admin";        // The MySQL username you created
$password = "your_password"; // The password you assigned to the admin user
$dbname = "student_db"; 

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the form data
$name = $_POST['name'];
$prn = $_POST['prn'];

// Insert data into the database
$sql = "INSERT INTO students (name, prn) VALUES ('$name', '$prn')";

if ($conn->query($sql) === TRUE) {
    echo "New student registered successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>