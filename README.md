# Music Library

A Flask-based music library web application that allows users to register, browse songs and artists, and explore music rankings.

## Deployment

The application is deployed using Render.

Live Demo:

https://music-library-pkeb.onrender.com

---

## Project Overview

Music Library is a Flask-based web application designed for exploring songs, artists, and music rankings.

The project focuses on user authentication, database integration, page routing, and frontend presentation while demonstrating fundamental full-stack web development skills.

This project was originally developed as a university coursework project and has been enhanced as a personal portfolio project.

---

## Features

* User registration
* User login and logout
* Guest login
* Browse songs
* View song details
* Browse artists by region
* View artist details
* Music ranking page
* Responsive web interface
* Password hashing using Werkzeug

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Python
* Flask
* SQLAlchemy

### Database

* SQLite

### Deployment

* Render
* GitHub

---

## Installation

Clone the repository.

```bash
git clone https://github.com/WeiboMeng/music-library.git
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

macOS / Linux

```bash
source .venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python run.py
```

---

## Usage

After starting the application, open your browser and visit the local address displayed in the terminal.

You can:

* Register a new account
* Log in with an existing account
* Browse songs
* Browse artists
* View rankings
* Explore song and artist details

---

## Project Structure

```text
music-library
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
│
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

## Future Improvements

* Song search
* Filter songs by category
* Pagination
* User profile page
* Playlist management
* Better responsive design

---

## Screenshots

### Home Page

![Home Page](screenshots/Home%20page.png)

### Login Page

![Login Page](screenshots/Login%20page.png)

### Register Page

![Register Page](screenshots/Register%20page.png)

### Songs Page

![Songs Page](screenshots/Songs%20page.png)

### Artist Page

![Artist Page](screenshots/Artist%20page.png)

---

## License

This project is licensed under the MIT License.

---

## Author

**Weibo Meng**
