# Auto-InstaLing

Bot designed to automate interactions with the InstaLing platform.

## Prerequisites

To run the script, ensure you have the following installed:

- **Python:** Version 3.6 or higher.
- **Google Chrome:** Latest version recommended.
- **Git:** For cloning the repository.

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/Student-FastDev/Auto-InstaLing
    cd Auto-InstaLing
    ```

2. **Install Required Packages:**

    Install the necessary Python packages using `pip`:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Python Script:**

    Execute the main script to start the automation process:

    ```bash
    python main.py
    ```

2. **Configure Settings:**

    After running the program for the first time, a `settings.json` file will be generated. Open this file in a text editor to customize your settings:

    ```json
    {
        "entries": 3,
        "headless": false,
        "login": "example_login",
        "password": "example_password"
    }
    ```

    - **entries:** The number of entries to process in each run.
    - **headless:** Set to `true` to run the browser in headless mode.
    - **login:** Your InstaLing login username.
    - **password:** Your InstaLing login password.

## Notes

- **Data Learning:** The bot uses brute force to learn and generate translations, which are stored in `data.json`. Initial runs may contain inaccuracies as the bot learns new words.
- **Security:** The local version uses [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) to minimize detection. No security issues were identified during testing.
- **Browser Requirements:** Ensure that Google Chrome is installed and compatible with the version required by chromedriver.

---

<div align="center">  
    <img src="https://i.imgur.com/C41nvYs.png" alt="Instaling Logo" width="60px">
</div>
