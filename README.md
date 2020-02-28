# qU : Automated Queue Management System

### Objective

Developing Automated Queue Management System for Walk-In-Customer in the Branch with the help of latest technology like QR Codes, IoT etc. The customer should be able to scan QR code to get the ticket, which will guide the customer further by informing the counter number to serve him at the earliest. The system shall automatically re-schedule the counter to maintain FIFO order depending on customer requirements. Centralized monitoring system shall analyze the queue data, suggest the Branch to improve turnaround time and rank the branches accordingly.

### Tech Stack Used

- Python 3.x
- Django
- MongoDB

### Steps to Runserver
1. Install Django by running :`pip install django` in terminal
2. Install Mongo by runnning : `pip install mongoengine`
3. Run `python manage.py runserver`

### How qU works 

Here are the steps for a walk-in customer to make a Deposit Transaction: 
1. Collect an application form from the branch or download one, online. 
2. Fill the form with details and make sure you have copies of any required documents (if any) like ID proof, cheque leaflet etc. 
3. Find a Counter, which might not always be properly labelled or understood by customers, which handles fund transfers and get in the queue. 
4. Wait for your turn with no estimated wait time. Customers also have to stand in queue physically for a long time before their turn comes. Customers often find they have made a mistake with the form or are missing some required documents. They might have to restart in the queue or disturb the queue when they return with the required documents. 
5. Get the application processed, collect receipt of transfer. 
6. Transaction is now complete.

### Data Model

![/datamodel.png]
