#! /bin/sh

pdm build
pdm export --no-extras --prod -o requirements.txt
sudo docker compose up --build --remove-orphans -d
sudo docker compose logs -f
