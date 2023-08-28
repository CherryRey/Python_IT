#!/bin/bash
n=0
command=$1

while ! $command && [ $n -le 5 ]; do
  sleep $n
  ((n=n+1))
  echo "Intentar de nuevo desde bash #$n"
done;
