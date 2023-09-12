# API Documentation

## Table of Contents
- [Models](#models)
- [Endpoints](#endpoints)
  - [Add Person](#add-person)
  - [Search Person](#search-person)
  - [Get Person](#get-person)
  - [Count People](#count-people)

## Models
### Person
```json
{
  "ID": "string",
  "Name": "string",
  "Nickname": "string",
  "Birth": "string",
  "CreatedAt": "time.Time",
  "UpdatedAt": "time.Time"
}
```

## Endpoints

### Add Person
- **URL:** /pessoas
- **Method:** POST
- **Request Body:**
```json
{
  "ID": "string",
  "Name": "string",
  "Nickname": "string",
  "Birth": "string"
}
```
- **Response:**
  - Status Code: 201
  - Body:
```json
{
  "ID": "string",
  "Name": "string",
  "Nickname": "string",
  "Birth": "string",
  "CreatedAt": "time.Time",
  "UpdatedAt": "time.Time"
}
```
- **Example:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "ID": "1",
  "Name": "John Doe",
  "Nickname": "JD",
  "Birth": "1990-01-01"
}' http://localhost:8080/pessoas
```

### Search Person
- **URL:** /pessoas
- **Method:** GET
- **Query Parameters:**
  - t: string (required)
- **Response:**
  - Status Code: 200
  - Body:
```json
[
  {
    "ID": "string",
    "Name": "string",
    "Nickname": "string",
    "Birth": "string",
    "CreatedAt": "time.Time",
    "UpdatedAt": "time.Time"
  }
]
```
- **Example:**
```bash
curl -X GET 'http://localhost:8080/pessoas?t=John'
```

### Get Person
- **URL:** /pessoas/:id
- **Method:** GET
- **Path Parameters:**
  - id: string
- **Response:**
  - Status Code: 200
  - Body:
```json
{
  "ID": "string",
  "Name": "string",
  "Nickname": "string",
  "Birth": "string",
  "CreatedAt": "time.Time",
  "UpdatedAt": "time.Time"
}
```
- **Example:**
```bash
curl -X GET 'http://localhost:8080/pessoas/1'
```

### Count People
- **URL:** /contagem-pessoas
- **Method:** GET
- **Response:**
  - Status Code: 200
  - Body: integer
- **Example:**
```bash
curl -X GET 'http://localhost:8080/contagem-pessoas'
```

*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*