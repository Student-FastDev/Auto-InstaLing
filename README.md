# Auto-InstaLing

**Auto-InstaLing** is a Selenium-based bot designed to automate interactions with the InstaLing platform. It leverages undetected-chromedriver to ensure seamless operation without triggering security measures. The bot learns and adapts through brute force, generating translations and improving accuracy over time.

## Features

- **Automated Interactions:** Streamline tasks on the InstaLing platform using Selenium.
- **Learning Mechanism:** Continuously improves translation accuracy by learning from interactions.
- **Undetected Chromedriver:** Utilizes [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) to bypass detection.
- **Headless Mode:** Option to run the browser in headless mode for background operations.
- **Replit Integration:** Easily deploy and run the bot on Replit for cloud-based automation.

## Prerequisites

To run the Auto-InstaLing script, ensure you have the following installed:

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

## Replit Integration

You can also run this project on Replit. Follow these steps to set it up:

1. **Access the Replit Project:**

    [Click here to access the Replit project.](https://replit.com/@FAST-qq/Auto-InstaLing)

2. **Fork the Project:**

    Fork the repository to your own Replit account.

3. **Add Secrets:**

    In the Replit project settings, add the following secrets:

    ```plaintext
    Key: LOGIN | Value: (YOUR LOGIN)
    Key: PASSWORD | Value: (YOUR PASSWORD)
    ```

4. **Update Settings:**

    Modify the `settings.json` file to suit the Replit environment:

    ```json
    {
        "entries": 3,
        "headless": false,
        "delay": 86400
    }
    ```

    - **delay:** Time in seconds between each program run (e.g., 86400 seconds for 24 hours).

## Notes

- **Data Learning:** The bot uses brute force to learn and generate translations, which are stored in `data.json`. Initial runs may contain inaccuracies as the bot learns new words.
- **Security:** The local version uses [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) to minimize detection. No security issues were identified during testing.
- **Browser Requirements:** Ensure that Google Chrome is installed and compatible with the version required by undetected-chromedriver.

---

<div align="center">  
    <img src="https://www.zstjaslo.pl/wp-content/uploads/2022/10/instaling-logo-article.webp" alt="Instaling Logo" width="50px">
</div>
