#!/bin/bash

export(){
  token="$(gettoken "afnanahmed7874@gmail.com" "Nanfa1614@#$" "wise")"
  curl -L --silent --header "Authorization: GoogleLogin auth=$token" "http://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=$1&exportFormat=$2&gid=$0"
  echo ""
}

export 1ACz6hoBqhm0AI5IUbzsDw3IwGXCiwB2e-0gQF1BEKjo csv