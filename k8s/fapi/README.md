Fastapi k8s

```bash
kubectl create configmap fastapi-config --from-env-file=k8s/fapi/fastapi.env

kubectl create secret generic mysecret --from-literal=mypassord='abcdefh1234' --from-literal=myapikey='12345678'

kubectl create secret generic sqlfilesecret --from-file=assets/postgres/init.sql

```

https://my.noip.com/dynamic-dns


kubectl create namespace cert-manager
helm repo add jetstack https://charts.jetstack.io
helm repo update

kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.crds.yaml

helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.12.0


https://www.madalin.me/wpk8s/2021/050/microk8s-letsencrypt-cert-manager-https.html