#!/bin/sh -l

container_name=$(docker ps -a | awk '{print $NF}' | grep -e "web" | cat)
echo "::set-output name=container_name::$container_name"