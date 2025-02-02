# Stage 1
FROM alpine:latest AS build

# Install required packages
RUN apk update && apk add --no-cache git hugo

# Create and set the working directory
WORKDIR /opt/homepage

# Clone the repository
RUN git clone https://github.com/dartungar/dartungar-homepage.git . && git submodule update --init

# Run Hugo in the Workdir to generate HTML.
RUN hugo --minify

# Stage 2
FROM nginx:1.25-alpine

# Set workdir to the NGINX default dir.
WORKDIR /usr/share/nginx/html

# Copy HTML from previous build into the Workdir.
COPY --from=build /opt/homepage/public .

# Expose port 80
EXPOSE 80/tcp
