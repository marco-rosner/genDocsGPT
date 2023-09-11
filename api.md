# API Documentation

## Table of Contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [1. User](#user)
    - [1.1 Get User](#get-user)
    - [1.2 Create User](#create-user)
    - [1.3 Update User](#update-user)
    - [1.4 Delete User](#delete-user)
  - [2. Products](#products)
    - [2.1 Get Products](#get-products)
    - [2.2 Create Product](#create-product)
    - [2.3 Update Product](#update-product)
    - [2.4 Delete Product](#delete-product)

## Introduction<a name="introduction"></a>
This API documentation provides information on the available endpoints and their functionalities.

## Authentication<a name="authentication"></a>
To access the API, you need to include your API key in the request header. The API key should be included in the `Authorization` header as follows:
```
Authorization: Bearer <your_api_key>
```

## Endpoints<a name="endpoints"></a>

### 1. User<a name="user"></a>

#### 1.1 Get User<a name="get-user"></a>
- Method: GET
- Endpoint: `/users/{id}`
- Description: Retrieves user information based on the provided ID.
- Request Parameters:
  - `id` (required): ID of the user.
- Response:
  - Status Code: 200 (OK)
  - Body: JSON object containing user details.

#### 1.2 Create User<a name="create-user"></a>
- Method: POST
- Endpoint: `/users`
- Description: Creates a new user.
- Request Body: JSON object containing user details.
- Response:
  - Status Code: 201 (Created)
  - Body: JSON object containing the created user details.

#### 1.3 Update User<a name="update-user"></a>
- Method: PUT
- Endpoint: `/users/{id}`
- Description: Updates user information based on the provided ID.
- Request Parameters:
  - `id` (required): ID of the user to be updated.
- Request Body: JSON object containing updated user details.
- Response:
  - Status Code: 200 (OK)
  - Body: JSON object containing the updated user details.

#### 1.4 Delete User<a name="delete-user"></a>
- Method: DELETE
- Endpoint: `/users/{id}`
- Description: Deletes a user based on the provided ID.
- Request Parameters:
  - `id` (required): ID of the user to be deleted.
- Response:
  - Status Code: 204 (No Content)

### 2. Products<a name="products"></a>

#### 2.1 Get Products<a name="get-products"></a>
- Method: GET
- Endpoint: `/products`
- Description: Retrieves a list of products.
- Response:
  - Status Code: 200 (OK)
  - Body: JSON array containing product objects.

#### 2.2 Create Product<a name="create-product"></a>
- Method: POST
- Endpoint: `/products`
- Description: Creates a new product.
- Request Body: JSON object containing product details.
- Response:
  - Status Code: 201 (Created)
  - Body: JSON object containing the created product details.

#### 2.3 Update Product<a name="update-product"></a>
- Method: PUT
- Endpoint: `/products/{id}`
- Description: Updates product information based on the provided ID.
- Request Parameters:
  - `id` (required): ID of the product to be updated.
- Request Body: JSON object containing updated product details.
- Response:
  - Status Code: 200 (OK)
  - Body: JSON object containing the updated product details.

#### 2.4 Delete Product<a name="delete-product"></a>
- Method: DELETE
- Endpoint: `/products/{id}`
- Description: Deletes a product based on the provided ID.
- Request Parameters:
  - `id` (required): ID of the product to be deleted.
- Response:
  - Status Code: 204 (No Content)

This concludes the API documentation.
