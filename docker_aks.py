
def decorator_method1():
    first_variable  = 1
    return first_variable

@decorator_method1
def method2():
    return decorator_method1.first_variable
    
    
.DockerFile
-- name: Docker1
    @image linux:alpine

--name: Docker2
    @image: posgtresql
    
docker run -it -d -p 8000:8000 -p 2022:22 aiopsdashboard python3 manage.py runserver 0.0.0.0:8000
# kubectl container_name= Docker1, max_memory_

#Cluster: resource group, Nodes: IP address 10.0.0.2, Pods: 10.0.0.124, 100 containers
#service / service pool - vnet + subnet
#Network configuration
#Replica set
#Rollout: 
#front end : reactjs /html