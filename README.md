# 3tier-app

## Three Tier Architecture selected here for Demo is:
- A simple Python Flask Web App 
- A MySQL Database for backend

EKS Cluser was deployed using terraform v.12 to host both the application and Database.
So we can reproduce the whole stack whenever we need to redeploy.
This is presented in Challenge1

## Python Flask Web App 
The app creates a DB called PARADB and a TABLE called 'users'. The App uses 3 routes

@app.route('/init'): To initialise the DB and TABLE 

@app.route('/addusers', methods=['GET', 'POST']): To add data into 'users' table using index.html

@app.route('/getusers'): To get the data from a table in example.html

## Docker Image

Docker image was pushed to dockerhub repo, venpara/ven-app:latest


## For testing purposes, here I used 'minikube' K8s cluster:

Here, the App & DB were deployed using kubectl manifests. In real world scenario, we can use CI/CD tools to deploy the application.
A secret is used for storing the DB password but in the real world we use 'vault' for storing the secrets.
The manifests are present in k8s folder.

Commands to deploy the mysql-db container:

```
kubectl apply -f k8s/mysql-deployment.yml
```
NOTE: makesure 'PARADB' database is present before deploying the testapp container in Kubernetes.


Commands to deploy the 'testapp':

```
$ kubectl apply -f k8s/app-deployment.yml 
deployment.apps/testapp configured
service/testapp unchanged

$ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP          13d
mysql        LoadBalancer   10.103.85.123   10.103.85.123   3306:30283/TCP   5h26m
testapp      LoadBalancer   10.102.226.23   10.102.226.23   8000:32102/TCP   7m8s

$ kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
mysql-5cc845b476-nlr4b   1/1     Running   1          5h26m
testapp-797544dd-gqmhd   1/1     Running   0          7m13s
testapp-797544dd-qj5qp   1/1     Running   0          7m13s
testapp-797544dd-wnvpf   1/1     Running   0          7m13s
$ 
```

## To Check the app is working or Not:

On the web browser, try

To initialize the DB:

http://{EXTERNAL-IP}:8000/init  where EXTERNAL-IP is 10.102.226.23 as per the 'kubectl get svc' output above.


To Add users to 'users' table:

http://{EXTERNAL-IP}:8000/addusers


To see the updated 'users' table:

http://{EXTERNAL-IP}:8000/getusers




