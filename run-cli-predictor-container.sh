#!/bin/sh
docker run --rm -v $(pwd)/$1:/app/input-file.csv wine-color-predictor-cli input-file.csv
