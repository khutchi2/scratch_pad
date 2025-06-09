# HELM
## What is HELM?
- K8s just looks at the yaml files and makes it happen.  It doesn't really have any idea that they're all together
- HELM is meant to put it all into context
- It's a K8s package manager.  Each manifest is part of the overall package.  When you use HELM you act on the package, it takes care of the details.
## What is a HELM chart?
- A HELM chart has everything needed to deploy an application to a K8s cluster
- There are hubs of HELM charts available: artifacthub.io, bitnami
    - Searchable via web
    - Or, searchable via:
    ```bash
    helm search hub <name-of-package>
    ```
## Using HELM
Some basic commands:
```bash
helm repo add <name-of-repo>
helm search repo <name-of-repo>
helm repo list
helm install <release-name> <chart-location>
helm uninstall <release-name>
helm pull <name-of-repo> # just downloads a repo
helm upgrade <name-of-release> <chart-location> --values <path_to_values_file>
```

## values.yaml file
- Provides a way to pass a set of "variable" names if you will to your various K8s manifests.  It's kind of like HELM has an autocompletion feature and the values.yaml file is a specific dictionary for that.
- When inserting this "autocompleted" value into a manifest in the templates directory, you'll do something like
```yaml
{{.Values.<value_name>}}
```
So for example, instead of having to define the app name as "my-super-cool-app" you can define that once in values.yaml as 
```yaml
appName: my-super-cool-app
```
and then point to that in the various manifests as
```yaml
{{.Values.appName}}
```
This provides several advantages
- Easier to modify values across several manifest files
- Don't have to worry about breaking your app by mistyping something in one manifest file
- Central location to see all of your various values and names

## values.yaml for dev and prod
- You can setup your templating such that it can apply for different environments
- For example, you might have a `values_dev.yaml` with `namespace: dev`, and `values_prod.yaml` with `namespace: prod`
- When you install this application, you'll do the following
```bash
helm install <release-name> <chart-location> --values <chart-location>/values.yaml -f <chart-location>/values_dev.yaml -n dev
```
This says, install this app using these default values.  Overwrite any defaults with special values in `values_dev.yaml` and do it in HELM release namespace `dev`


## Good resources
- https://www.youtube.com/watch?v=jUYNS90nq8U&ab_channel=DevOpsJourney 