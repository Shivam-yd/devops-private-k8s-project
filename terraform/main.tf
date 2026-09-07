terraform {
  required_version = ">= 1.6.0"

  backend "s3" {
    bucket       = "devops-private-k8s-tfstate-20260907-001"
    key          = "devops-private-k8s-project/terraform.tfstate"
    region       = "ap-south-1"
    use_lockfile = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

