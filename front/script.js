function access_request() {
  let getEmail = document.loginForm.emailField.value;
  let getUser = document.loginForm.employeeField.value;
  let getRequest = document.loginForm.requestField.value;

  verify_login(getEmail, getUser, getRequest);
}

async function verify_login(email, user_id, request_id) {
  let isEmailOrUserGood = false;
  let isRequestGood = false;
  let myRequest = null;
  let myEmployee = null;

  // Check to see if the email given exists with an employee from database
  const employeeListURL = `http://localhost:5000/employees`;
  const employeeListResponse = await fetch(employeeListURL);
  const employeeList = await employeeListResponse.json();

  for (let employee of employeeList) {
    if (employee.email === email && employee.id == user_id) {
      isEmailOrUserGood = true;
      myEmployee = employee;
      break;
    }
    else console.log(employee.id + " does not match with " + user_id);
  }

  if (!isEmailOrUserGood) {
    console.log("The given e-mail and employee ID do not correspond or exist in database")
    return;
  }
  else console.log("Proceeding to check request ID...")

  // If successful, check if this employee has a request in database
  const requestListURL = `http://localhost:5000/requests`;
  const requestListResponse = await fetch(requestListURL);
  const requestList = await requestListResponse.json();

  for (let request of requestList) {
    if (request.id == request_id && request.employee_id == user_id) {
      isRequestGood = true;
      myRequest = request;
      break;
    }
  }

  if (!isRequestGood) {
    console.log("The given request ID does not exist in the database or is not accessible to the user");
    return;
  }
  else alert("You can log in!!");

  // If successful, check if this employee has a request in database
  // const url = `http://localhost:5000/requests`;
  // const httpResponse = await fetch(url);
  // const body = await httpResponse.json();
  // console.log("Verifying login credentials...");
  // console.log(body[0]);

  //If successful, get the employee role to determine what user can do
  //window.location()
}

// async function get_response(url) {

// }

function create_request() {
  console.log("Sending request form to database...");

  let getName = document.newEmployeeForm.fname.value + " " +
   document.newEmployeeForm.lname.value;
  let getEmail = document.newEmployeeForm.email.value;
  let getPhone = document.newEmployeeForm.phone.value;
  let getAddress = document.newEmployeeForm.employeeaddress.value + ", " +
    document.newEmployeeForm.employeecity.value + ", " +
    document.newEmployeeForm.employeestate.value + " " +
    document.newEmployeeForm.employeezip.value;

  let getEventType = document.newEventForm.eventtype.value;
  let getStartDate = document.newEventForm.eventdate.value.split("-");
  getStartDate = new Date(getStartDate[0], getStartDate[1] - 1, getStartDate[2]);
  let getLocation = document.newEventForm.eventaddress.value + ", " +
    document.newEventForm.eventcity.value + ", " +
    document.newEventForm.eventstate.value + " " +
    document.newEventForm.eventzip.value;
  let getDescription = document.newEventForm.description.value;
  let getCost = document.newEventForm.cost.value;
  console.log("All fields completed!");
  // Create JSON for the employee data to be sent to Postman
  let newEmployee = {
    "name": getName,
    "phone": getPhone,
    "address": getAddress,
    "email": getEmail
  };

  newEmployee = sendEmployeeData(newEmployee).then(emp => {emp;});
  console.log(newEmployee);

  let newRequest = {
    "amount_reimb": 1000.00,
    "cost": getCost,
    "employee_id": newEmployee.id,
    "grade": "72 of 75",
    "status": "Awaiting supervisor approval"
  };
  //console.log(newRequest);
  // newRequest = sendRequestData(newRequest);
  // console.log(newRequest);
  // Check if the event needs to be added to the database (if nec.)
  let newEvent = {
    "type": getEventType,
    "start_date": getStartDate,
    "description": getDescription,
    "location": getLocation
  };
  //newEvent = sendEventData(newEvent);
  //console.log(newEvent);
  // Otherwise, get ID of existing event and link it to this request

  // Create JSON for the request details to be added
}

async function sendEmployeeData(employeeObject) {
  const employeePostURL = `http://localhost:5000/employees`;
  const employeePostOptions = {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeObject)
  };
  const employeePostResponse = await fetch(employeePostURL, employeePostOptions);
  const emp = await employeePostResponse.json();
  return emp;
}

async function sendRequestData(requestObject) {
  const requestPostURL = `http://localhost:5000/requests`;
  const requestPostOptions = {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestObject)
  };
  const requestPostResponse = await fetch(requestPostURL, requestPostOptions);
  const rqst = await requestPostResponse.json();
  return rqst;
}

async function sendEventData(requestID, eventObject) {
  let id = requestID;
  const eventPostURL = `http://localhost:5000/requests/${id}/event`;
  const eventPostOptions = {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(eventObject)
  };
  const eventPostResponse = await fetch(eventPostURL, eventPostOptions);
  const ev = await eventPostResponse.json();
  return ev;
}
