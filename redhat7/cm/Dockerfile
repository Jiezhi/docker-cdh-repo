FROM httpd:2.4

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

ENV HTTP_DIR /usr/local/apache2/htdocs/cloudera-repo

RUN set -ex; \
  apt update; \
  apt install -y --no-install-recommends wget ca-certificates; \
  apt autoremove -y; \
  rm -rf /var/lib/apt/lists/*; \
  mkdir -p $HTTP_DIR; \
  wget -nv --recursive --no-parent --no-host-directories https://archive.cloudera.com/cm6/6.3.1/redhat7/ -P $HTTP_DIR ;\
  wget -nv --recursive --no-parent --no-host-directories https://archive.cloudera.com/cm6/6.3.1/allkeys.asc -P $HTTP_DIR ;\
  chmod -R ugo+rX $HTTP_DIR
