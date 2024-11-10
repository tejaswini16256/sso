# Use an official Ubuntu base image
FROM ubuntu:16.04

# Set environment variables for non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Update and install Apache, MySQL, PHP, and other dependencies
RUN apt-get update && \
    apt-get install -y apache2 mysql-server php libapache2-mod-php php-mysql && \
    apt-get clean

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Copy your application files into the Apache directory
COPY ./app /var/www/html
COPY ./mysql /var/lib/mysql

# Set working directory
WORKDIR /var/www/html;

# Expose the default HTTP port
EXPOSE 80

# Set default command to start Apache and keep container running
CMD service apache2 start && tail -F /var/log/apache2/*log
