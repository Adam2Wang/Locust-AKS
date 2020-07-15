

# LOCUST on Azure Kubernetes

###### tags: `Loading Test`

> LOCUST on AKS guide


## :memo: Where do I start?

### Cluster Deployment

```
git clone https://github.com/Adam2Wang/Locust-AKS.git

kubectl create -f locust-cm.yaml -f scripts-cm.yaml -f master-deployment.yaml -f service.yaml -f slave-deployment.yaml
```

### Application Gateway Ingress Controller (AGIC) Setup

We need application gateway to access pod inside, the followeing link will show you how to setup Azure AGIC

Greenfield Deployment: https://github.com/Azure/application-gateway-kubernetes-ingress/blob/master/docs/setup/install-new.md

After setup, you can get external IP address through
```
kubectl get ingress
```
Then go to this IP you could see the Locust Web UI and set the **number of users** & **ramp rate** to start your test. 

![](https://i.imgur.com/iwDxobl.png)



### Usage

#### locustfile

In `scripts-cm.yaml`, you can customized testing script in `data` part

#### Number of Workers

If your loading task need more workers to simulate, you could check `slave-deployment.yaml` and modify number after `replicas: `

#### Pod Image

Pod image can also be customized, command and parameter could be modified in `entrypoint.sh` (Ex: tags)

Once the new image has been built, check `master-deployment.yaml` & `slave-deployment.yaml` to modify image

### Prometheus & Grafana

#### Exporter

```
git clone https://github.com/ContainerSolutions/locust_exporter.git
```
Before Running, remember to modify the default URL to your **Application Gateway IP**

```
go run main.go
```
Then you can check metrics at http://localhost:9646/metrics

![](https://i.imgur.com/RiQW1sP.png)


#### Prometheus Server
```
docker run -itd -p 9090:9090 -v ~/YOUR_YAML_FILE_PATH/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```
After running this command, you could check prometheus UI at http://localhost:9090

![](https://i.imgur.com/QZbEXeC.png)

#### Grafana

```
docker pull grafana/grafana
docker run -d -p 3000:3000 grafana/grafana
```
You can check grafana at http://localhost:3000 and import data source from prometheus

![](https://i.imgur.com/L5zXQmH.png)

After successfully importing, we could add dashboard through uploading Locust.json file

![](https://i.imgur.com/E1MPnDD.png)

The Final Result! We have a nice look dashboard to check our locust!

![](https://i.imgur.com/XatlQL3.png)



---
- And MORE ➜ [HackMD Tutorials](https://hackmd.io/c/tutorials)
