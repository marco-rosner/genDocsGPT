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
| Field      | Type      | Description     |
|------------|-----------|-----------------|
| ID         | string    | Unique ID       |
| Name       | string    | Person's name   |
| Nickname   | string    | Person's nickname |
| Birth      | string    | Person's birthdate |
| CreatedAt  | time.Time | Creation timestamp |
| UpdateAt   | time.Time | Last update timestamp |

## Endpoints

### Add Person
#### Request
- Method: POST
- Path: `/pessoas`

#### Request Body
```json
{
  "id": "string",
  "name": "string",
  "nickname": "string",
  "birth": "string"
}
```

#### Response
- Status Code: 201 Created
- Body:
```json
{
  "id": "string",
  "name": "string",
  "nickname": "string",
  "birth": "string"
}
```

### Search Person
#### Request
- Method: GET
- Path: `/pessoas`

#### Query Parameters
- `t` (required): Search term

#### Response
- Status Code: 200 OK
- Body:
```json
[
  {
    "id": "string",
    "name": "string",
    "nickname": "string",
    "birth": "string",
    "createdAt": "time.Time",
    "updatedAt": "time.Time"
  }
]
```

### Get Person
#### Request
- Method: GET
- Path: `/pessoas/:id`

#### Path Parameters
- `id` (required): ID of the person

#### Response
- Status Code: 200 OK
- Body:
```json
{
  "id": "string",
  "name": "string",
  "nickname": "string",
  "birth": "string",
  "createdAt": "time.Time",
  "updatedAt": "time.Time"
}
```

### Count People
#### Request
- Method: GET
- Path: `/contagem-pessoas`

#### Response
- Status Code: 200 OK
- Body:
```json
{
  "count": 0
}
```

*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*