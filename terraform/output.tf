output "ecr_repository_url" {
  description = "ECR repository URL"
  value       = aws_ecr_repository.devops_app.repository_url
}

output "ecr_repository_name" {
  description = "ECR repository name"
  value       = aws_ecr_repository.devops_app.name
}

output "aws_region" {
  description = "AWS region"
  value       = "us-east-1"
}
