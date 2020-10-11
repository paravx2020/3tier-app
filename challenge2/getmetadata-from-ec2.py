### Python program to query the meta data of an instance within aws and provide a json formatted output. 
###
#!/usr/bin/env python

import requests
import json


# Converts AWS EC2 instance metadata to a dictionary
def load():
    metaurl = 'http://169.254.169.254/latest'
    # meta-data subdirectories not exposed with a final '/'
    metadict = {'meta-data': {}}

    for subsect in metadict.keys():
        datacrawl('{0}/{1}/'.format(metaurl, subsect), metadict[subsect])

    return metadict


def datacrawl(url, d):
    r = requests.get(url)
    if r.status_code == 404:
        return

    for l in r.text.split('\n'):
        if not l: # "instance-identity/\n" case
            continue
        newurl = '{0}{1}'.format(url, l)
        # a key is detected with a final '/'
        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            datacrawl(newurl, d[newkey])

        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None



if __name__ == '__main__':
    print(json.dumps(load(),indent=4, sort_keys=True))
    
    
    
    
Note: There is a python module (called ec2-metadata 2.2.0) which can be used directly used to fetch the individual fileds of meta-data for a EC2 instance.
And the module can be imported into any python application and can be installed to any EC2 instance using pip.       
    
    
    
OUTPUT:

$ python getmetadata.py 
{
    "meta-data": {
        "ami-id": "ami-0bb3fad3c0286ebd5", 
        "ami-launch-index": 0, 
        "ami-manifest-path": "(unknown)", 
        "block-device-mapping": {
            "ami": "/dev/xvda", 
            "root": "/dev/xvda"
        }, 
        "events": {
            "maintenance": {
                "history": [], 
                "scheduled": []
            }
        }, 
        "hibernation": {
            "configured": false
        }, 
        "hostname": "ip-172-31-35-25.eu-west-1.compute.internal", 
        "identity-credentials": {
            "ec2": {
                "info": {
                    "AccountId": "060013981027", 
                    "Code": "Success", 
                    "LastUpdated": "2020-10-08T15:27:30Z"
                }, 
                "security-credentials": {
                    "ec2-instance": {
                        "AccessKeyId": "ASIAQ36I4VVRSRHKML67", 
                        "Code": "Success", 
                        "Expiration": "2020-10-08T21:29:10Z", 
                        "LastUpdated": "2020-10-08T15:27:18Z", 
                        "SecretAccessKey": "OkYdXPn+jCBd13WsfhpyKocsWkVKDw8Nq0Y2iXdy", 
                        "Token": "IQoJb3JpZ2luX2VjEPj//////////wEaCWV1LXdlc3QtMSJHMEUCIQD/swic1QDAw3DJAgXZROxGdpm2BqoPdNiFRvRYuvpUDwIgCqUpLwUwdBAymdmyAjAlrRGOhu7Vbpz/H3ZYU/RsUa0qvwMIMRABGgwwNjAwMTM5ODEwMjciDN0O4pDJIMVPg9YNeyqcA81K2ZqJrN7IWQClVMp40XxrhUis8ck3hxoEg0lCTxVQs/vY0jZvtjkZmLvunP6ZhSN30fsGo0ab/gfTOJAsBF3S/IZ6loUFBUExmaR7aMQ07+DHBIysK9HyVXNrrsO51hCHbXlv1aCts/SXnhLvcl6qMjt2erSb69CjXFxLlqCTLI7o3ONQFYjLUkS4tLUPL/IHTTU2gvobmrAUVbJjk6E7VbpleFIRjafi5rl2ulr7RdnNSyCc91xqWxRF2XtSbTAdGEKGKrVxXTi1sSPN1c46B9+ZILguihwy4CU9UfI4lz0BaqUPrATzTXWw9NR5CkqmGNMGWeWnAEhjBjZ8g2qDPy6HKykKBeEBfiywsvZWw8ZEB7cE3aAT9nnH5AaKfeR/TmfEiycaT2jv+YGfsyk6N5trFyWYGNT0xxGvxSZLpVK6SfQDwgVS0o/vmR2xdwggojO6Be2OzSjG+j/PBLX/w4aCFT+6cDsf8POSH038pmoQ5lAixmuPbw+TKB5/tL3AB79o3nOb5ISjnPCDrv38YOM3jJHKzOQP0WAw3d/8+wU65wHIK9Wao2PZEDS0tLwbCgidep3DSzKv3apFOeWqiqIx9zKpmkC9GY8I9PxRolDtDeU42HnOPG/7AyUa2/RmbVjYhidsFEFedOtOkb7MdG9xkSz52gmbKXrNxoRCSQ7isKIrUKKTR9ltA2IIAIjrQqhMCKf9isjY6EtMTqCkJlKxG/ixE3RL4QgjJwj89O/7YeVP1S946QHfa6abaI7D0girrpOfMUgXSfr4OV5GZZI9EWFWFviKHrLj+3pr7UPkarqinDP2/aO2Jfqr+idnCv2lqUNL6Bm4N0dgDvIXuDUi2OamaA+CKTs=", 
                        "Type": "AWS-HMAC"
                    }
                }
            }
        }, 
        "instance-action": "none", 
        "instance-id": "i-027bfb742ef089ed9", 
        "instance-life-cycle": "spot", 
        "instance-type": "t2.micro", 
        "local-hostname": "ip-172-31-35-25.eu-west-1.compute.internal", 
        "local-ipv4": "172.31.35.25", 
        "mac": "0a:73:13:1c:ca:ef", 
        "metrics": {
            "vhostmd": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        }, 
        "network": {
            "interfaces": {
                "macs": {
                    "0a:73:13:1c:ca:ef": {
                        "device-number": 0, 
                        "interface-id": "eni-007eaf7a9576804f9", 
                        "ipv4-associations": {
                            "34.241.176.71": "172.31.35.25"
                        }, 
                        "local-hostname": "ip-172-31-35-25.eu-west-1.compute.internal", 
                        "local-ipv4s": "172.31.35.25", 
                        "mac": "0a:73:13:1c:ca:ef", 
                        "owner-id": "060013981027", 
                        "public-hostname": "ec2-34-241-176-71.eu-west-1.compute.amazonaws.com", 
                        "public-ipv4s": "34.241.176.71", 
                        "security-group-ids": "sg-60c2a616", 
                        "security-groups": "default", 
                        "subnet-id": "subnet-b537b9ef", 
                        "subnet-ipv4-cidr-block": "172.31.32.0/20", 
                        "vpc-id": "vpc-d59d8eb3", 
                        "vpc-ipv4-cidr-block": "172.31.0.0/16", 
                        "vpc-ipv4-cidr-blocks": "172.31.0.0/16"
                    }
                }
            }
        }, 
        "placement": {
            "availability-zone": "eu-west-1b", 
            "availability-zone-id": "euw1-az3", 
            "region": "eu-west-1"
        }, 
        "profile": "default-hvm", 
        "public-hostname": "ec2-34-241-176-71.eu-west-1.compute.amazonaws.com", 
        "public-ipv4": "34.241.176.71", 
        "public-keys": {
            "0=terraform_keypair": null
        }, 
        "reservation-id": "r-038c774ff30715538", 
        "security-groups": "default", 
        "services": {
            "domain": "amazonaws.com", 
            "partition": "aws"
        }
    }
}

