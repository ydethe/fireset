#! /bin/sh

pdm build
sudo docker compose up --build --remove-orphans -d
sudo docker compose logs -f
