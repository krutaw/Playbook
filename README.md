
# Playbook
----------

## What is this?
Playbook is a workflow engine for performing various tasks from the perspective of the NOC (Network Operations Center) team's perspective.  The basic idea is to wrap tooling around action items that are performed when something happens.  This could be restarting a service, calling the SME who is on-call via Twilio, etc.

## Standards
- Language
  - All code shall conform to Python 3.6+
  - All code shall pass Python Linter

## Models
- SMEs (Subject Matter Experts)
  - Cell Phone Number
  - Username
  - Email address
  - Given name
  - Surname
- Teams (made up of SMEs)
  - Team Name
  - Team manager
  - SME
- Calendars (allow for multiple per team)
  - Calendar name
  - Associated team
- RecurRule
  - Name
  - Description
  - Frequency
  - Params
- Schedule (allow for multiple per Calendar)
  - Schedule name
  - Associated Calendar
  - Start time
  - End time
  - Recurrence pattern (if any)
- Schedule order
  - OnCall SME
  - Oncall Order
  - Oncall Schedule (reference to Schedule)
- Actions
  - Action Type
    - Twilio SMS
    - Twilio Phone call
    - HipChat notification
      - Hipchat Room
    - Email
    - Ansible playbook
      - Associated certificate
    - Recovery check
  - Action Name
- Auth Certificate
  - Password
  - Certificate name
- Playbook
  - Playbook Name
  - Associated Team
- Play
  - Associated Playbook
  - Order
  - Associated Action
  - Number of Retries
  - Associated action to check recovery (used for auto-corrective actions only)

## Interfaces
- Basic web interface for Playbook definition
- API for tool interaction

## Logical workflow
![Logical workflow](https://github.com/krutaw/Playbook/blob/master/Playbook_workflow.png)

## Installation
- Clone
- Update core/Settings.py
  - REST_FRAMEWORK
    - URL_FIELD_NAME
