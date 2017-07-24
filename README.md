
Slack-phonebook is a simple ready-to-deploy phonebook for Slack.

The application will generate a phone book of all your Slack users. You can filter users to remove bots and deleted users. You can also choose fields to display.

Main features:

- Responsive web phonebook
- Choose fields to display (email, phone, ...)
- Phone numbers format
- VCARD export

Screenshot:

    ****FIXME****

# Installation

The application need a Slack token to build your phonebook.

You need to generate a Slack token [https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)

## Docker

Installation using Docker is quiet simple, pull and run the application.

    docker run -p 8000:8000 -e SLACK_TOKEN=<your_slack_token> vmercier/slack-phonebook:latest

Connect on your docker :

    http://<docker_ip>:8000

## Docker compose

    ****FIXME****

## Ansible

Create a playbook file called **deploy_phonebook.yml** with the following content:
	
	******TODO******
	******TODO******
	******TODO******
	******TODO******
	******TODO******
	******TODO******
	******TODO******
	******TODO******
	******TODO******

Execute playbook:

    ansible-playbook deploy_phonebook.yml --diff

## Sources

# Configuration

List of available environment variables:

| Parameter | Default value | Description |
| --- | --- | --- |
| CACHE\_EXPIRATION | 43 200 | Cache expiration in seconds. By default the cache is configured to 12h. |
| SLACK\_TOKEN| None| Slack token to use  |
| SLACK\_INCLUDE\_DELETED\_USERS| False| Include deleted users| Notes that deleted Slack users stay in Slack user list |
| SLACK\_INCLUDE\_DISABLED\_USERS| False| Include disabled users |
| SHOW\_USER\_EMAIL| True| Show user email |
| SHOW\_USER\_PHONE| True| Show user phone |
| SHOW\_USER\_VCARD| True| Enable vcard export |
| SHOW\_USER\_TITLE| True| Display user title (eg. position in the team) |
| PAGE\_TITLE| Phonebook| Title of page (<tiitle> tag) |
| PAGE\_MESSAGE| Here is the team!| Text to display in page header. Could include html. |
| HTTP\_PROXY| None| Proxy to use for HTTP request |
| HTTPS\_PROXY| None| Proxy to use for HTTPS request |