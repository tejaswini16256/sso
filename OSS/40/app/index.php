<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Registration</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h2>Register a Student</h2>
  <form action="form.php" method="POST">
    <label for="name">Student Name:</label>
    <input type="text" id="name" name="name" required><br><br>
    
    <label for="prn">Student PRN:</label>
    <input type="text" id="prn" name="prn" required><br><br>

    <button type="submit">Submit</button>
  </form>
</body>
</html>