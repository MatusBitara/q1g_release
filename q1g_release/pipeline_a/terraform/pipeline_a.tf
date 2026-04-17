terraform {
  required_version = ">= 1.5"
}

variable "pipeline_a_tag" {
  type        = string
  description = "Release or image tag for pipeline A (example)."
}

locals {
  pipeline_a_name = "pipeline-a"
}

output "pipeline_a_ref" {
  description = "Example composite identifier."
  value       = "${local.pipeline_a_name}:${var.pipeline_a_tag}"
}
