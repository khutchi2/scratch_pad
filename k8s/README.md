# K8s

## Helm
- Kind of like a K8s package manager -- lets you find and install software easily to a cluster
- Installed locally, then connects to your K8s cluster and performs operations on it
- Software is installed using an add, update, install pattern.  For example, for the homarr application:
``bash
helm repo add homarr-labs https://homarr-labs.github.io/charts/
helm repo update
helm install homarr homarr-labs/homarr
```
- It's kind of an entire K8s app rolled up into one thing -- deployments, pods, services, pvc, etc.
- You can pass your Helm chart a values.yaml file to change the default parameters of the chart

## Monitoring
- Prometheus and Grafana are the defacto standard for K8s monitoring
- Installing the helm chart is simple: https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/README.md 
- If you need to view a default value (like an admin password, for example), do `helm show values <repo> >> default-values.yaml`
- Values can be changed fairly easily by `helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring --values values.yaml`
- Several pods get spun up:
    - alertmanager: can send out notifications to email, etc. if certain thresholds are met (e.g. memory usage at 80% capacity)
    - kube-prom-prometheus: the pod holding the metrics
    - grafana: the UI/visualization component (there's an associated service we can port-forward to)
    - prom-operator: simplifies deploying prometheus on K8s
    - kube-state-metrics: gathers K8s metrics and forwards them to prometheus
    - node-exporter: agent that runs on nodes and collects node performance metrics