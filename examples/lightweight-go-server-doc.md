# API Documentation

## Models

### Person

Represents a person.

| Field     | Type      | Description       |
| --------- | --------- | ----------------- |
| ID        | string    | The person's ID    |
| Name      | string    | The person's name  |
| Nickname  | string    | The person's nickname |
| Birth     | string    | The person's birth date |
| CreatedAt | time.Time | The time the person was created |
| UpdateAt  | time.Time | The time the person was last updated |

## Handlers

### SearchPerson

Searches for a person based on a search term.

**Request**

- Method: GET
- Path: /pessoas
- Query Parameters:
  - t: The search term

**Response**

- Status Code: 200 (OK)
- Body: The found person(s)

### AddPerson

Adds a new person.

**Request**

- Method: POST
- Path: /pessoas
- Body: The person to add

**Response**

- Status Code: 201 (Created)
- Body: The added person

### CountPeople

Counts the number of people.

**Request**

- Method: GET
- Path: /contagem-pessoas

**Response**

- Status Code: 200 (OK)
- Body: The number of people

### GetPerson

Gets a person by ID.

**Request**

- Method: GET
- Path: /pessoas/:id
- Path Parameters:
  - id: The ID of the person

**Response**

- Status Code: 200 (OK)
- Body: The found person

*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*