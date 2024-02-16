# Flask Job Scraper

This Python project is a Flask application designed to scrape job listings from Head Hunter and aggregate the required skills for a given job keyword. It helps users understand the most demanded skills for a specific vacancy.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the latest version of Python installed on your system. This application was developed with Python 3.x in mind.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/madmanRE/py_flask/
```

2. Navigate to the project directory:

```bash
cd py_flask
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

To start the application, run the following command in the root of the project directory:

```bash
python main.py
```

After running the command, the Flask application will start, and you can access it via your web browser.

## Application Overview

This Flask application takes a keyword for a job title and performs the following actions:

- Queries the Head Hunter website for job listings related to the keyword.
- Collects information on each job listing, focusing on the required skills.
- Aggregates the data to determine the skills most in demand for that particular job title.

The result is a concise report of the most sought-after skills for the job you're interested in, aiding in your job search or skill development.
