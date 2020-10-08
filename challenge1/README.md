# Provision an EKS Cluster

After installing the AWS CLI. Configure it to use your credentials.

```shell
$ aws configure
AWS Access Key ID [None]: <YOUR_AWS_ACCESS_KEY_ID>
AWS Secret Access Key [None]: <YOUR_AWS_SECRET_ACCESS_KEY>
Default region name [None]: <YOUR_AWS_REGION>
Default output format [None]: json
```

After you've done this, initalize your Terraform workspace, which will download 
the provider and initialize it with the values provided in the `terraform.tfvars` file.

```shell
$ terraform init
Initializing modules...

Initializing the backend...

Initializing provider plugins...
- Using previously-installed hashicorp/template v2.1.2
- Using previously-installed hashicorp/kubernetes v1.13.2
- Using previously-installed hashicorp/random v2.3.0
- Using previously-installed hashicorp/local v1.4.0
- Using previously-installed hashicorp/null v2.1.2
- Using previously-installed hashicorp/aws v3.9.0
...
...
Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary

Terraform has been successfully initialized!
```

Then, provision your EKS cluster by running `terraform apply`. This will 
take approximately 10 minutes.

```shell
$ terraform apply

# Output truncated...

Plan: 52 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

# Output truncated...

Apply complete! Resources: 51 added, 0 changed, 0 destroyed.

Outputs:

cluster_endpoint = https://38C5A78E6E9168C636C95C9F98088931.gr7.us-east-2.eks.amazonaws.com
cluster_name = ven-eks-922cYXFJ
cluster_security_group_id = sg-001aaf99a7b1cb561
config_map_aws_auth = [
  {
    "data" = {
      "mapAccounts" = "[]\n"
      "mapRoles" = "- \"groups\":\n  - \"system:bootstrappers\"\n  - \"system:nodes\"\n  \"rolearn\": \"arn:aws:iam::060013981027:role/ven-eks-922cYXFJ2020100818005343900000000a\"\n  \"username\": \"system:node:{{EC2PrivateDNSName}}\"\n"
      "mapUsers" = "[]\n"
    }
    "id" = "kube-system/aws-auth"
    "metadata" = [
      {
        "generate_name" = ""
        "generation" = 0
        "name" = "aws-auth"
        "namespace" = "kube-system"
        "resource_version" = "515"
        "self_link" = "/api/v1/namespaces/kube-system/configmaps/aws-auth"
        "uid" = "83d6c4d4-93f3-47ca-983c-a85e4f67b3f0"
      },
    ]
  },
]
kubectl_config = apiVersion: v1
preferences: {}
kind: Config

clusters:
- cluster:
    server: https://38C5A78E6E9168C636C95C9F98088931.gr7.us-east-2.eks.amazonaws.com
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJd01UQXdPREUzTlRjME1Wb1hEVE13TVRBd05qRTNOVGMwTVZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTXZECjFDZUpSZm9VWi94ZmsvaU1qM3ZOMTZWRzNqZXZ1SWRsMW5xb3M4T3Rqc0Qwb1lrb2tiWFZRZkJ2YjBmVy9rRXkKK1JpNWIyeERTUXY2UDNmRnE2aUs1dzBRaEdiN0pyMXNBdjJuYlpKdm13d0hvRTREWnlZQ1ViY25WVFd0VDZKRQpwajdMU3Mwa3puZ1hmeVkrQ2hYeGpZd0pUeGprQU1adWxJeG9URzlHWVpzM3VGT2pPdlZKOXdLY1I0MWZpdDR1CkYxdlVKVFlVeFNpWkwvSVBJTUw2THN2MG1KYWJtZ1lVTHROZkxyZlQ1OUp1d29rd0ZxS0lYL2VMN3EyMU9TTEIKL2M5WDJwSEVVU1VMekVDakcrNXZPaTlzM3FqL0lkNUNoRlVmWDE2N2JWZUtGNkcrZTlzK20zem5lanF5UFYzTQptQUpBUTlqNlY1S1YyS2wwSFIwQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFDNHRJQmhCNjA4dVMxWDdabEVyRmNjSkRNK1QKNEN2R2xyNFVCaGZvVFZRbXFvSjFGUW1UWFFFU3REeXJrOUZoVk5wbWo2MS83VEJOQS8zR294ZnVqeTFuT2VERgpZelJmVlFqdkNldlhkcE96a3lZbE9NazRPdTI4eUdDaVptUzJjcjk2RERrWWRSZHBDTXRVWVdScTh6Yi8zb2tpCkgwUGsxYUhheHlpaEIzamhsWnVqVlp5YUt1VkZGcGUwbWdvMHI1empraWhPTWdlN1FMSTN6RXdDSGlFS3NWbWcKc0hWY1huWk84NkxWTjdYK1hUM1B6azZGWlJ6RUk2L0FDZGhlYUNKU2xtUVZSaVBzQ2ZOUDRvN3ZrMjJpQWtmNQp6OVQyeFc4UHFWWnhuRnlnSUF1Y0d2VUdjVU5TZVZsbktTQVJHMDJsekRrcXU1bVZzS2FvTkpqbWYwaz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
  name: eks_ven-eks-922cYXFJ

contexts:
- context:
    cluster: eks_ven-eks-922cYXFJ
    user: eks_ven-eks-922cYXFJ
  name: eks_ven-eks-922cYXFJ

current-context: eks_ven-eks-922cYXFJ

users:
- name: eks_ven-eks-922cYXFJ
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1alpha1
      command: aws-iam-authenticator
      args:
        - "token"
        - "-i"
        - "ven-eks-922cYXFJ"

region = us-east-2
ubuntu@ven-master
```

## Configure kubectl

The following command will get the access credentials for your cluster and automatically
configure `kubectl`.

```shell
$ aws eks --region $(terraform output region) update-kubeconfig --name $(terraform output cluster_name)

$ kubectl get nodes
NAME                                       STATUS   ROLES    AGE     VERSION
ip-10-0-2-152.us-east-2.compute.internal   Ready    <none>   3h59m   v1.16.13-eks-ec92d4
ip-10-0-2-92.us-east-2.compute.internal    Ready    <none>   3h59m   v1.16.13-eks-ec92d4
ip-10-0-3-54.us-east-2.compute.internal    Ready    <none>   3h59m   v1.16.13-eks-ec92d4



```

