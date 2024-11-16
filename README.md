# Youtube video and subtitle (caption) downloader telegram bot


This telegram bot download subtitles and vedio from YouTube videos.

## Installation

1. Clone the repository:
    ```bash
    https://github.com/leulgezahegn/Youtube-video-downloader.git
    cd 
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. Create .env file and write telegram bot TOKEN
    ```bash
    TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    ```
    
2. Run the Flask application:
    ```bash
    python app.py
    ```


## Project Structure
youtube-vedio-subtitle-downloder/\
│\
├── venv/                    # Virtual environment files\
│\
├── app.py                   # main app\
│\
├── .gitignore               # Git ignore files list\
│\
├── requirements.txt         # installition libs\
│\
└── README.md                # about this project\


## Dependencies

- requests: check vedio existens
- python-telegram-bot: for working telegram bot
- youtube-transcript-api: download subtitle from youtube
- pytube: download video and audio from youtube
- python-dotenv: for working environment

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
