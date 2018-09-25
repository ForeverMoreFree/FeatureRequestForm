#Credit to Roman Dodin - dodin.roman@gmail.com for the base config files for Nginx and Supervisord

FROM alpine


# Copy python requirements file
COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache \
    python3 \
    bash \
    nginx \
    uwsgi \
    uwsgi-python3 \
    supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

# Copy the Nginx global conf
COPY nginx.conf /etc/nginx/
# Copy the Flask Nginx site conf
COPY flask-site-nginx.conf /etc/nginx/conf.d/
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/
# Custom Supervisord config
COPY supervisord.conf /etc/supervisord.conf

#Force no-cache on items run below here
RUN pwd

# Add demo app
COPY ./app /app
WORKDIR /app
ENV AM_I_IN_A_DOCKER_CONTAINER Yes
ENV FLASK_APP=main.py FLASK_ENV=development
RUN chmod -R 777 .

CMD ["/usr/bin/supervisord"]