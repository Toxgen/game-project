#!/bin/bash
Xvfb :99 -screen 1 1024x768x16 &
export DISPLAY=:99
exec "$@"
