# Use nginx as the base image
FROM nginx:alpine

# Copy the website files to the nginx html directory
COPY Cursor/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
