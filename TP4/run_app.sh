#!/bin/bash

docker run -d \
	--name tp4-app \
	--network net-tp4 \
	--mount type=bind,source=$(pwd)/,target=/srv/ \
	-p 5000:5000 \
	im-tp4
