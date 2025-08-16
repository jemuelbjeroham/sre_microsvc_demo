FROM python:3.10-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
  sshpass git python3-pip && \
  pip install ansible boto3 && \
  apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /workspace
CMD ["bash"]