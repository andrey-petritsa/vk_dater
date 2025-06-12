#!/bin/bash

poetry run pytest -m "not integration" -q --tb=line -p no:warnings
