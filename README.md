
#Playbook
----------

## What is this?
Playbook is a workflow engine for performing various tasks from the perspective of the NOC (Network Operations Center) team's perspective.  The basic idea is to wrap tooling around action items that are performed when something happens.  This could be restarting a service, calling the SME who is on-call via Twilio, etc.


## Models
- SMEs (Subject Matter Experts)
  - Cell Phone Number
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
- Schedule (allow for multiple per Calendar)
  - Schedule name
  - Associated Calendar
  - Start time
  - End time
  - Recurrence pattern (if any)
- Actions
  - Action Type
    - Twilio SMS
    - Twilio Phone call
    - HipChat notification
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
