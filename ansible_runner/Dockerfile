FROM python:3.10
RUN apt-get update && apt-get install -y --no-install-recommends \
  sshpass git python3-pip && \
  pip install ansible boto3 && \
  apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /workspace
CMD [ "sleep", "infinity" ]
# Storing this image in ECR in the aws ecr create-repository --repository-name ansible-runner
# command will create the repository in ECR