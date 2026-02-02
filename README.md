# Telegram Space Images Bot

This project downloads space images from public APIs (NASA APOD, NASA EPIC, SpaceX) and publishes them to a Telegram channel.

The main goal of the project is to demonstrate working with REST APIs, file downloads, environment variables, and Telegram bot automation.

---

## Features

* Download images from **SpaceX launches**
* Download **NASA APOD** (Astronomy Picture of the Day) images in bulk
* Download **NASA EPIC** images of Earth
* Publish images to a Telegram channel
* Publish a specific image via command-line argument
* Automatically publish images from multiple directories in an infinite loop
* Shuffle images to avoid repeating the same order

---

## Project Structure

```text
.
├── common.py                 # Common helper functions (image downloading)
├── fetch_spacex_images.py    # Download SpaceX launch images
├── fetch_apod_images.py      # Download NASA APOD images
├── fetch_epic_images.py      # Download NASA EPIC images
├── telegram_bot.py           # Publish images to Telegram
├── NASA/
│   ├── apod/
│   └── epic/
├── Space X/
├── .env
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.8 or higher
* Telegram Bot Token
* NASA API Key

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration (Settings)

All configuration is done using **environment variables**.

Create a `.env` file in the project root directory:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
TG_CHAT_ID=your_telegram_channel_id
NASA_API_KEY=your_nasa_api_key
```

### Environment Variables Explained

* **TELEGRAM_TOKEN** – Telegram bot token obtained from @BotFather
* **TG_CHAT_ID** – ID of the Telegram channel where images will be published
* **NASA_API_KEY** – API key from [https://api.nasa.gov/](https://api.nasa.gov/)

---

## Downloading Images

### Download SpaceX Images

```bash
python fetch_spacex_images.py
```

Downloads images from the latest SpaceX launch (or a specific launch ID if implemented).

---

### Download NASA APOD Images

```bash
python fetch_apod_images.py
```

Downloads multiple APOD images in a single request.

---

### Download NASA EPIC Images

```bash
python fetch_epic_images.py
```

Downloads 5–10 EPIC images of Earth in PNG format.

---

## Publishing Images to Telegram

### Publish a Specific Image

Use the `--file` argument to publish a single image:

```bash
python telegram_bot.py --file NASA/apod/example.jpg
```

Only the specified image will be published.

---

### Automatic Publishing Mode

If no file is specified, the bot publishes images automatically:

```bash
python telegram_bot.py
```

Behavior:

* Images are taken from the following directories:

  * `NASA`
  * `NASA/epic`
  * `Space X`
* Images are shuffled before publishing
* One image is published every **4 hours**
* When all images are published, the list is shuffled and the cycle starts again

---

## Error Handling

* Network and API errors are handled using `raise_for_status()`
* Empty directories or missing files raise clear exceptions
* Temporary NASA API downtime is expected and should not crash the entire project

---

## Notes

* EPIC images are always downloaded in `.png` format
* Images are not reposted twice during a single cycle
* Publication delay can be moved to an environment variable if needed

---

## License

This project is created for educational purposes.
