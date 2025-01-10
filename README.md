# BE-Capstone-Project

# Recipe Management API Documentation

Welcome to the My Backend Capstone Project, a Recipe Management API documentation. 
This API allows you to manage recipes, categories, ingredients, and user accounts. All endpoints that require authentication expect a JWT token in the Authorization header.

##### STILL UPDATING AS PROJECT IS STILL BEING BUILT

## Authentication

### Register New User
**Endpoint:** `POST /api/auth/register/`

Creates a new user account.

Request body:
```json
{
    "username": "#",
    "email": "#",
    "password": "#"
}
```

Response (201 Created):
```json
{
    "id": 1,
    "username": "#",
    "email": "#"
}
```

### Login
**Endpoint:** `POST /api/auth/token/`

Obtains JWT token pair for authentication.

Request body:
```json
{
    "username": "#",
    "password": "#"
}
```

Response (200 OK):
```json
{
    "access": "#",
    "refresh": "#"
}
```

### Refresh Token
**Endpoint:** `POST /api/auth/token/refresh/`

Obtains new access token using refresh token.

Request body:
```json
{
    "refresh": "#"
}
```

Response (200 OK):
```json
{
    "access": "#"
}
```

## Recipes

### List Recipes
**Endpoint:** `GET /api/recipes/`

Retrieves a paginated list of recipes. Supports filtering and searching.

Query Parameters:
- `page`: Page number (default: 1)
- `search`: Search term for title or description
- `category`: Filter by category ID
- `ingredient`: Filter by ingredient name
- `preparation_time_lte`: Filter by maximum preparation time
- `ordering`: Sort by field (e.g., '-created_date', 'preparation_time')

Response (200 OK):
```json
{
    "count": 100,
    "next": "http://api.example.com/recipes/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Chocolate Cake",
            "description": "Delicious chocolate cake recipe",
            "ingredients": [
                {
                    "id": 1,
                    "name": "Flour",
                    "quantity": "2",
                    "unit": "cups"
                }
            ],
            "instructions": "1. Mix ingredients...",
            "category": {
                "id": 1,
                "name": "Desserts"
            },
            "preparation_time": 30,
            "cooking_time": 45,
            "servings": 8,
            "created_date": "2024-01-08T14:30:00Z",
            "creator": {
                "id": 1,
                "username": "johndoe"
            }
        }
    ]
}
```

### Get Single Recipe
**Endpoint:** `GET /api/recipes/{id}/`

Retrieves detailed information about a specific recipe.

Response (200 OK):
```json
{
    "id": 1,
    "title": "Chocolate Cake",
    "description": "Delicious chocolate cake recipe",
    "ingredients": [
        {
            "id": 1,
            "name": "Flour",
            "quantity": "2",
            "unit": "cups"
        }
    ],
    "instructions": "1. Mix ingredients...",
    "category": {
        "id": 1,
        "name": "Desserts"
    },
    "preparation_time": 30,
    "cooking_time": 45,
    "servings": 8,
    "created_date": "2024-01-08T14:30:00Z",
    "creator": {
        "id": 1,
        "username": "johndoe"
    }
}
```

### Create Recipe
**Endpoint:** `POST /api/recipes/`

Creates a new recipe. Requires authentication.

Request body:
```json
{
    "title": "Chocolate Cake",
    "description": "Delicious chocolate cake recipe",
    "ingredients": [
        {
            "name": "Flour",
            "quantity": "2",
            "unit": "cups"
        }
    ],
    "instructions": "1. Mix ingredients...",
    "category": 1,
    "preparation_time": 30,
    "cooking_time": 45,
    "servings": 8
}
```

Response (201 Created):
```json
{
    "id": 1,
    "title": "Chocolate Cake",
    "description": "Delicious chocolate cake recipe",
    "ingredients": [
        {
            "id": 1,
            "name": "Flour",
            "quantity": "2",
            "unit": "cups"
        }
    ],
    "instructions": "1. Mix ingredients...",
    "category": {
        "id": 1,
        "name": "Desserts"
    },
    "preparation_time": 30,
    "cooking_time": 45,
    "servings": 8,
    "created_date": "2024-01-08T14:30:00Z",
    "creator": {
        "id": 1,
        "username": "johndoe"
    }
}
```

### Update Recipe
**Endpoint:** `PUT /api/recipes/{id}/`

Updates an existing recipe. Requires authentication and recipe ownership.

Request body: Same as Create Recipe

Response (200 OK): Same as Create Recipe response

### Delete Recipe
**Endpoint:** `DELETE /api/recipes/{id}/`

Deletes a recipe. Requires authentication and recipe ownership.

Response (204 No Content)

### My Recipes
**Endpoint:** `GET /api/recipes/my_recipes/`

Retrieves authenticated user's recipes. Requires authentication.

Response: Same format as List Recipes

## Categories

### List Categories
**Endpoint:** `GET /api/categories/`

Retrieves all recipe categories.

Response (200 OK):
```json
[
    {
        "id": 1,
        "name": "Desserts",
        "description": "Sweet treats and desserts"
    }
]
```

### Create Category
**Endpoint:** `POST /api/categories/`

Creates a new category. Requires authentication.

Request body:
```json
{
    "name": "Desserts",
    "description": "Sweet treats and desserts"
}
```

Response (201 Created): Same as request body with ID

## Ingredients

### List Ingredients
**Endpoint:** `GET /api/ingredients/`

Retrieves all ingredients. Supports searching.

Query Parameters:
- `search`: Search term for ingredient name

Response (200 OK):
```json
[
    {
        "id": 1,
        "name": "Flour"
    }
]
```

### Create Ingredient
**Endpoint:** `POST /api/ingredients/`

Creates a new ingredient. Requires authentication.

Request body:
```json
{
    "name": "Flour"
}
```

Response (201 Created): Same as request body with ID

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
    "detail": "Invalid request data",
    "errors": {
        "field_name": [
            "Error message"
        ]
    }
}
```

### 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
    "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
    "detail": "Not found."
}
```

## Pagination

All list endpoints support pagination with the following query parameters:
- `page`: Page number (default: 1)
- `page_size`: Number of items per page (default: 10, max: 100)

## Search and Filtering

The recipe endpoints support various filtering options:
- Text search across title, description, and ingredients
- Category filtering
- Ingredient filtering
- Preparation time filtering
- Sorting by various fields

Example:
```
GET /api/recipes/?search=chocolate&category=1&preparation_time_lte=30&ordering=-created_date
```

## Rate Limiting

API requests are rate-limited to prevent abuse:
- Authenticated users: 100 requests per minute
- Anonymous users: 20 requests per minute

When rate limit is exceeded, the API returns 429 Too Many Requests:
```json
{
    "detail": "Request was throttled. Expected available in 30 seconds."
}
```