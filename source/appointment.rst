********************
Appointment Package
********************

Creating An Appointment
########################

In order to create an appointment, send an authorised **POST** request to
::
    http://localhost:8000/api/appointments/

The body of the request should contain a json object that follows the following schema

.. code-block:: json

    {
        "service_provider": 1,
        "service_type": 2,
        "time": "10:00 AM",
        "date": "2020-03-10",
        "comment": "hello"
    }

#. The **service_provider** field takes the id of the servce provider
#. The **service_type** field takes the id of the service requested
#. The **time** field takes the times as a string with *AM/PM* appended
#. The **date** field takes the date in the format *YYYY-MM-DD*
#. The **comment** field is optional and takes a string


