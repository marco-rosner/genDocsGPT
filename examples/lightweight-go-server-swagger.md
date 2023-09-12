## API Documentation

### Person

Represents a person.

#### Properties

- ID: string (required) - The ID of the person.
- Name: string (required) - The name of the person.
- Nickname: string (required) - The nickname of the person.
- Birth: string (required) - The birth date of the person.
- CreatedAt: time.Time - The timestamp when the person was created.
- UpdateAt: time.Time - The timestamp when the person was last updated.

### Handlers

#### SearchPerson

Searches for a person based on a term.

- Method: GET
- Path: /pessoas
- Query Parameters:
  - t: string (required) - The search term.
- Responses:
  - 200 OK: Returns the list of matching persons.
  - 400 Bad Request: If the search term is missing.
  - 404 Not Found: If no matching persons are found.
  - 500 Internal Server Error: If an error occurs during the search.

#### AddPerson

Adds a new person.

- Method: POST
- Path: /pessoas
- Request Body: Person (JSON)
- Responses:
  - 201 Created: Returns the created person.
  - 400 Bad Request: If the request body is invalid.
  - 500 Internal Server Error: If an error occurs during the creation.

#### CountPeople

Counts the number of people.

- Method: GET
- Path: /contagem-pessoas
- Responses:
  - 200 OK: Returns the number of people.
  - 404 Not Found: If an error occurs during the count.

#### GetPerson

Gets a person by ID.

- Method: GET
- Path: /pessoas/:id
- Path Parameters:
  - id: string (required) - The ID of the person.
- Responses:
  - 200 OK: Returns the person.
  - 404 Not Found: If the person is not found.

*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*