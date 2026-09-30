# AI Customer Support Chatbot

An AI-powered web-based customer support chatbot developed using Python, Flask, JavaScript, SQLite and the Google Gemini API.

## Project Overview

This project provides an intelligent web-based customer support system that allows customers to communicate with an AI assistant.

The chatbot can answer frequently asked questions using a company knowledge base, maintain conversation history and create support tickets when human assistance is required.

The application uses the Google Gemini API to generate natural-language responses based on the company's knowledge base and previous conversation history.

## Features

* AI-powered customer support
* Google Gemini API integration
* FAQ and knowledge-base integration
* Natural-language conversations
* Conversation history
* Customer support ticket creation
* Human-agent escalation
* SQLite database
* Responsive web interface
* Secure API key management using environment variables
* Automatic database creation

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Artificial Intelligence

* Google Gemini API
* Generative AI
* Knowledge-base integration
* Conversation context

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Python Virtual Environment
* Git
* GitHub

## Project Structure

```text
AI-Customer-support-chatbot/
│
├── app.py
├── chatbot.py
├── database.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── data/
│   └── knowledge.txt
│
├── database/
│   └── chatbot.db
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

## Installation

### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd AI-Customer-support-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root directory.

Add your Google Gemini API key:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Never upload the `.env` file or your API key to GitHub.

The `.env` file is excluded using `.gitignore`.

## Running the Application

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Start the Flask application:

```powershell
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the address in a web browser.

## How the System Works

The chatbot follows this basic workflow:

```text
Customer
    ↓
Web Interface
    ↓
JavaScript
    ↓
Flask Backend
    ↓
Chatbot Module
    ↓
Knowledge Base + Conversation History
    ↓
Google Gemini API
    ↓
AI Generated Response
    ↓
Customer
```

When a customer requests human assistance, the application creates a support ticket and stores it in the SQLite database.

## Knowledge Base

The chatbot uses a company knowledge base stored in:

```text
data/knowledge.txt
```

The knowledge base contains information about:

* Company information
* Order information
* Order cancellation
* Returns
* Refunds
* Payment methods
* Payment problems
* Account support
* Customer support

The chatbot is instructed not to invent company policies, prices, order statuses, refund amounts or delivery dates.

## Database

The application uses SQLite to store customer-support information.

The database contains tables for:

* Conversations
* Messages
* Support tickets

The database file is automatically generated at:

```text
database/chatbot.db
```

The database file is excluded from GitHub using `.gitignore`.

## Human-Agent Escalation

If the customer requires human assistance, they can use the **Human Agent** option.

The application creates a support ticket containing:

* Ticket ID
* Customer session
* Issue description
* Ticket status
* Creation time

## Security

API credentials are stored in environment variables rather than directly inside the source code.

The following files should not be uploaded to GitHub:

```text
.env
database/chatbot.db
venv/
```

These files are excluded through `.gitignore`.

## Future Improvements

* Retrieval-Augmented Generation (RAG)
* PDF/document knowledge base
* User authentication
* Admin dashboard
* Real-time order tracking API
* Email notifications
* WhatsApp integration
* Voice-based customer support
* Customer analytics
* Cloud deployment

## Author

Adaya Patel

B.Tech Computer Science and Engineering
