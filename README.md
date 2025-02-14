# CINEMA-API

Unleashing Movie Magic with Seamless Data Management

[![License](https://img.shields.io/github/license/brunopascoal/cinema-api?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/brunopascoal/cinema-api?style=default&logo=git&logoColor=white&color=0080ff)](https://github.com/brunopascoal/cinema-api/commits)
[![Top Language](https://img.shields.io/github/languages/top/brunopascoal/cinema-api?style=default&color=0080ff)](https://github.com/brunopascoal/cinema-api/search?l=python)
[![Languages Count](https://img.shields.io/github/languages/count/brunopascoal/cinema-api?style=default&color=0080ff)](https://github.com/brunopascoal/cinema-api)

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
   - [Project Index](#project-index)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Usage](#usage)  
   - [Testing](#testing)  
5. [Endpoints](#endpoints)  
   - [Genres](#genres)  
   - [Actors](#actors)  
   - [Movies](#movies)  
   - [Reviews](#reviews)  
   - [Example Using `curl`](#example-using-curl)  
<!-- 6. [Project Roadmap](#project-roadmap)   -->
6. [Contributing](#contributing)  
7. [License](#license)  
<!-- 9. [Acknowledgments](#acknowledgments)   -->

---

## Overview

**cinema-api** is a Django REST Framework application designed to manage a digital cinema platform. It includes robust features to handle movies, actors, genres, and user reviews. The goal is to deliver a reliable tool for:

- Movie database websites  
- Cinema management systems  
- General entertainment industry solutions  

With a modular design, **cinema-api** is easy to maintain, extend, and integrate into larger platforms.

---

## Features

|     | **Feature**        | **Summary**                                                                                                                                                                 |
|:---:|:-------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**    | - Built with Django, a high-level Python framework.<br>- Organized into Django apps (`movies`, `actors`, `genres`, `reviews`).                                            |
| 🔩 | **Code Quality**    | - Follows PEP 8 styling.<br>- Each app has dedicated `models.py`, `views.py`, `urls.py`, etc.<br>- Test files (`tests.py`) are set for easy coverage expansion.             |
| 📄 | **Documentation**   | - This README covers setup, usage, and API endpoints.<br>- Inline code comments.<br>- `requirements.txt` for dependencies.                                                 |
| 🔌 | **Integrations**    | - Uses Django’s SQLite DB by default.<br>- Leverages Django REST Framework for API building.<br>- JWT auth with `PyJWT` and `djangorestframework-simplejwt`.                |
| 🧩 | **Modularity**      | - Separate apps for movies, actors, genres, reviews.<br>- Easy to swap or add new apps.                                                                                     |
| 🧪 | **Testing**         | - Test placeholders in each app.<br>- Integrates with `pytest` or Django’s `TestCase`.                                                                                       |
| ⚡️  | **Performance**    | - SQLite is suitable for small to medium-sized apps.<br>- Easily switch to PostgreSQL or another RDBMS for scalability.<br>- Django ORM abstracts efficient DB operations. |

---

## Project Structure

```bash
cinema-api/
├── README.md
├── actors/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── genres/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── movies/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── reviews/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

### Project Index

<details open>
 <summary><b><code>CINEMA-API/</code></b></summary>
 <details> <!-- __root__ Submodule -->
  <summary><b>__root__</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/manage.py'>manage.py</a></b></td>
    <td>- Manage.py serves as the command-line utility for administrative tasks in the Django project<br>- It sets the default settings module, checks for Django's availability in the environment, and executes command-line arguments<br>- This file is crucial for running administrative tasks and managing the Django application.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/db.sqlite3'>db.sqlite3</a></b></td>
    <td>- I'm sorry, but you haven't provided any code file or additional data about the project<br>- Could you please provide the necessary information so I can generate a summary for you?</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/requirements.txt'>requirements.txt</a></b></td>
    <td>- Requirements.txt outlines the necessary dependencies for the project, specifying versions for Django, Django REST framework, and other related libraries<br>- It ensures consistent environment setup across different development stages, contributing to the stability and reliability of the entire codebase.</td>
   </tr>
   </table>
  </blockquote>
 </details>
 <details> <!-- core Submodule -->
  <summary><b>core</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/core/settings.py'>settings.py</a></b></td>
    <td>- The core/settings.py file in the Django project serves as the central configuration hub<br>- It defines the project's security measures, installed applications, middleware, database setup, and other settings<br>- It also includes settings for internationalization and static files, contributing to the overall functionality and behavior of the project.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/core/urls.py'>urls.py</a></b></td>
    <td>- Core/urls.py serves as the central routing hub for the Django project, directing incoming requests to their respective application handlers<br>- It includes routes for the admin interface and API endpoints for genres, actors, movies, and reviews, ensuring efficient navigation and data retrieval within the application.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/core/asgi.py'>asgi.py</a></b></td>
    <td>- The core/asgi.py serves as the ASGI configuration for the core project<br>- It establishes the ASGI application as a module-level variable named 'application', setting the stage for asynchronous server gateway interface operations<br>- This configuration is crucial for deployment, as detailed in Django's official documentation.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/core/wsgi.py'>wsgi.py</a></b></td>
    <td>- The 'core/wsgi.py' serves as the Web Server Gateway Interface (WSGI) configuration for the core project<br>- It establishes the WSGI application callable, which is crucial for deploying the Django application<br>- The file also sets the default Django settings module to 'core.settings', ensuring the correct settings are loaded during application startup.</td>
   </tr>
   </table>
  </blockquote>
 </details>
 <details> <!-- movies Submodule -->
  <summary><b>movies</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/tests.py'>tests.py</a></b></td>
    <td>- Movies/tests.py serves as the testing module for the 'movies' component of the Django project<br>- It's designed to contain unit tests that ensure the functionality and reliability of the 'movies' component, contributing to the overall stability and robustness of the codebase.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/views.py'>views.py</a></b></td>
    <td>- In the context of the entire codebase, movies/views.py facilitates the creation, retrieval, updating, and deletion of movie records in the database<br>- It leverages Django's REST framework and the MovieSerializer to interact with the Movie model, thereby managing the movie data effectively.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/apps.py'>apps.py</a></b></td>
    <td>- MoviesConfig, located in movies/apps.py, serves as a configuration hub for the 'movies' application within the Django project<br>- It sets the default auto field for the application's database models and establishes the application's name, ensuring seamless integration and operation within the broader codebase architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/urls.py'>urls.py</a></b></td>
    <td>- The 'movies/urls.py' file in the project structure defines the URL patterns for the movie-related functionalities<br>- It maps the endpoints to their respective views, enabling the creation, retrieval, update, and deletion of movie data<br>- This file plays a crucial role in the Django web framework's request-response cycle.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/serializers.py'>serializers.py</a></b></td>
    <td>- MovieSerializer in movies/serializers.py serves as a crucial link between the Movie model and its representation in the project<br>- It leverages Django's REST framework to serialize all fields of the Movie model, facilitating efficient data exchange and manipulation within the application.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/admin.py'>admin.py</a></b></td>
    <td>- MovieAdmin in movies/admin.py registers the Movie model with the Django admin interface, enabling the display of movie titles, genres, release dates, and resumes<br>- This functionality facilitates efficient management and manipulation of movie data within the project's backend.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/models.py'>models.py</a></b></td>
    <td>- 'Movies/models.py' defines the Movie model in the Django framework, establishing relationships with the Genre and Actors models<br>- It outlines key attributes such as title, genre, release date, actors, and resume<br>- This model serves as a crucial component in managing movie-related data throughout the application.</td>
   </tr>
   </table>
   <details>
    <summary><b>migrations</b></summary>
    <blockquote>
     <table>
     <tr>
      <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/movies/migrations/0001_initial.py'>0001_initial.py</a></b></td>
      <td>- The '0001_initial.py' in the 'movies' module establishes the initial database migration for the Movie model in the Django project<br>- It creates a new Movie model with fields for id, title, release date, resume, actors, and genre, setting up relationships with the 'actors' and 'genres' modules.</td>
     </tr>
     </table>
    </blockquote>
   </details>
  </blockquote>
 </details>
 <details> <!-- actors Submodule -->
  <summary><b>actors</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/tests.py'>tests.py</a></b></td>
    <td>- Actors/tests.py serves as the testing module for the 'actors' component of the Django project<br>- It utilizes Django's built-in TestCase class to create unit tests, ensuring the functionality and reliability of the 'actors' component within the overall codebase architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/views.py'>views.py</a></b></td>
    <td>- Actors/views.py enables the creation, retrieval, updating, and deletion of 'Actors' data in the Django application<br>- It leverages Django Rest Framework's generic views and serializers for efficient data manipulation<br>- This file plays a crucial role in managing the 'Actors' model within the project's architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/apps.py'>apps.py</a></b></td>
    <td>- ActorsConfig, located in the actors/apps.py, is a Django application configuration class<br>- It sets the default auto field for the 'actors' application to 'django.db.models.BigAutoField'<br>- This configuration is crucial for the overall project architecture as it determines the primary key field type for models in the 'actors' application.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/urls.py'>urls.py</a></b></td>
    <td>- Actors/urls.py establishes the URL routing for the Actor-related views in the Django application<br>- It maps the URLs for creating and listing actors, as well as retrieving, updating, and deleting specific actors<br>- This contributes to the overall codebase by defining the web interface for actor data management.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/serializers.py'>serializers.py</a></b></td>
    <td>- ActorsSerializer in actors/serializers.py serves as a bridge between the Actors model and its representation in JSON format<br>- It leverages Django's REST framework to serialize all fields of the Actors model, facilitating data exchange in the application's architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/admin.py'>admin.py</a></b></td>
    <td>- ActorsAdmin in actors/admin.py registers the Actors model with the Django admin interface, enabling the display of Actor instances<br>- It specifies the fields to be shown in the list view, namely id, name, birthday, and nationality<br>- This enhances the manageability of Actor data within the project's administrative interface.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/models.py'>models.py</a></b></td>
    <td>- Actors/models.py serves as a data model within the Django framework, defining the 'Actors' class<br>- It outlines the structure and attributes of an actor, including name, birthday, and nationality<br>- This model is integral to the project's database operations, enabling data storage and retrieval for actor-related functionalities.</td>
   </tr>
   </table>
   <details>
    <summary><b>migrations</b></summary>
    <blockquote>
     <table>
     <tr>
      <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/actors/migrations/0001_initial.py'>0001_initial.py</a></b></td>
      <td>- The initial migration script in the 'actors' module establishes the 'Actors' database model within the Django framework<br>- It defines the structure for storing actor-related data, including fields for ID, name, birthday, and nationality<br>- This forms a crucial part of the project's data layer, enabling data persistence and manipulation.</td>
     </tr>
     </table>
    </blockquote>
   </details>
  </blockquote>
 </details>
 <details> <!-- genres Submodule -->
  <summary><b>genres</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/tests.py'>tests.py</a></b></td>
    <td>- Genres/tests.py is responsible for housing test cases related to the 'genres' component of the project<br>- It leverages Django's testing framework to ensure the functionality and reliability of the 'genres' module, contributing to the overall stability and robustness of the codebase.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/views.py'>views.py</a></b></td>
    <td>- Genres/views.py enables the listing, creation, retrieval, updating, and deletion of genre data in the application<br>- It leverages Django's REST framework and the Genre model to manage genre-related operations, ensuring seamless interaction with the database<br>- This file is integral to the overall data management in the project's architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/apps.py'>apps.py</a></b></td>
    <td>- GenresConfig, located in genres/apps.py, serves as a configuration hub for the 'genres' application within the Django project<br>- It sets the default auto field and names the application, playing a crucial role in Django's app loading mechanism and overall project architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/urls.py'>urls.py</a></b></td>
    <td>- Genres/urls.py establishes the URL routing for the 'genres' component of the project<br>- It maps URLs to their corresponding views, enabling the creation, retrieval, update, and deletion of genre instances<br>- This file plays a crucial role in the Django web framework's request-response cycle, contributing to the overall functionality of the application.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/serializers.py'>serializers.py</a></b></td>
    <td>- GenreSerializer in genres/serializers.py serves as a conduit for transforming Genre model data into a format suitable for HTTP responses<br>- It leverages Django's REST framework and ModelSerializer to serialize all fields of the Genre model, facilitating efficient data exchange in the project's architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/admin.py'>admin.py</a></b></td>
    <td>- GenreAdmin in genres/admin.py registers the Genre model with the Django admin interface, enabling the display of genre instances<br>- It specifically configures the admin interface to show the 'id' and 'name' fields of each genre<br>- This contributes to the overall project by facilitating efficient management of genre data.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/models.py'>models.py</a></b></td>
    <td>- Genre models in the Django framework are defined in genres/models.py<br>- The model, Genre, contains a single field 'name' with a character limit of 200<br>- It represents different genres in the application, providing a string representation of each genre by its name.</td>
   </tr>
   </table>
   <details>
    <summary><b>migrations</b></summary>
    <blockquote>
     <table>
     <tr>
      <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/genres/migrations/0001_initial.py'>0001_initial.py</a></b></td>
      <td>- The '0001_initial.py' within the 'genres/migrations' directory initiates the creation of the 'Genre' model in the Django framework<br>- It establishes the 'Genre' model with an 'id' as the primary key and a 'name' field, setting the foundation for genre categorization in the project's database architecture.</td>
     </tr>
     </table>
    </blockquote>
   </details>
  </blockquote>
 </details>
 <details> <!-- reviews Submodule -->
  <summary><b>reviews</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/tests.py'>tests.py</a></b></td>
    <td>- Reviews/tests.py serves as a placeholder for unit tests within the Reviews module of the Django project<br>- It's designed to validate the functionality of the Reviews component, ensuring its reliability and correctness<br>- However, it currently doesn't contain any tests, indicating that this aspect of the project is yet to be developed.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/views.py'>views.py</a></b></td>
    <td>- ReviewListCreateApiView and ReviewRetrieveUpdateDestroyView, located in reviews/views.py, serve as the primary interfaces for handling review data<br>- They facilitate the listing, creation, retrieval, updating, and deletion of reviews, utilizing the ReviewsSerializer for data serialization<br>- These views form a crucial part of the project's RESTful API structure.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/apps.py'>apps.py</a></b></td>
    <td>- ReviewsConfig, located in reviews/apps.py, serves as a configuration hub for the 'reviews' application within the Django project<br>- It sets the default auto field for the application's database models and establishes the application's name, thereby integrating it into the overall codebase architecture.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/urls.py'>urls.py</a></b></td>
    <td>- The 'reviews/urls.py' file in the project structure defines the URL patterns for the review application<br>- It maps URLs to their corresponding views, enabling the creation, retrieval, update, and deletion of reviews<br>- This plays a crucial role in the overall codebase architecture by facilitating user interaction with review data.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/serializers.py'>serializers.py</a></b></td>
    <td>- ReviewsSerializer in reviews/serializers.py serves as a bridge between the Reviews model and its representation in JSON format<br>- It leverages Django's REST framework to serialize all fields of the Reviews model, facilitating data exchange in the project's API endpoints.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/admin.py'>admin.py</a></b></td>
    <td>- ReviewsAdmin in reviews/admin.py registers the Reviews model with the Django admin interface, enabling the display of review ratings and comments<br>- This integration facilitates the management of user reviews within the project's administrative framework.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/models.py'>models.py</a></b></td>
    <td>- Reviews/models.py establishes the Reviews model in the Django framework, linking it to the Movie model<br>- It validates user ratings and allows for optional comments<br>- This model plays a crucial role in collecting and managing user reviews for movies within the overall project.</td>
   </tr>
   </table>
   <details>
    <summary><b>migrations</b></summary>
    <blockquote>
     <table>
     <tr>
      <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/migrations/0001_initial.py'>0001_initial.py</a></b></td>
      <td>- The code file in question establishes the initial database migration for the 'Reviews' model in a Django-based project<br>- It creates a new model with fields for id, rate, comment, and movie, setting up relationships and validations<br>- This migration is a foundational part of the project's data layer, linking reviews to movies.</td>
     </tr>
     <tr>
      <td><b><a href='https://github.com/brunopascoal/cinema-api/blob/master/reviews/migrations/0002_alter_reviews_rate.py'>0002_alter_reviews_rate.py</a></b></td>
      <td>- The code in 'reviews/migrations/0002_alter_reviews_rate.py' modifies the 'rate' field in the 'reviews' model<br>- It introduces validators to ensure the rating value is within the range of 0 to 5<br>- This change is part of the project's data validation strategy, enhancing the integrity of user-generated reviews.</td>
     </tr>
     </table>
    </blockquote>
   </details>
  </blockquote>
 </details>
</details>

---

## Getting Started

### Prerequisites

Before getting started with cinema-api, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Install cinema-api using one of the following methods:

**Build from source:**

1. Clone the cinema-api repository:

```sh
❯ git clone https://github.com/brunopascoal/cinema-api
```

2. Navigate to the project directory:

```sh
❯ cd cinema-api
```

3. Install the project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

### Usage

Run cinema-api using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```

### Testing

Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

## Endpoints

Below are some of the primary endpoints you can use to interact with **cinema-api**.  
All endpoints typically follow the pattern: `/api/v1/<resource>/`

---

### Genres

| Method   | Endpoint               | Description                                | Request Body                                     | Response Example                                                                                 |
|:--------:|:-----------------------|:-------------------------------------------|:-------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| **GET**  | `/api/v1/genres/`     | Retrieves a list of all genres            | –                                               | `[ { "id": 1, "name": "Comedy" }, { "id": 2, "name": "Action" } ]`                                |
| **POST** | `/api/v1/genres/`     | Creates a new genre                       | `{ "name": "Romance" }`                         | `{ "id": 3, "name": "Romance" }`                                                                 |
| **GET**  | `/api/v1/genres/:id/` | Retrieves a specific genre by **id**      | –                                               | `{ "id": 1, "name": "Comedy" }`                                                                  |
| **PUT**  | `/api/v1/genres/:id/` | Updates an existing genre                 | `{ "name": "Thriller" }`                        | `{ "id": 1, "name": "Thriller" }`                                                                |
| **DELETE** | `/api/v1/genres/:id/` | Deletes an existing genre                | –                                               | **Status:** `204 No Content`                                                                     |

---

### Actors

| Method   | Endpoint               | Description                                | Request Body                                                            | Response Example                                                                                         |
|:--------:|:-----------------------|:-------------------------------------------|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| **GET**  | `/api/v1/actors/`     | Retrieves a list of all actors            | –                                                                      | `[ { "id": 1, "name": "Robert De Niro", "birthday": "1943-08-17", "nationality": "American" } ]`         |
| **POST** | `/api/v1/actors/`     | Creates a new actor                       | `{ "name": "Scarlett Johansson", "birthday": "1984-11-22", "nationality": "American" }` | `{ "id": 3, "name": "Scarlett Johansson", "birthday": "1984-11-22", "nationality": "American" }`         |
| **GET**  | `/api/v1/actors/:id/` | Retrieves a specific actor by **id**      | –                                                                      | `{ "id": 2, "name": "Denzel Washington", "birthday": "1954-12-28", "nationality": "American" }`          |
| **PUT**  | `/api/v1/actors/:id/` | Updates an existing actor                 | `{ "name": "Tom Hanks", "birthday": "1956-07-09", "nationality": "American" }` | `{ "id": 2, "name": "Tom Hanks", "birthday": "1956-07-09", "nationality": "American" }`                  |
| **DELETE** | `/api/v1/actors/:id/` | Deletes an existing actor                | –                                                                      | **Status:** `204 No Content`                                                                             |

---

### Movies

| Method   | Endpoint               | Description                                      | Request Body                                                                                                        | Response Example                                                                                                                                  |
|:--------:|:-----------------------|:-------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| **GET**  | `/api/v1/movies/`     | Retrieves a list of all movies                  | –                                                                                                                  | `[ { "id": 1, "title": "Inception", "release_date": "2010-07-16", "resume": "...", "actors": [...], "genre": 1 } ]`                               |
| **POST** | `/api/v1/movies/`     | Creates a new movie                             | `{ "title": "Joker", "release_date": "2019-10-04", "resume": "Psychological thriller...", "actors": [1, 3], "genre": 1 }` | `{ "id": 2, "title": "Joker", "release_date": "2019-10-04", "resume": "Psychological thriller...", "actors": [1, 3], "genre": 1 }`               |
| **GET**  | `/api/v1/movies/:id/` | Retrieves a specific movie by **id**            | –                                                                                                                  | `{ "id": 2, "title": "Joker", "release_date": "2019-10-04", "resume": "Psychological thriller...", "actors": [1, 3], "genre": 1 }`                |
| **PUT**  | `/api/v1/movies/:id/` | Updates an existing movie                       | `{ "title": "The Matrix", "release_date": "1999-03-31", "resume": "...", "actors": [2], "genre": 2 }`               | `{ "id": 2, "title": "The Matrix", "release_date": "1999-03-31", "resume": "...", "actors": [2], "genre": 2 }`                                     |
| **DELETE** | `/api/v1/movies/:id/` | Deletes an existing movie                      | –                                                                                                                  | **Status:** `204 No Content`                                                                                                                      |

---

### Reviews

| Method   | Endpoint                | Description                                          | Request Body                                                       | Response Example                                                                                       |
|:--------:|:------------------------|:-----------------------------------------------------|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| **GET**  | `/api/v1/reviews/`     | Retrieves a list of all reviews                     | –                                                                 | `[ { "id": 1, "rate": 5, "comment": "Fantastic movie!", "movie": 2 } ]`                                |
| **POST** | `/api/v1/reviews/`     | Creates a new review                                | `{ "rate": 4, "comment": "Very good", "movie": 2 }`              | `{ "id": 2, "rate": 4, "comment": "Very good", "movie": 2 }`                                           |
| **GET**  | `/api/v1/reviews/:id/` | Retrieves a specific review by **id**               | –                                                                 | `{ "id": 2, "rate": 4, "comment": "Very good", "movie": 2 }`                                           |
| **PUT**  | `/api/v1/reviews/:id/` | Updates an existing review                          | `{ "rate": 3, "comment": "It was alright", "movie": 2 }`          | `{ "id": 2, "rate": 3, "comment": "It was alright", "movie": 2 }`                                      |
| **DELETE** | `/api/v1/reviews/:id/` | Deletes an existing review                         | –                                                                 | **Status:** `204 No Content`                                                                            |

---

#### Example Using `curl`

```bash
curl -X GET \
  http://127.0.0.1:8000/api/v1/movies/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR_TOKEN_HERE>"
```

## Contributing

- **💬 [Join the Discussions](https://github.com/brunopascoal/cinema-api/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/brunopascoal/cinema-api/issues)**: Submit bugs found or log feature requests for the `cinema-api` project.
- **💡 [Submit Pull Requests](https://github.com/brunopascoal/cinema-api/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.

   ```sh
   git clone https://github.com/brunopascoal/cinema-api
   ```

3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.

   ```sh
   git checkout -b new-feature-x
   ```

4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.

   ```sh
   git commit -m 'Implemented new feature x.'
   ```

6. **Push to github**: Push the changes to your forked repository.

   ```sh
   git push origin new-feature-x
   ```

7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!

</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/brunopascoal/cinema-api/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=brunopascoal/cinema-api">
   </a>
</p>
</details>

---

## License

This project is protected under the [GNU](<https://www.gnu.org/licenses/gpl-3.0.html>) License. For more details, refer to the [LICENSE](https://github.com/brunopascoal/cinema-api/blob/main/LICENSE) file.

---
