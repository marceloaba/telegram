# Telegram Bot API

This is a Python-based REST API that enables sending messages through a Telegram bot. The application is built using Flask and communicates with the Telegram Bot API.

## Features

- Accepts POST requests to send messages.
- Logs information, warnings, and errors for better monitoring and debugging.
- Environment variable-based configuration for secure credentials management.

## Requirements

- Python 3.7+
- Flask
- Requests

## Setup

### 1. Clone the Repository

```bash
# Replace <repository_url> with the actual repository URL.
git git@github.com:marceloaba/telegram.git
cd telegram
```

### 2. Build and push app to docker hub

#### Build and push app to docker hub
```bash
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t marceloaba/uppababy-price-tracking:tagname --push .
```

### 2. Run app using docker compose

### Set Environment Variables

Create and set the following environment variables:

```bash
export TELEGRAM_TOKEN="your_telegram_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
```

#### Start the Container
```bash
docker-compose up -d
```

The API will start and listen on `http://localhost:5001`.

## API Endpoint

### `POST /send_message`

#### Request:

- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
      "message": "Your message text"
  }
  ```

#### Response:

- **Success (200):**
  ```json
  {
      "success": "Message sent successfully."
  }
  ```
- **Error (400/500):**
  ```json
  {
      "error": "Description of the error.",
      "details": "Additional details about the error."
  }
  ```

## Testing the API

### Using `curl`

```bash
curl -X POST http://localhost:5001/send_message \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, this is a test message!"}'
```

## Notes

- Ensure your Telegram bot token and chat ID are kept secure.
- You can run the application on a different host or port by modifying the `app.run` line in the script.