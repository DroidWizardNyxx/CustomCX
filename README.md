# Google Search API with Flask and Render

This project is a simple and robust API, built with Python (Flask), that acts as a proxy for the **Google Custom Search JSON API**.

The main goal is to provide a secure and easy-to-use endpoint for performing web searches without exposing your Google API keys on the client-side (frontend), while also handling CORS (Cross-Origin Resource Sharing) policies.

It's ideal for small projects, prototypes, or any application that needs search functionality without initial costs, using the free tier of [Render](https://render.com/).

## ✨ Features

-   **Secure Endpoint:** Keeps your Google API key safe on the backend.
-   **Ready to Deploy:** Configured for a quick and easy deployment on the Render platform.
-   **CORS Enabled:** Allows the API to be called from any domain (great for frontends built with React, Vue, Angular, etc.).
-   **Simple Configuration:** Uses environment variables for credentials.
-   **Lightweight and Fast:** Based on Flask, a Python micro-framework.

## 🚀 How It Works

The application flow is straightforward:

`Your Frontend (JavaScript) ➡️ Your API on Render ➡️ Google's API`

1.  Your frontend application makes a call to the `/search` endpoint on your API hosted on Render.
2.  Your Flask API receives the request, adds your secret Google API key, and forwards the search to the Google Custom Search API.
3.  The Google API returns the results to your API on Render.
4.  Your API on Render sends the results back to your frontend application in JSON format.

## 📋 Prerequisites

Before you begin, you will need two credentials from Google.

1.  **Google API Key**
    -   Go to the [Google Cloud Console](https://console.cloud.google.com/).
    -   Create a new project (or use an existing one).
    -   Navigate to **"APIs & Services" > "Library"**, search for **"Custom Search API"**, and enable it.
    -   Navigate to **"APIs & Services" > "Credentials"**, click **"+ CREATE CREDENTIALS"**, and select **"API key"**.
    -   Copy and save this key.

2.  **Search Engine ID (CX)**
    -   Go to the [Programmable Search Engine control panel](https://programmablesearchengine.google.com/controlpanel/all).
    -   Create a new search engine.
    -   **Important:** Enable the **"Search the entire web"** option.
    -   After creation, copy the **"Search engine ID"**.

## ⚙️ Installation and Deployment on Render

This project is ready to be deployed with just a few clicks on Render.

1.  **Fork/Clone this Repository**
    -   Fork this repository to your own GitHub account.

2.  **Create a Render Account**
    -   Go to [Render.com](https://render.com/) and sign up for a free account.

3.  **Create a New "Web Service"**
    -   On your Render dashboard, click **"New +" ➡️ "Web Service"**.
    -   Connect your GitHub account and select the repository you just forked.
    -   Render will analyze the project. Fill in the settings:
        -   **Name:** Give it a unique name (e.g., `my-google-api`).
        -   **Runtime:** `Python 3`
        -   **Build Command:** `pip install -r requirements.txt` (usually auto-detected).
        -   **Start Command:** `gunicorn app:app`
        -   **Plan:** Select `Free`.

4.  **Set up Environment Variables**
    -   Navigate to the **"Environment"** section before finalizing the creation.
    -   Add the two credentials you obtained in the prerequisites:
        -   **Key:** `GOOGLE_API_KEY`, **Value:** `YOUR_API_KEY_HERE`
        -   **Key:** `SEARCH_ENGINE_ID`, **Value:** `YOUR_CX_ID_HERE`

5.  **Click "Create Web Service"**
    -   Wait a few minutes while Render builds and deploys your application. Once finished, you will be given a public URL for your API.

## ⚡ How to Use the API

Your API will have a single main endpoint.

### `GET /search`

Performs a web search.

-   **Query Parameters:**
    -   `q` (required): The term you want to search for.

-   **Example Request (using `fetch` in JavaScript):**

```javascript
const query = 'hatsune miku';
const apiUrl = `https://your-service-name.onrender.com/search?q=${encodeURIComponent(query)}`;

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log(data.items); // Array containing the search results
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
