# Person API

API to manage person data.

## Add Person

Add a new person to the database.

### Request

`POST /pessoas`

#### Parameters

| Name      | Type   | Description                |
| --------- | ------ | -------------------------- |
| `name`    | string | The name of the person     |
| `nickname`| string | The nickname of the person |
| `birth`   | string | The birthdate of the person|

### Response

#### Success Response

- Code: 201
- Content: `{"id": "string", "name": "string", "nickname": "string", "birth": "string"}`

#### Error Response

- Code: 400
- Content: `"ValidationError: string"`

## Search Person

Search for a person in the database.

### Request

`GET /pessoas`

#### Parameters

| Name | Type   | Description                |
| ---- | ------ | -------------------------- |
| `t`  | string | The search term             |

### Response

#### Success Response

- Code: 200
- Content: `[{"id": "string", "name": "string", "nickname": "string", "birth": "string"}]`

#### Error Response

- Code: 400
- Content: `"bad request"`

## Get Person

Get a person by ID.

### Request

`GET /pessoas/:id`

#### Parameters

| Name | Type   | Description                |
| ---- | ------ | -------------------------- |
| `id` | string | The ID of the person        |

### Response

#### Success Response

- Code: 200
- Content: `{"id": "string", "name": "string", "nickname": "string", "birth": "string"}`

#### Error Response

- Code: 404
- Content: `"Person not found"`

## Count People

Get the count of people in the database.

### Request

`GET /contagem-pessoas`

### Response

#### Success Response

- Code: 200
- Content: `integer`

#### Error Response

- Code: 404
- Content: `"Error message"`

*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*