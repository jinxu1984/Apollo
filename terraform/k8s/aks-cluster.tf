provider "azurerm" {
  features {
  }
}

resource "azurerm_resource_group" "default" {
  name     = var.resource_group_name
  location = var.resource_location

  tags = {
    environment = var.environment
  }
}

resource "azurerm_kubernetes_cluster" "default" {
  name                = var.apollo_aks_name
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = var.apollo_aks_dns_prefix

  default_node_pool {
    name            = "default"
    node_count      = var.apollo_aks_node_count
    vm_size         = var.apollo_aks_vm_size
    os_disk_size_gb = var.apollo_aks_os_disk_size_gb
  }

  service_principal {
    client_id     = var.appId
    client_secret = var.password
  }

  role_based_access_control {
    enabled = true
  }

  tags = {
    environment = var.environment
  }
}
