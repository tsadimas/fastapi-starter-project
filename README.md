## Run project locally with docker-compose

* copy .env.example to .env
```bash
cp app/.env.example app/.env
```

run with docker-compose

```bash
docker-compose -d --build
```


## Links
* [FastAPI with Async SQLAlchemy, SQLModel, and Alembic](https://testdriven.io/blog/fastapi-sqlmodel/)

## Pre commit Hooks

```bash
pip install pre-commit
```
create a sample pre-commits file
```bash
pre-commit sample-config > .pre-commit-config.yaml
```
edit this file to add hooks
install hooks
```bash
pre-commit install --install-hooks
```

## Container registry

# docker registry
## Github Packages
* create personal access token (settings --> Developer settings -- > Persnoal Access Tokens)
* tag an image
```bash
docker build -t ghcr.io/tsadimas/pms8-fastapi:latest -f fastapi.Dockerfile .
```
* login to docker registry
```bash
cat ~/github-image-repo.txt | docker login ghcr.io -u tsadimas --password-stdin
```
* push image
```bash
docker push ghcr.io/tsadimas/pms8-fastapi:latest
```

## Useful
```bash
truncate table artist restart identity cascade;
```

## create docker login secret
* create <AUTH> from the command
```bash
echo <USER>:<TOKEN> | base64
```
* create kubernetes secret
```bash
echo '{"auths":{"ghcr.io":{"auth":"<AUTH>"}}}' | kubectl create secret generic dockerconfigjson-github-com --type=kubernetes.io/dockerconfigjson --from-file=.dockerconfigjson=/dev/stdin
```

Links
* [pre-commit: A framework for managing and maintaining multi-language pre-commit hooks.](https://pre-commit.com/)
* [Github: Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
* [Personla access toksns](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

# Tests

run
```bash
tavern-ci tests
```
or
```bash
docker-compose exec fastapi tavern-ci tests
```

Links
* [tavern-testing](https://tavern.readthedocs.io/en/latest/examples.html)


# Keycloak

* create a realm, e.g. hulk
* create a client , e.g. backend-client
* set root url, home url to http://fastapi:8000
* set valid redirects URIs to http://fastapi:8000/*
* in capacity config enable Client authentication
* in credentials tab get client secret
* get public key from http://keycloak:8080/realms/hulk and store it on a file
* create a user in realm

* Links
* [intro to keycloak](http://www.mastertheboss.com/keycloak/introduction-to-keycloak/)
* Useful

```bash
truncate artist restart identity cascade;
```


# FrontEnd

https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/

