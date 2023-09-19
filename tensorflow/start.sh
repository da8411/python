#!/bin/sh

proj_path="$(cd "$(dirname "$0")" && pwd)"

d_network="tf-dajinbabo-net"

docker network create "${d_network}"

container_name="dajinbabo"

image_name="tensorflow/tensorflow" # Need to change!

docker run \
  --rm \
  -d \
  --name "${container_name}" \
  --network "${d_network}" \
  -v "/""${proj_path}":/home/"${container_name}" \
  -w //home/"${container_name}" \
  -u "$(id -u)":"$(id -g)" \
  -e HOME=//home/"${container_name}"/remote-config \
  "${image_name}" \
  sleep infinity