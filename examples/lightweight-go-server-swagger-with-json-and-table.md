# API Documentation

## Table of Contents
- [Search Person](#search-person)
- [Add Person](#add-person)
- [Count People](#count-people)
- [Get Person](#get-person)

---

## Search Person

Searches for a person based on a term.

**URL** : `/pessoas`

**Method** : `GET`

**Query Parameters** : 
- `t` (string, required) - The search term.

**Success Response** : 
- Code: 200
- Content: JSON array of person objects.

**Error Responses** : 
- Code: 400
- Content: "bad request"

- Code: 404
- Content: Error message if person not found.

- Code: 500
- Content: Error message if internal server error occurs.

---

## Add Person

Adds a new person.

**URL** : `/pessoas`

**Method** : `POST`

**Request Body** : JSON object representing the person.

**Success Response** : 
- Code: 201
- Content: JSON object representing the added person.

**Error Responses** : 
- Code: 400
- Content: "ValidationError: " followed by error message if validation fails.

- Code: 500
- Content: Error message if internal server error occurs.

---

## Count People

Counts the total number of people.

**URL** : `/contagem-pessoas`

**Method** : `GET`

**Success Response** : 
- Code: 200
- Content: Number representing the total count of people.

**Error Responses** : 
- Code: 404
- Content: Error message if count fails.

---

## Get Person

Retrieves a person by ID.

**URL** : `/pessoas/:id`

**Method** : `GET`

**URL Parameters** : 
- `id` (string) - The ID of the person.

**Success Response** : 
- Code: 200
- Content: JSON object representing the retrieved person.

**Error Responses** : 
- Code: 404
- Content: "Person not found" if person with specified ID is not found.

*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*