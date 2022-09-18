# PhilipsHue

Toggle Lights On/Off in a Room

## Setup Virtual Env

`python -m venv venv`

`source venv/bin/activate`

## Install Project Requirements

`pip install -r requirements.txt`

## Setup App

`export FLASK_APP=hue`

## Start App

`flask run`

## Required ENV

HUE_API (endpoint of your Hue Bridge, ex: https://192.168.1.10/clip/v2/resource)
HUE_API_KEY (User key provided when you add your user to the Hue Bridge)
Provide these as -e arguments or in a file with --env-file in your docker run command.

## Philips Hue API Core Concepts

[Core Concepts](https://developers.meethue.com/develop/get-started-2/core-concepts/)
