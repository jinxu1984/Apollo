variable "appId" {
  description = "Azure Kubernetes Service Cluster service principal"
}

variable "password" {
  description = "Azure Kubernetes Service Cluster password"
}

variable "environment" {
  description = "Azure Kubernetes Service Cluster environment"
}

variable "resource_group_name" {
   description = "Azure resource group name"
}

variable "resource_location" {
   description = "Apollo resource location"
}

variable "apollo_aks_name" {
  description = "Azure Kubernetes Service Cluster name"
}

variable "apollo_aks_dns_prefix" {
  description = "Azure Kubernetes Service Cluster dns prefix"
}

variable "apollo_aks_node_count" {
  description = "Azure Kubernetes Service Cluster node count"
}

variable "apollo_aks_vm_size" {
  description = "Azure Kubernetes Service Cluster vm size"
}

variable "apollo_aks_os_disk_size_gb" {
  description = "Azure Kubernetes Service Cluster OS disk size"
}