# remind-me-to

User should be able to put in a number, and an unit (miliseconds, days, years, etc.) and a message. The user will also have to register a way to contact them (email, text-message) 
The information gets passed on to the server and gets stored in a postgres database. Heroku has an add-on which acts basicly the equivalent as cron-jobs do and will be used to schedule the server for sending the user a message
