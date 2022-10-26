# REST API Python App with Flask and PostgreSql

How to run:
```bash
# docker-compose up --build -d
make build

# docker-compose down -v 
make down

# show logs
make show_logs
```


## Helm install 

```bash
cd charts
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update

helm install postgresql-release bitnami/postgresql -f ./charts/bitnami/postgres/values.yaml

helm install nginx-release -f nginx-ingress-values.yaml nginx-stable/nginx-ingress

helm install test-rest-api-release test-rest-api/ -f ./test-rest-api/values.yaml
```


## Helm uninstall

```bash
helm uninstall test-rest-api-release
helm uninstall nginx-release
helm uninstall postgresql-release
```