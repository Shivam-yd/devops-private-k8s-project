terraform {
  required_version = ">= 1.6.0"

  backend "s3" {
    bucket       = "devops-private-k8s-tfstate-845430216465"
    key          = "devops-private-k8s-project/terraform.tfstate"
    region       = "us-east-1"
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
  region = "us-east-1"
}

resource "aws_ecr_repository" "devops_app" {
  name                 = "devops-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }

  tags = {
    Project     = "devops-private-k8s-project"
    Environment = "shared"
    ManagedBy   = "Terraform"
  }
}

resource "aws_ecr_lifecycle_policy" "devops_app" {
  repository = aws_ecr_repository.devops_app.name

  policy = jsonencode({
    rules = [
      {
        rulePriority = 1
        description  = "Keep last 20 images"

        selection = {
          tagStatus   = "any"
          countType   = "imageCountMoreThan"
          countNumber = 20
        }

        action = {
          type = "expire"
        }
      }
    ]
  })
}
