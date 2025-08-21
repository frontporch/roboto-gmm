# Use the official Nginx image as the base (Alpine variant for smaller size)
FROM nginx:alpine

# Install bash for ecs exec and gettext for envsubst
RUN apk update && \
    apk add --no-cache bash gettext && \
    which bash && \
    ls -l /bin/bash && \
    which envsubst && \
    ls -l /usr/bin/envsubst

# Copy the Nginx configuration template
COPY ./nginx.conf /etc/nginx/nginx.conf.template

# Copy your static files into Nginx's default web root directory
COPY ./published/ /usr/share/nginx/html

# Expose port 80 (Nginx listens on this by default)
EXPOSE 80

# Use envsubst to replace ${ALLOWED_ORIGIN} and start Nginx
CMD ["sh", "-c", "envsubst '${ALLOWED_ORIGIN}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]