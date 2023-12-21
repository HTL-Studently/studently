#!/bin/bash
# From https://dev.to/karvounis/advanced-traefik-configuration-tutorial-tls-dashboard-ping-metrics-authentication-and-more-4doh

# Clear already existing direcotry
echo "Clearing old direcotry"
rm -rfd certs/

# Create cert directories
echo "Creating new direcotry"
mkdir -p certs/{ca,traefik}

# Create Certificate Authority
echo "Creating Certificate Authority"
openssl genrsa -out certs/ca/rootCA.key 4096
openssl req -x509 -new \
    -nodes \
    -sha256 \
    -days 3650 \
    -key certs/ca/rootCA.key \
    -subj "/C=AT/L=Carinthia/O=Studently/CN=Studently/OU=Studently" \
    -out certs/ca/rootCA.pem

# Create Traefik certificates
echo "Creating Traefik Certificates"
openssl genrsa -out certs/traefik/traefik.key 4096
openssl req -new \
    -key certs/traefik/traefik.key \
    -subj "/C=AT/L=Carinthia/O=Studently/CN=Studently/OU=Studently" \
    -out certs/traefik/traefik.csr
openssl x509 -req \
    -sha256 \
    -days 365 \
    -CA certs/ca/rootCA.pem \
    -CAkey certs/ca/rootCA.key \
    -CAcreateserial \
    -in certs/traefik/traefik.csr \
    -out certs/traefik/traefik.crt

echo "Done"