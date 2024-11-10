---

**Using Redmine for Bug Tracking with Docker**

---

Step 1: Run a PostgreSQL Container for Redmine

# Run a PostgreSQL container as Redmine's database.
docker run -d --name redmine-postgres -e POSTGRES_USER=redmine -e POSTGRES_PASSWORD=redminepassword -e POSTGRES_DB=redmine postgres:13

Explanation:
- `POSTGRES_USER=redmine` sets the database user to `redmine`.
- `POSTGRES_PASSWORD=redminepassword` sets the user password.
- `POSTGRES_DB=redmine` creates a database named `redmine`.

---

Step 2: Run the Redmine Container

# Run the Redmine container linked to the PostgreSQL container.
docker run -d -p 8081:3000 --name redmine --link redmine-postgres:postgres redmine

Explanation:
- `-p 8081:3000` maps port 8081 on your host to port 3000 in the container.
- `--link redmine-postgres:postgres` links the Redmine container to the PostgreSQL container for database access.

---

Step 3: Access Redmine in Your Browser

1. Open a web browser and navigate to:
   http://localhost:8081

2. Use the following database settings during the initial setup:
   - Database type: PostgreSQL
   - Hostname: postgres
   - Database name: redmine
   - Username: redmine
   - Password: redminepassword

---

Step 4: Log into Redmine

1. Open Redmine in your browser at:
   http://localhost:8081

2. Log in with the default credentials:
   - Username: admin
   - Password: admin

3. Change the password: Redmine will prompt you to change the default password for security purposes.

---

Step 5: Create a New Project and Track Issues

1. **Create a New Project**:
   - From the Redmine dashboard, go to **Projects** > **New Project**.
   - Enter the project details (name, description, etc.).
   - Click **Create**.

2. **Create an Issue**:
   - Within your project, go to **Issues** > **New Issue**.
   - Fill in details for the issue (title, description, priority, status).
   - Click **Create** to save the issue.

---

**Pushing the Docker Image**

# To create your own Redmine Docker image and push it to a repository (e.g., Docker Hub):


1. Login on the docker : 
   docker login

2. Push the Image to Docker Hub:


docker tag yourusername/redmine-custom:latest
docker push yourusername/redmine-custom