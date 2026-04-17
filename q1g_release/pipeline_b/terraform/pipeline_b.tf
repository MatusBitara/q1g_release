terraform {
  required_version = ">= 1.5"
}

variable "pipeline_b_tag" {
  type        = string
  description = "Release or image tag for pipeline B (example)."
}

locals {
  pipeline_b_name = "pipeline-b"
}

output "pipeline_b_ref" {
  description = "Example composite identifier."
  value       = "${local.pipeline_b_name}:${var.pipeline_b_tag}"
}
