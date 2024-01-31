# Technoxploit

<img width="477" alt="Screenshot 2024-02-01 at 12 19 44 AM" src="https://github.com/sasi123-sk/Technoxploit/assets/81082865/8513816b-5c21-45f7-b0f1-223cb32c6640">

A Python script to analyze server versions, search for exploits, and perform security checks on websites.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This tool is designed to perform security assessments on websites by analyzing server versions and searching for known exploits in the Exploit Database (exploitdb).

## Features

- Identify the server version of a website
- Search for exploits in the Exploit Database
- Support for analyzing a single URL or a list of URLs

## Prerequisites

- Python 3.x
- `colorama` library (`pip install colorama`)
- `searchsploit` command-line tool

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required `colorama` library:

    ```bash
    pip install colorama
    ```

3. Ensure that `searchsploit` is installed on your system.

## Usage
```
pip install technoxploit==0.1.0
```
```bash
python3 technoxploit.py -h

python3 technoxploit.py -u http://example.com
