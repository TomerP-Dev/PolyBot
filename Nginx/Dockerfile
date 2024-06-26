# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the Nginx configuration file into the container
COPY Nginx.conf /etc/nginx/nginx.conf

# Expose the port that Nginx will run on
EXPOSE 8334

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
