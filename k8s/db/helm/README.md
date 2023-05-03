### install helm


```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```
Link 
* [install helm](https://helm.sh/docs/intro/install/)
### enable helm in microk8s

```bash
microk8s enable helm3
```
### add bitnami repo

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```
get helm values
```bash
helm show values bitnami/postgresql > helm/values.yaml
```
edit values and set storage and auth, as in example file
* create database namespace
```bash
kubectl create ns database
```
install helm chart
```bash
helm install postgres -f values.yaml bitnami/postgresql -n database
```

Link
* [bitnami postgres helm chart](https://bitnami.com/stack/postgresql/helm)