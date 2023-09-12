# API Documentation

## Person

### Model

```go
package models

import "time"

type Person struct {
	ID        string `json:"id" `
	Name      string `json:"name" binding:"required"`
	Nickname  string `json:"nickname" binding:"required"`
	Birth     string `json:"birth" binding:"required"`
	CreatedAt time.Time
	UpdateAt  time.Time
}
```

### Handlers

#### SearchPerson

Searches for a person based on a given term.

##### Request

- Method: GET
- Path: /pessoas
- Query Parameters:
  - t (string, required): The search term

##### Response

- Status Code: 200 (OK)
- Body: JSON representation of the person(s) found

##### Example

```bash
curl -X GET "http://localhost:8080/pessoas?t=John"
```

#### AddPerson

Adds a new person.

##### Request

- Method: POST
- Path: /pessoas
- Body: JSON representation of the person to be added

##### Response

- Status Code: 201 (Created)
- Body: JSON representation of the added person

##### Example

```bash
curl -X POST "http://localhost:8080/pessoas" -d '{"name":"John Doe","nickname":"JD","birth":"1990-01-01"}'
```

#### GetPerson

Gets a specific person by ID.

##### Request

- Method: GET
- Path: /pessoas/{id}
- Path Parameters:
  - id (string): The ID of the person

##### Response

- Status Code: 200 (OK)
- Body: JSON representation of the person

##### Example

```bash
curl -X GET "http://localhost:8080/pessoas/123"
```

#### CountPeople

Counts the number of people.

##### Request

- Method: GET
- Path: /contagem-pessoas

##### Response

- Status Code: 200 (OK)
- Body: Number of people

##### Example

```bash
curl -X GET "http://localhost:8080/contagem-pessoas"
```