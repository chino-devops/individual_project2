# individual_project2

## Requirements

- An Asana board or equivalent Kanban board tech (Trello board)
- An fully fucntional application integrated into a Version Control System which will then be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine (GCP Virtual machines)
- Project must feature 4 services, 2 and 3 will be get requests sent to service 4 which will be a post request. all requests then sent to and displayed on service 1
- Project must be deployed using containerisation (Docker) and an orchestration tool (Docker Swarm)
- Ansible Playbook must be created provision the environment for the application
- Project must make use of a reverse proxy (NGINX) to make your application accessible to the user
- application must be able to show rolling updates without interrupting user experience 

documentation:

Trello board:https://trello.com/b/kW7ECZEc/individual-project-watches

My idea: Service 1 will be the user interface (front end web app)
- service 2 generates a random watch brand from a predetermined list (rolex, audemars piguet, vacheron constatin etc)
- Service 3 generates a random material which the product will be made from (gold, steel etc)
-  Service 4 generates a price based on the first two conditions from a predetermined list

Risk assessment:

[Screenshot-15.png](https://postimg.cc/N9BW2vC7)
Known issues:

- DB having issues connecting back to front end and interrupting displaying service 4
- testing: tests not running due to incorrect configuration
- did not have enough time to use swarm, jenkins and ansible

future improvements:

- spend less time on less important aspects of the project
- be more assertive when needing help
- always complete tracking board first