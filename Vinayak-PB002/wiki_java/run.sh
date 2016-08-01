#!/bin/bash
javac -cp org.json.jar Wiki.java
if [ $# -eq 2 ]; then
	java -cp .:org.json.jar Wiki $1 $2
else
	java -cp .:org.json.jar Wiki
fi