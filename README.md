

# n8n-python

參考：
https://github.com/naskio/n8n-nodes-python
https://github.com/naskio/docker-n8n-python


## n8n-python Docker Image (Recommended)
This node is pre-installed in the n8n-python docker image .

Use n8n-python:latest-debian if you are planning to install heavy python packages such as numpy or pandas.
Use n8n-python:latest for a more lightweight image.
Example using docker-compose.yml

## Adding external packages
You can mount a requirements.txt file to the container to install additional packages.

You can use the ExecuteCommand node to run pip install -r requirements.txt and the n8nTrigger node to trigger it after each restart.


