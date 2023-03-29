# Django API + ReactJS mono-repo

A simple application with Django API and ReactJS frontend to manage a CRUD of projects.


### Requirements
- Docker
- Makefile

### Install check-list
- [ ] Create local.env in `src/api/core/local.env` from template
- [ ] Create django secrets and put in `local.env`
- [ ] Set Sentry DSN in `local.env` if you want to use Sentry

### Run
- `make up` to start the project


### Urls
- API: http://localhost:8000
- Frontend: http://localhost:3000