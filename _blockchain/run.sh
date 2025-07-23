#!/bin/sh
cd ethernaut
yarn network
yarn deploy:contracts
NODE_OPTIONS=--openssl-legacy-provider yarn start:ethernaut
