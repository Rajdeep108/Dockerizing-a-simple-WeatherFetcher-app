# London Weather Scraper

## Overview
This project is a Dockerized Python application that scrapes the current weather for London from BBC's website. Built using Flask for the web framework and BeautifulSoup for web scraping, it provides a simple yet effective way to display real-time weather information.

## Key Features
- **User-Friendly Interface**: Easily view the current weather conditions for London.
- **Dockerized**: The application is packaged in a Docker container for easy deployment and portability.

## How to Run the Application

### Prerequisites
Make sure you have Docker installed on your machine. If you haven't installed Docker yet, you can download it from [Docker's official website](https://www.docker.com/get-started).

### Steps to Run
1. **Pull the Docker Image**:
   ```bash
   docker pull rajdeep108/london_weather_scraper:2.0
2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 rajdeep108/london_weather_scraper:2.0
   ```
3. **Access the Application**:
   Open your web browser and navigate to
   ```bash
   http://localhost:5000
   ```
   to view the weather information.
