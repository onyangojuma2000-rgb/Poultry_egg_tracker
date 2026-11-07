# Kiambu Poultry Egg Production Tracker

A simple Flask web application for recording and monitoring daily egg production across multiple poultry sheds.

## Features

- Record daily egg production by shed.
- View all production records in a table.
- Automatically calculate total eggs produced.
- Track production totals per shed.
- Update records without refreshing the browser.
- Validate user input and display error messages.

## Technologies

Python · Flask · Flask-CORS · HTML · CSS · JavaScript · Fetch API

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   cd Egg_tracker
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000/` in your browser.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Open the tracker |
| POST | `/api/eggs` | Submit production records |
| GET | `/api/eggs` | Retrieve records and totals |

## Potential Customers in Kenya

- Small and medium-sized poultry farms.
- Commercial layer and Kienyeji egg producers.
- Egg collection and distribution businesses.
- Poultry cooperatives managing multiple sheds.

## Suggested Pricing

| Service | Price |
|---|---:|
| Basic setup and installation | KES 8,000–12,000 |
| Customized application | KES 15,000–25,000 |
| Monthly maintenance | KES 1,000–2,000 |

*Hosting and additional features can be quoted separately.*

## Current Limitation

Records are temporarily stored in memory and are lost when the application restarts. Database integration is recommended for permanent storage.

## Project Status

Version 2.0 – Browser interface with live production updates.