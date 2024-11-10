

Deploy WordPress and MySQL with Docker Compose 

**Step 1: Install Docker and Docker Compose**
- Ensure Docker and Docker Compose are installed and running on your system.

**Step 2: Create a Project Directory**

1. Open a terminal and create a new directory for this setup:
   ```bash
   mkdir wordpress-docker
   cd wordpress-docker
   ```

**Step 3: Create the Docker Compose File**

1. In the `wordpress-docker` directory, create a file named `docker-compose.yml` with the following content:

   ```yaml
   version: '3.8'

   services:
     db:
       image: mysql:latest
       container_name: wordpress-mysql
       restart: always
       environment:
         MYSQL_ROOT_PASSWORD: password
         MYSQL_DATABASE: wordpress
         MYSQL_USER: user
         MYSQL_PASSWORD: password
       volumes:
         - db_data:/var/lib/mysql

     wordpress:
       image: wordpress:latest
       container_name: wordpress
       restart: always
       depends_on:
         - db
       ports:
         - "8080:80"
       environment:
         WORDPRESS_DB_HOST: db:3306
         WORDPRESS_DB_NAME: wordpress
         WORDPRESS_DB_USER: user
         WORDPRESS_DB_PASSWORD: password
       volumes:
         - wordpress_data:/var/www/html

   volumes:
     db_data:
     wordpress_data:
   ```

**Explanation of docker-compose.yml**

- **db service**:
  - Uses the `mysql:latest` image for MySQL.
  - Sets environment variables for MySQL root password, database name, user, and password.
  - Maps the database data to the `db_data` volume for data persistence.

- **wordpress service**:
  - Uses the `wordpress:latest` image.
  - Depends on the `db` service, ensuring MySQL starts first.
  - Maps port `8080` on the host to port `80` in the WordPress container (access WordPress at `http://localhost:8080`).
  - Configures WordPress to connect to the MySQL database with the provided credentials.

**Step 4: Start the Docker Compose Setup**

1. In the terminal, start the services with:
   ```bash
   docker-compose up -d
   ```
   - This command downloads necessary images, creates containers, and starts them in detached mode (`-d` flag).

**Step 5: Access the WordPress Frontend**

1. Open a web browser.
2. Go to `http://localhost:8080`.
   - This should open the WordPress installation page. Follow the on-screen instructions to complete the setup.

**Step 6: Verify the Containers are Running**

1. To check if both containers are running, use:
   ```bash
   docker-compose ps
   ```
   - You should see both `wordpress` and `wordpress-mysql` containers listed and marked as "Up".

---
