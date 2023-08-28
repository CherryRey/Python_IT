#!/bin/bash

if grep "127.0.0.1"/etc/hosts; then
        echo "Everything is fine"
else
        echo "Error!  127.0.0.1 isn't here"
fi


