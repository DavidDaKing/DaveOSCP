#!/bin/bash

clear
echo "Welcome to linux.messenger "
		echo ""
users=$(cat /etc/passwd | grep home |  cut -d/ -f 3)
		echo ""
echo "$users"
		echo ""
read -p "Enter username to send message : " name 
		echo ""
read -p "Enter message for $name :" msg
		echo ""
echo "Sending message to $name "

$msg 2> /dev/null

		echo ""
echo "Message sent to $name :) "
		echo ""
