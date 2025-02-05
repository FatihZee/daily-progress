# Auto Quote Updater

This repository automatically updates a quote three times a day. The quotes are fetched from an external API and stored in a `progress.txt` file. The repository uses GitHub Actions to auto-commit changes.

## Features
- Fetches new quotes three times daily.
- Automatically updates `progress.txt` with the new quote.
- GitHub Actions auto-commits the changes to the repository.

## Setup
1. Clone the repository to your local machine:
   git clone https://github.com/FatihZee/daily-progress.git

2. Set up the necessary API to fetch quotes and configure it in the repository.

3. GitHub Actions will handle the auto-update and commit process.

## Usage
- The `progress.txt` file will contain the updated quote after each automatic update.
- No manual intervention is required for quote updates; everything is handled by GitHub Actions.

## License
This project is licensed under the MIT License.
