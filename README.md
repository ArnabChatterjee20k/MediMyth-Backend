
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
  .then(response => // console.log(response))
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
| `email_visibility` | `Boolean` | **Optional**. Default is true |
| `reg_no_visibility` | `Boolean` | **Optional**. Default is true |
| `phone_no_visibility` | `Boolean` | **Optional**. Default is true |

```js
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json', token: 'generated OTP'},
  body: '{"name":"are","email":"homeuse.hu.1@gmail.com","phone_no":"91XXXXXXXX","address":"lsjflldsf","category":"lslf","reg_no":"1212","password":"arnab"}'
};

fetch('http://127.0.0.1:5000/doctor/register?phone=91XXXXXXXX', options)
  .then(response => response.json())
  .then(response => // console.log(response))
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
  .then(response => // console.log(response))
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
  .then(response => // console.log(response))
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
  .then(response => // console.log(response))
  .catch(err => console.error(err));
```

* returns -
```json
"status":"status of account"
```


## Schdule

- Scheduling can be done by only **active doctors**.
- We need access-token in the headers for dealing with schedule

#### Get all schedules of a particular doctor

```http
  GET /schedule
```

| Header Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access-token` | `string` | **Required**. Doctor Access Token |

- **Example**
```javascript
let headersList = {
 "access-token": "<your access token>"
}

let response = await fetch("/schedule", { 
  method: "GET",
  headers: headersList
});

let data = await response.text();
// console.log(data);
```

#### Create a schedule

```http
  POST /schedule/
```

| Header Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `access-token` | `string` | **Required**. Doctor Access Token |

**Information you can post**
| JSON Body | Type     | Requirement                |
| :-------- | :------- | :------------------------- |
| `phone_no` | `string(max 10 size)` | **Optional**. If not provided then doctor's phone number will be taken |
| `day` | `int(0 to 6)` | **Required**.It represents the days in a week in numeric form |
| `specific_week` | `int(1,4)` | **Optional**. |
| `slot_start` | `string(in HH:MM:DD format)` | **Required**. |
| `slot_end` | `string(in HH:MM:DD format)` | **Optional**. |
| `booking_start` | `int` | **Optional**.Represents how **days before** the booking will start |
| `booking_end` | `int` | **Optional**. Represents how many **hours before** the booking will end|
| `fees` | `int` | **Optional**. |
| `address` | `string` | **Optional**. |
| `clinic_name` | `string` |Out of clinic_name and medical_shop atleast one is Required|
| `medical_shop` | `string` | Out of clinic_name and medical_shop atleast one is Required |

- **Example**
```javascript
let headersList = {
 "Content-Type": "application/json",
 "access-token": "<doctor access token>"
}

let bodyContent = JSON.stringify({
  "day": 1,
  "slot_start": "07:00:00",
  "address": "lsdfj",
  "medical_shop": "sdf",
  "clinic_name": "sdfd",
  "phone_no": "9812121212"
});

let response = await fetch("127.0.0.1:5000/schedule/", { 
  method: "POST",
  body: bodyContent,
  headers: headersList
});

let data = await response.text();
// console.log(data);

```

#### Updating a schedule

```http
  PUT /schedule/<schedule id>
```

| Header Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `access-token` | `string` | **Required**. Doctor Access Token |

**Information you can post**
| JSON Body | Type     | Requirement                |
| :-------- | :------- | :------------------------- |
| `phone_no` | `string(max 10 size)` | **Optional**. If not provided then doctor's phone number will be taken |
| `day` | `int(0 to 6)` | **Required**.It represents the days in a week in numeric form |
| `specific_week` | `int(1,4)` | **Optional**. |
| `slot_start` | `string(in HH:MM:DD format)` | **Required**. |
| `slot_end` | `string(in HH:MM:DD format)` | **Optional**. |
| `booking_start` | `int` | **Optional**.Represents how **days before** the booking will start |
| `booking_end` | `int` | **Optional**. Represents how many **hours before** the booking will end|
| `fees` | `int` | **Optional**. |
| `address` | `string` | **Optional**. |
| `clinic_name` | `string` |Out of clinic_name and medical_shop atleast one is Required|
| `medical_shop` | `string` | Out of clinic_name and medical_shop atleast one is Required |

- **Example**
```javascript
let headersList = {
 "Content-Type": "application/json",
 "access-token": "<doctor access token>"
}

let bodyContent = JSON.stringify({
  "address":"dsdff",
  "slot_start":"05:30:12"
});

let response = await fetch("127.0.0.1:5000/schedule/2", { 
  method: "PUT",
  body: bodyContent,
  headers: headersList
});

let data = await response.text();
// console.log(data);

```

#### Deleting a schedule

```http
  DELETE /schedule/<schedule id>
```

| Header Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `access-token` | `string` | **Required**. Doctor Access Token |

- **Example**
```javascript
let headersList = {
 "access-token": "<doctor access token>"
}

let response = await fetch("127.0.0.1:5000/schedule/2", { 
  method: "DELETE",
  headers: headersList
});

let data = await response.text();
// console.log(data);

```


## Appointment 

- Appointmenting to any schedule does not require any access-token
- Patient needs to provide some information for booking
- OTP verification will be their in booking. So otp token will be required

#### Get all Appointments of a specific schedule

```http
  GET /appointment/<schedule id>
```

* Example

```javascript
let response = await fetch("127.0.0.1:5000/appointment/1", { 
  method: "GET"
});

let data = await response.text();
// console.log(data);

```

#### Book an appointment

- **Phone number must be verified before registration**

```http
  POST  /appointment/<schedule id>?phone=<phone number where otp is sent>
```

| Query Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `phone`      | `string(max size 10)` | **Required**|


| Header Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**|

| JSON Parameters | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**|
| `age`      | `int` | **Required**|
| `contact_number`      | `string(max of 10 size)` | **Required**|

* Example
```javascript
let headersList = {
 "token": "12345",
 "Content-Type": "application/json"
}

let bodyContent = JSON.stringify({
  "name":"arnab chatterjee",
  "age":18,
  "contact_number":"9064846599"
});

let response = await fetch("127.0.0.1:5000/appointment/1?phone=123456789", { 
  method: "POST",
  body: bodyContent,
  headers: headersList
});

let data = await response.text();
// console.log(data);

```
