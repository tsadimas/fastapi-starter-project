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
* set client authentication on
* set root url, home url to http://fastapi:8000
* set valid redirects URIs to http://fastapi:8000/*
* in capability config enable Client authentication
* in credentials tab get client secret
* get public key from http://keycloak:8080/realms/hulk and store it on a file
* create a user in realm

```bash
curl --location --request POST 'http://keycloak:8080/realms/hulk/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=backend-client' \
--data-urlencode 'client_secret=GeUpsEQYZHdPIf2xaYjVMGtsfOlMdizv' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=sheldon@pasadena.com' \
--data-urlencode 'password=sheldon'

curl --location --request POST 'http://fastapi:8000/artists' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQMENlVm9qRHRmWU53eGhRNElrMHpHbE5mWm5qVjV6a1JqZURWRzhLeEJVIn0.eyJleHAiOjE2ODAwODM1NzQsImlhdCI6MTY4MDA4MzI3NCwianRpIjoiNDg4ODczZmUtOGY1ZS00OGIxLWE2NmEtYzE2NGJhOWRkMzFjIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL2h1bGsiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZWIxMmVhMDktODNlYy00OTUyLThlNTItNDg0ZTFjOGYwMzJkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYmFja2VuZC1jbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiNmI3NDMxNjItNTgzZC00MGVhLTkyYjUtYjEzZTMzZWRkNjA1IiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vZmFzdGFwaTo4MDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1odWxrIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiNmI3NDMxNjItNTgzZC00MGVhLTkyYjUtYjEzZTMzZWRkNjA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6InNoZWxkb24iLCJnaXZlbl9uYW1lIjoiIiwiZmFtaWx5X25hbWUiOiIiLCJlbWFpbCI6InNoZWxkb25AcGFzYWRlbmEuY29tIn0.k4jeK1hPV-VR4cM2y173ZQ31HT7ZcYnnZlbR3yTz944eDBFob1Y20Ys4DYqhKE9noQUA-hvNN4ThFK4oejvSvMt4-no72iGaW-o7YSGIKSwrIJ1VzteKiSRlkUZMzZ6BXy25MV2i4bq399KIQaMs9ncGpp5Ln7zRSfVSUlZmDkxcLMgImo-TRyv1Pgwh4VJ14dXTF9vYWFV0cOmxfZAhV2aBaGFFJngkF_4yxFRPAeUCWvd0HHYaKuEmQ4GFcWiuArT_NxONZnuLTxlR-wqXxUeHH1W82ZAYxVZmJ59Ei9F-ppwYHZJZvJSo3IrZyjqGfYbFFSRYvXoi6K8fXusecQ' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "string",
  "surname": "string"
}'

```


* Links
* [intro to keycloak](http://www.mastertheboss.com/keycloak/introduction-to-keycloak/)
* Useful

```bash
truncate artist restart identity cascade;
```


# FrontEnd

https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/

