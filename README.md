# LTBL - Empowering Communities

This Django project, **LTBL**, aims to serve the community by focusing on key areas: providing housing information for homeless individuals, supporting underdeveloped neighborhoods towards equality and justice, and training young youth to become social advocates. Additionally, the site includes a donation platform to enable community support.

## Features

* **Housing Information:** A section dedicated to listing available housing resources for homeless individuals, including details like address, capacity, availability, and contact information.
* **Social Advocate Profiles:** Profiles of trained young social advocates, highlighting their bios, training dates, and contact information. This section promotes connection and support for their work.
* **Donation Platform:** A dedicated page for individuals to make donations to support the organization's initiatives.
* **Focus on Equality and Justice:** The underlying goal of the project is to contribute to equality and justice within underdeveloped neighborhoods through its various services and programs.
* **Youth Empowerment:** By training young individuals as social advocates, the project invests in the future of community leadership and change.

## Getting Started

Follow these steps to set up the LTBL project on your local machine.

### Prerequisites

* **Python:** Make sure you have Python 3.x installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **pip:** Python package installer, which usually comes with Python.
* **Django:** You'll need to install Django.

### Installation

1.  **Clone the repository (if you have one):**

    ```bash
    git clone <repository_url>
    cd LTBL
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: You might not have a `requirements.txt` file yet if this is a new project. In that case, you can install Django directly: `pip install Django`)*

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an administrator account.

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Open your web browser and navigate to `http://127.0.0.1:8000/` to see the website. You can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

## Project Structure

