
# MediMyth Backend Documenation


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SQLALCHEMY_DATABASE_URI`

`SQLALCHEMY_TRACK_MODIFICATIONS`

`TWILIO_ACCOUNT_SID`

`TWILIO_AUTH_TOKEN`

## API Reference

### OTP

#### Get OTP

```http
  GET ​/otp/<phone number>
```

| Query Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone number` | `string` | **Required**. |

```js
const options = {method: 'GET'};

fetch('http://127.0.0.1:5000/otp/91XXXXXXXX', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```


### Doctor

#### Registration

**OTP must be generated before registration**

```http
  POST /doctor/register?phone=<phone>
```

| Query Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone` | `string` | **Required**. Number where otp is sent|

**Information you can post**
| JSON Body | Type     | Requirement                |
| :-------- | :------- | :------------------------- |
| `name` | `string(max 30 size)` | **Required**. |
| `phone_no` | `string(max 10 size)` | **Required**. |
| `email` | `string(max 30 size)` | **Required**. |
| `reg_no` | `string(max 20 size)` | **Required**. |
| `address` | `string` | **Required**. |
| `category` | `string(max 20 size)` | **Required**. |
| `password` | `string` | **Required**. |
| `profile_pic` | `file` | **Optional**. |
| `reff_code` | `string(max 10 size)` | **Optional**. |

```js
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json', token: 'generated OTP'},
  body: '{"name":"are","email":"homeuse.hu.1@gmail.com","phone_no":"91XXXXXXXX","address":"lsjflldsf","category":"lslf","reg_no":"1212","password":"arnab"}'
};

fetch('http://127.0.0.1:5000/doctor/register?phone=91XXXXXXXX', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
* returns -
```json
"token":"access-token"
```

### Access Doctor Account

#### Login

```http
GET doctor/?email=<registered email>&password=<password>
```
| Query Parameters | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `registered email` | `string` | **Required**. |
| `password` | `string` | **Required**. |

```js
const options = {method: 'GET'};

fetch('http://127.0.0.1:5000/doctor/?email=home.hu.1%40gmail.com&password=1212', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```

* returns -
```json
"token":"access-token"
```

#### Update Information

```http
PUT /doctor/
```

**access-token** be present in the headers to Update

```js
const options = {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
    'access-token': 'access-token' // you can get this by login or registration
  },
  body: '{"name":"snsdf","email":"homeuse.hu.70@gmail.com"}'
};

fetch('http://127.0.0.1:5000/doctor/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```

**Information you can Update**
| JSON Body | Type     | 
| :-------- | :------- |
| `name` | `string(max 30 size)` | **Optional**. |
| `phone_no` | `string(max 10 size)` | **Optional**. |
| `email` | `string(max 30 size)` | **Optional**. |
| `reg_no` | `string(max 20 size)` | **Optional**. |
| `address` | `string` | **Optional**. |
| `category` | `string(max 20 size)` | **Optional**. |
| `password` | `string` | **Optional**. |
| `profile_pic` | `file` | **Optional**. |
| `reff_code` | `string(max 10 size)` | **Optional**. |

* returns -
```json
"token":"token if email updated",
"status":"status of data"
```

#### Delete Account

```http
DELETE /doctor/
```

**access-token** be present in the headers to Delete

```js
const options = {
  method: 'DELETE',
  headers: {
    'access-token': 'access-token' // you can get this by login or registration
  }
};

fetch('http://127.0.0.1:5000/doctor/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```

* returns -
```json
"status":"status of account"
```