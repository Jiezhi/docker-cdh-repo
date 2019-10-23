FROM httpd:2.4

ENV HTTP_DIR /usr/local/apache2/htdocs/cloudera-repo

RUN set -ex; \
  apt update; \
  apt install -y --no-install-recommends wget ca-certificates; \
  apt autoremove -y; \
  rm -rf /var/lib/apt/lists/*; \
  mkdir -p $HTTP_DIR; \
  wget https://archive.cloudera.com/cm6/6.3.1/repo-as-tarball/cm6.3.1-redhat7.tar.gz -P $HTTP_DIR; \
  chmod -R ugo+rX $HTTP_DIR
