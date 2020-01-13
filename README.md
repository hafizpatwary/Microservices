Presentation Link: https://docs.google.com/presentation/d/1fnFwZXLDXZT04di-YbaYPCNdkgrMjLmZ2AKxPxxrEfE/edit?usp=sharing
Web application: http://35.223.251.82/



# Microservices
An application that takes advantage of micro-service architecture and contenarisation

## Index
[Brief](#brief)
   * [Solution](#brief)
   * [Architecture](#architecture)
   * [Micorservices](#microservices)
   * [Entity Relationship Diagrams](#erd)

[Risk Assessment](#risks)
   * [Risk Sssessment Table](#risks)
   * [Explanations](#risks_expl)

[Deployment](#depl)
   * [Technologies Used](#tech)
   * [Testing](#testing)

[Project planning and user stories](#user_sotry)
   * [Use case diagram](#use_case)
   * [UML diagram](#uml)

[Improvements for the Future](#improve)
[Authors](#auth)

<a name="brief"></a>
## The Brief
The aims of the project are as follows:

* Create a service ortiented web-application, that is comprised of at least four services. Each service must have two different implementation that can be swapped between them without disrupting the user experience.
* Build a CI pipeline using Jenkins that automatically updates and deploys the web-app when source code is updated.
* Create ansible playbook to automate configuation of resources (VMs) required for this project

## Solution

For my web application I decided to create a quiz game. The app presents the user a randomly generated flag, where the user has to guess which country the flag belongs to based on a multiple choice question.
If the user guesses correctly, the user is rewarded with a voucher for a plane ticket.
<a name="architecture"></a>
### Architecture
To create the app, the services architecture is shown below:
<a name="microservices"></a>
<img src="/Documentation/microservice_architecture.png" alt="Microservice architecture" />

#### Country generator service:
   * This service essentially generates the question that will be shown on the frontend. To create the multiple choice question, it generates a random list of unique countires from a json file. Once the selection has been done, it parses a json package with the countries and a flag from one of those countries.

#### Temperature api service:
  * This service selects a random city from a list of cities and makes an api call to openweathermap.com to get the current temperature. The response is decoded and then parsed to the desired JSON format to be used by service 4.

#### Voucher generator service:
  * Combines the JSON objects recieved from service 2 and 3 with some logic to create a voucher. The current logic set is to generate a prize based on number of options, set in the quiz, and the current weather.

#### Frontend service:
  * This is the service that the user will be interacting with. The frontend uses the country service to retrieve the flag quiz. Upon submission of quiz, if the answer is correct, the forntend then proceeds to make a get request to the voucher service to reward the user. Additionally it also persist some data to an SQL database, such as the response of the user to the question and user's email address used to retrieve the voucher.
<a name="erd"></a>
### Entity Relationship Diagrams
![Entity RelationShip diagram](/Documentation/database_architecture.png)

Altough having an entity relationship diagram was not a requirement for this project, it was useful to revise some database concepts and practice SQLAlchemy's syntax.
The tables above are used by the frontend to store the answer to the quiz given by the user and email address given to retrieve the voucher.

<a name="risks" ></a>
## Risk Assessment
| Risks                            | Likelihood    | Impact       |    Explanation          |
| -------------------------------- |:-------------:| :-----------:| -----------------------:|
| Uploading API key to GitHub      | High          | High         | [1 Click here](#api)
| External database manipulation   | Medium        | High         | [2 Click here](#sql)
| Automation causing issues        | Medium        | High         | [3 Click here](#automation)
| Container losing data when VM stopped | High     | High         | [4 Click here](#container)
| Website malfunctions because code is broken |  Medium | High    | [5 Click here](#borken_code)


<a name="risks_expl" ></a>
<a name="api"></a>
#### Uploading API key to GitHub
Service three retrieves the temperature of a random city by making an api request to openweathermap.com.
The website lets the application retrieve the data required for this project for free, however there also paid services which requires the API key. When writing source code I might upload these keys on GitHub my mistake:
Solution:
+ Set the API key as an enviorment variable
<a name="sql"></a>
#### External database manipulation
During development it is likely that I will be working on different machines, hence there will be a public Git repo. It is very likely that I may upload some credentials by mistake

Solution:
* Set enviornmental variables so that credentials can be accesed by one person only
* Delete credentials if you know someone else might use the same machine
<a name="automation"></a>
#### Automation causing issues
Automation can save a lot of time and hassle if done right, however if not done properly it can:
* When writing Ansible playbook, it is important to write them as versatile as possible, like not having the host name hardcoded but instead one that varies automatically.

Solution:
* Automate only repetitive tasks such as deployment
* Do not automate a task that is not repetitive, such as setting environmental variables
<a name="container"></a>
#### Container losing data when VM stopped
It is important to realise that when a VM is stopped, the docker containers exit. On restart of VM, the containers can also be restarted, however they won't be the same as before.
Solution:
* Set container to the option "--restart=always"
* Set volumes to the container
<a name="borken_code"></a>
#### Website malfunctions because code is broken
* Always test before pushing code
* Set up a test enviornment
<a name="depl" ></a>
## Deployment
The test and deployment process for the web app was automated using Jenkins, a CI server. Jenkins runs in a GCP instance that automatically deploys the webapp into deployment server, with a webhook to GitHub which is triggered with every push event.
Ansible was used to create VMs with the correct configuration, to automate the process of setting environmetns for production and CI server.

Jenkins job:
* Once code is pushed to GitHub, Jenkins is triggered
* Jenkins downloads executable Jenkinsfile
* It run an automated test on the code
* Build images from yaml file and pushes image to local repo
* Pulls image down on Deployment server and makes a rolling update.
<img src="/Documentation/CI_pipeline.png" alt="CI Pipeline" />

<a name="tech"></a>
### Technologies Used

* Database: GCP SQL Server
* Programming language: Python
* Framework: Flask
* Deployment: Gunicorn
* CI Server: Jenkins
* Test Reporting: Pytest
* VCS: [Git](https://github.com/hafizpatwary/microservices)
* Project Tracking: [Trello](https://trello.com/b/Edpyk0uq/solo-project-qa)
* Live Environment: GCP
* Containerization: Docker
* Configuration Management: Ansible
* Orchestration: Docker-compose

<a name="testing"></a>
## Testing
Testing has been done using pytest. The coverage report for the services overall is 92%.
The breakdown of test coverage for each service is reported below with explanation wherever is necessary.
### Test for Service 2 (Contry Genarator)

<img src="/Documentation/countries_test_cov.png" alt="countries_test_cov" width="80%" height="80%" border="5"/>

### Test for Service 3 (Temperature)
<img src="/Documentation/temperature_api_test.png" alt="temperature_api_test" width="80%" height="80%" border="5"/>

### Test for Service 4 (Vouhcer Generator)
<img src="/Documentation/prize_test_cov.png" alt="prize_test_cov" width="80%" height="80%" border="5"/>

### Test for Service 1 (Frontend)
<img src="/Documentation/frontend_test_cov.png" alt="frontend_test_cov" width="80%" height="80%" border="5"/>


<a name="user_sotry"></a>
### Project planning and user stories
Project tracking was done using a trello board. Below the before and after of the project.
<img src="/Documentation/trello_before.png" alt="prize_test_cov" />
<img src="/Documentation/trello_after.png" alt="prize_test_cov" />
<a name="uml"></a>
### UML diagram

<a name="improve"></a>
## Improvements for the Future
* Currently the job running on Jenkins takes about two minutes, to run. Time can be reduced by about 10 seconds, by making jenkins cloning down only what is necessary for deplyment. Hence, ignoring file such as documentation, images and other unused code.
* In Ansible configuration I would break down the task in smaller files and making them more generic so that I can use them in the future for other projects.
* I would make an SQL container, rather than using a production ready database from GCP. I would save time during development and save gcp credit
