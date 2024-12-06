#!/bin/bash

if ! [ -f ./Python-3.12.8.tgz ]; then
	echo wget https://www.python.org/ftp/python/3.12.8/Python-3.12.8.tgz
	wget https://www.python.org/ftp/python/3.12.8/Python-3.12.8.tgz
fi

if ! [ -d Python-3.12.8 ]; then
	echo tar xf Python-3.12.8.tgz
	tar xf Python-3.12.8.tgz
fi

sudo apt -y install build-essential zlib1g-dev libncurses5-dev libdb-dev libgdbm-compat-dev libdb5.3-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev liblzma-dev tk-dev uuid-dev

cd Python-3.12.8

if ! [ -f Makefile ]; then
	./configure --prefix=/home/oy753c/code-editor-flask
fi

if ! [ -x ./python ]; then
	make -j 7
fi

if ! [ -x bin/python3 ]; then
	make install
fi
