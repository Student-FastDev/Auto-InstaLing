# Auto-InstaLing

InstaLing bot made with selenium.

Made for educational purposes!

## Table of Contents
- [Questions](#questions)
  - [How this works?](#how-this-works?)
  - [Is it safe?](#is-it-safe?)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Python File](#running-the-python-file)
- [Replit Integration](#replit-integration)


## Questions

### How this works?

Data will be learnt by bruteforce, data.json will be generated. There you can find all gathered translations ("your language":"foreign language").
You can see that bot makes mistakes at first few runs, thats because it is learning new words. Later it will be 100% accurate.

### Is it safe?

The local version is made with [undetected-chromedriver.](https://github.com/ultrafunkamsterdam/undetected-chromedriver) It is very safe and undetectable in 99% of cases.

The replit version, because of the limitations of replit, is a little less safe, although it is still very reliable. But it also have pros, free and good hosting for low demanding programs like this.

There were no security issues when I tested the program. (10/16/2023)

## Getting Started

This section will guide you through setting up and running the project locally.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python
- Git

### Installation

1. Clone this repository to your local machine using Git:

```plain
git clone https://github.com/Student-FastDev/Auto-InstaLing
```

2. Change to the project directory:

```plain
cd (path to Auto-InstaLing)
```

3. Install the required Python packages using pip and the requirements.txt file:

```plain
pip install -r requirements.txt
```

## Usage

### Running the Python File

To run the Python file, use the following command while being in the repository folder:

```bash
python main.py
```

Edit the settings, by opening the settings.json (will appear after running the program for the first time) in some text editor.

```plain
{
    "entries": 3, <- The amount of entries done in each program run.
    "headless": false, <- If true, the browser will be invisible.
    "login": "example_login", <- Here enter your InstaLing login.
    "password": "example_password" <- Here enter your InstaLing password.
}
```
## Replit Integration

[Replit can work 24/7, with delay]

You can also run this project on Replit. To do so, follow these steps:

1. [Click here to access the Replit project.](https://replit.com/@FAST-qq/Auto-InstaLing)

2. Fork the project.

3. In the Replit project settings, add the following secrets:

```plain
Key: LOGIN | Value: (YOUR LOGIN)
Key: PASSWORD | Value: (YOUR PASSWORD)
```

4. Change the settings in the settings.json (will appear after running the program for the first time).

```plain
{
    "entries": 3, <- The amount of entries done in each program run.
    "headless": false, <- If true, the browser will be invisible (not that important on the replit). 
    "delay": "86400" <- Delay between each program run. (in seconds)
}
```
