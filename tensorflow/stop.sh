#!/bin/sh

cd "$(cd "$(dirname "$0")" && pwd)"

container_name="dajinbabo"
d_network="tf-dajinbabo-net"

docker rm -f "${container_name}"
docker network rm "${d_network}"