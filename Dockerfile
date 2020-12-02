FROM nginx
WORKDIR /affirmations
COPY . /var/www/html/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80 443