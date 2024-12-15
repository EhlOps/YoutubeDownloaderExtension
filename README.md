# Youtube Downloader Extension

### How To Use

1. You must have Docker installed
2. You must be using Google Chrome as your browser

To use this extension, first go to [chrome://extensions](chrome://extensions) to check your extensions. Then click **"Load Unpacked"**, and navigate to the repository folder. Select the folder titled **"Extension"**. Now, you should be able to see the extension in Google Chrome. Please make sure that the extension is turned on.

To start the download server, ensure that the Docker daemon is running. Execute `quickstart.sh`, or create an `.env` file that looks like the following:

```
DOWNLOAD_PATH=/path/to/your/downloads/destination
```

You can then try running the server by running `docker compose up -d --build`.

Good luck downloading!
