#!/usr/bin/env bash
podman machine stop
podman machine rm -f
podman machine init --cpus 4 --memory 6144 -v "$HOME:$HOME" --now