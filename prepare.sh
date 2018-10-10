#!/bin/bash

. /etc/os-release

if echo $ID | grep -iq "centos"; then
	yum install epel-release python-pip -y &>/dev/zero
	mkdir -p /data/flask_data               
	echo "done"
else
	echo "不想写太多系统版本的判断，请用centos的系统0.0"
fi


