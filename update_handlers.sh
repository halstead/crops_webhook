#!/bin/sh
cd /etc/crops-webhook/handlers
git pull > $1/response
