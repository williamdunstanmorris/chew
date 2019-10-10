# Chew

# Why Chew
If you're chewin' the cud, fat or rag and pointlessly tweaking your devops configurations and scripts, that's not good. Chew can help you abstract some of these scripts back into a developer-esque workflow.

## Overview [![GoDoc](https://godoc.org/github.com/williamdunstanmorris/Morf?status.svg)](https://godoc.org/github.com/williamdunstanmorris/Morf)

A python package for managing scripts, playbooks and files. It's an object-orientated python package for helping you both generate and maintain your scripts at a higher level.

Chew currently helps you generate scripts and maintain
 the following technologies:
 
**Continuous Integration**
* Gitlab-CI (.gitlab-ci.yml)
* Jenkins (Jenkinsfile)
* CircleCI ()
* Travis (.travis-ci.yml)

**Containerisation**
* Docker (Dockerfile)
* Docker-Compose (.docker-compose.yml)
* Kubernetes (config)

**Configuration Management**
* Ansible
* Terraform
* Hashicorp

## Prerequisites 
Even if you're not a python veteran, you can produce a script with only a few lines of code! 

A presumed understanding of some DevOps practices are assumed here, but if you come here as a developer, this tool is a great way to get up with some of the DevOps scripts and lingo :)
## Install

```
go get github.com/williamdunstanmorris/Morf
```

## Contributing

### Development

### Git Workflow

### Docker + Jenkins (Environments and CI/CD w AWS)

Many organizations use Docker to unify their build and test environments across machines, and to provide an efficient mechanism for deploying applications. Starting with Pipeline versions 2.5 and higher, Pipeline has built-in support for interacting with Docker from within a Jenkinsfile.


### Docker [![docker build](https://img.shields.io/docker/automated/williamdunstanmorris/morf.svg)](https://hub.docker.com/r/williamdunstanmorris/morf)

## Contributors

ToDo.

## Author

ToDo.

## Future Work 

Eventually, a more elaborate version of the Chew CLI will be converted into Golang, for better cross-compatibility, and directly installable via brew, apt-get and other package-installers out there.
