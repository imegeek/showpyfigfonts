<div align="center">
<h1>showpyfigfonts</h1>
<kbd>
<p style="font-size:13px">Preview</p>
<img width="200" alt="showpyfigfonts-preview" src="https://github.com/imegeek/showpyfigfonts/assets/63346676/50b74cd9-0d50-4e7d-a90b-737431c9d103">
</kbd>
</div>

## **📑 INDEX**

* [**⚙️ Installation**](#installation)
* [**✅ Setup**](#setup)
* [**❓ How to use?**](#how-to-use)

<a name="installation"></a>

## ⚙️ Installation

**1. Install Python & Git:**

* For Windows:

  ```shell
  winget install Python.Python.3.12
  winget install Git.Git
  ```
* For Linux:

  ```shell
  sudo apt-get update
  sudo apt-get install -y git python3
  ```
* For macOS:

  ```shell
  brew install python git
  ```
* For Termux:

  ```shell
  apt update
  apt install git python -y
  ```

<a name="setup"></a>

## ✅ Setup

- ### Automatic Setup

```shell
pip install showpyfigfonts
```

- ### Manual Setup

**1. Download repository:**

```shell
  git clone https://github.com/imegeek/showpyfigfonts
```

**2. Change Directory:**

```shell
  cd showpyfigfonts
```

**3. Run setup.py:**

- ##### Linux/macOS/Termux:

```shell
python3 setup.py install
```

- ##### Windows:

```shell
python setup.py install
```

<a name="how-to-use"></a>

## ❓ How to use?

- Run this command:

```shell
showpyfigfonts
```

- ### Command Line Help:

```shell
usage: showpyfigfonts [-h] [--font name] [text]

positional arguments:
  text                  Render fonts by text.

options:
  -h, --help            show this help message and exit
  --font name, -f name  Render specific font by name.
```

- ### Command Line Usage:
- Show help menu:

```shell
showpyfigfonts --help
```

- Print custom text for all fonts:

```shell
showpyfigfonts 'hello'
```

- Print specific font:

```shell
showpyfigfonts -f mono12
```

- Print custom text with specific font:

```shell
showpyfigfonts -f mono12 'hello'
```
