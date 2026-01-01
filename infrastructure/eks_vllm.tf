Infrastructure as Code for scaling open-source models (vLLM)

resource "aws_eks_node_group" "gpu_nodes" { cluster_name = var.cluster_name node_group_name = "ai-gpu-workers" node_role_arn = aws_iam_role.eks_node_role.arn subnet_ids = var.subnets

scaling_config { desired_size = 3 max_size = 10 min_size = 1 }

instance_types = ["p4d.24xlarge"] # A100 GPUs for production inference }