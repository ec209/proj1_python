#!/bin/sh

cd $(cd "$(dirname "$0")" && pwd)

. venv/bin/activate

export FLASK_APP=hello
export FLASK_ENV=development
flask run --host 0.0.0.0

