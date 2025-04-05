CC = g++
CFLAGS = -std=c++17 -Wall -Wextra
LDFLAGS = -ludev

SRC_DIR = src/cpp
BIN_DIR = bin
PYTHON_DIR = src/python

.PHONY: all clean build run

all: build

build:
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $(BIN_DIR)/usb_listener $(SRC_DIR)/usb_listener.cpp $(LDFLAGS)

clean:
	rm -rf $(BIN_DIR)

run: build
	sudo $(BIN_DIR)/usb_listener

install-deps:
	sudo apt-get update
	sudo apt-get install -y libudev-dev clamav yara python3-pip
	pip3 install yara-python

test:
	python3 -m pytest tests/ 