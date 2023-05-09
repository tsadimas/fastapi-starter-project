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
* create personal access token (settings --> Developer settings -- > Personal Access Tokens), select classic
* select write:packages
* save the token to a file
* to see packages, go to your github profile and select tab Packages
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

* create a .dockerconfigjson file, like this
```json
{
    "auths": {
        "https://ghcr.io":{
            "username":"REGISTRY_USERNAME",
            "password":"REGISTRY_TOKEN",
            "email":"REGISTRY_EMAIL",
            "auth":"BASE_64_BASIC_AUTH_CREDENTIALS"
    	}
    }
}
```


* create <BASE_64_BASIC_AUTH_CREDENTIALS> from the command
```bash
echo -n <USER>:<TOKEN> | base64
```
* create kubernetes secret
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: registry-credentials
  namespace: default
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: BASE_64_ENCODED_DOCKER_FILE
```
where BASE_64_ENCODED_DOCKER_FILE is
```bash
cat .dockerconfigjson | base64 -w 0
```


# Links
* [pre-commit: A framework for managing and maintaining multi-language pre-commit hooks.](https://pre-commit.com/)
* [Github: Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
* [Personal access toksns](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
* [Using Gitlab Private Registry with Kubernetes](https://chris-vermeulen.com/using-gitlab-registry-with-kubernetes/)
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


* Useful

```bash
truncate artist restart identity cascade;
```
