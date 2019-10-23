# Docker-CDH-repo
Mirror of CDH repository by Docker with httpd

## Why
This project aims to speed up your progress when you want to install [CDH](https://www.cloudera.com/downloads/cdh/6-3-1.html) at [Configuring a Local Package Repository](https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/cm_ig_create_local_package_repo.html), especially for developers from China.

## Where
The repository images are built automatically at [Docker Hub](https://hub.docker.com/r/lencent/cdh/tags).

You should choose the right one for your host to install HDP.

## How
> If you are from China, you should to configure Docker proxy, like [this](https://cr.console.aliyun.com/?spm=a2c4e.11153940.0.0.52027e29fNRb0v).

If you want to install CDH version `6.3.1` on `Centos 7`:

### Cloudera Manager
`docker run -dit --name cm-6.3.1 -p 8080:80 lencent/cdh:redhat7-cm-6.3.1`

or

`docker run --rm -it -p 8080:80 lencent/cdh:redhat7-cm-6.3.1`

### CDH
`docker run -dit --name cdh-6.3.1 -p 8090:80 lencent/cdh:redhat7-cdh-6.3.1`

or

`docker run --rm -it -p 8090:80 lencent/cdh:redhat7-cdh-6.3.1`

---

If you encounter any problems, just issue an issue.

