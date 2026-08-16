# Secure Aged Care Cloud Platform

> A cloud-native aged care operations platform designed to support secure resident care, workforce rostering, staffing continuity, and reliable multi-site operations.

## Project Overview

The **Secure Aged Care Cloud Platform** is an independent industry project designed around operational challenges faced by aged care providers.

Aged care organisations may operate across multiple facilities with personal care workers, nurses, doctors, reception staff, roster coordinators, managers, and other employees depending on digital systems to perform their daily work.

Two key problems form the foundation of this project:

1. **Secure and reliable access to resident care information**
2. **Maintaining workforce continuity when rostered staff become unexpectedly unavailable**

The platform combines resident care operations and workforce rostering with cloud engineering, DevOps, security, and Site Reliability Engineering practices.

Rather than implementing cloud technologies as isolated demonstrations, each technology introduced into the project is intended to solve a defined operational or engineering problem.

---

# Problem Statement

A multi-site aged care provider needs to ensure that:

- Authorised staff can access the resident information required for their role.
- Sensitive resident information is protected from unnecessary access.
- Resident care services remain available across facilities.
- Staff schedules and availability can be managed centrally.
- Unfilled shifts can be identified quickly.
- Suitable replacement staff can be identified when employees become unavailable.
- System failures can be detected before they significantly affect operations.
- Application changes can be deployed safely and consistently.
- Infrastructure can recover from failures.
- Operational incidents can be investigated and documented.

The project explores how modern cloud and DevOps practices can address these requirements.

---

# Platform Objectives

The platform is organised around four primary engineering domains.

## 1. Resident Care Operations

The resident care component will progressively support:

- Resident profile management
- Appointment information
- Care-related information
- Reports and documents
- Secure document access
- Role-specific access to resident information
- Auditability of sensitive operations

The objective is not to expose an entire resident record to every employee.

Different users should receive only the information required to perform their role.

---

## 2. Workforce Rostering & Staffing Continuity

The workforce component will support:

- Staff profiles
- Aged care facilities
- Staff roles
- Staff availability
- Qualifications and compliance information
- Shift creation
- Shift assignments
- Unfilled shift detection
- Replacement worker identification
- Shift acceptance
- Roster status visibility

A major scenario explored by the project is an unexpected staff cancellation.

### Example

```text
PCA becomes unavailable
        |
        v
Scheduled shift becomes UNFILLED
        |
        v
Rostering service processes the change
        |
        v
Eligible replacement workers identified
        |
        v
Check:
- role
- availability
- qualification requirements
- facility
- existing roster conflicts
        |
        v
Suitable workers notified
        |
        v
Worker accepts shift
        |
        v
Shift assignment updated
        |
        v
Facility roster reflects new coverage
```

This workflow will later provide a practical use case for event-driven cloud architecture.

---

## 3. Security

Aged care systems contain sensitive resident and workforce information.

The platform will therefore progressively implement:

- Authentication
- Role-Based Access Control (RBAC)
- Least-privilege access
- Secure secret management
- Encryption
- Audit logging
- API validation
- Secure cloud configuration
- Vulnerability and dependency scanning

Different roles will have different permissions.

For example, an administrative employee may require access to resident contact and appointment information but should not automatically receive detailed clinical information.

---

## 4. Platform Reliability

The application is also designed as a practical environment for learning and demonstrating Site Reliability Engineering.

Reliability capabilities will progressively include:

- Application health checks
- Database health checks
- Structured logging
- Application metrics
- Infrastructure metrics
- Monitoring dashboards
- Alerting
- Service Level Indicators (SLIs)
- Service Level Objectives (SLOs)
- Incident response
- Operational runbooks
- Root Cause Analysis (RCA)
- Backup and restore
- Disaster recovery
- Failure simulation
- Recovery testing

---

# Primary Users

The platform will eventually provide role-specific capabilities rather than exposing the same information and actions to every user.

## Care Worker / Personal Care Assistant

Potential capabilities include:

- View assigned shifts
- View permitted resident information
- Record authorised care information
- View available replacement shifts
- Respond to replacement shift requests

## Nurse / Doctor

Potential capabilities include:

- View appointments
- Access authorised resident records
- Access relevant reports and documents
- Record permitted clinical information
- Manage appropriate care documentation

## Reception / Administration

Potential capabilities include:

- Register residents
- Maintain administrative resident information
- Manage appointments
- View doctor or staff availability
- View appointment status
- View permitted payment or booking information

Administrative access will be separated from unnecessary clinical access.

## Roster Coordinator / Manager

Potential capabilities include:

- Create and manage shifts
- Assign workers
- View facility staffing coverage
- Identify unfilled shifts
- Review staff availability
- Identify eligible replacement workers
- Monitor shift acceptance
- Manage workforce continuity

---

# Multi-Site Scenario

The target architecture assumes an aged care organisation may operate multiple facilities.

```text
Facility A --------\
Facility B ---------+------ Secure Aged Care Cloud Platform
Facility C --------/                     |
                                          |
                             ---------------------------
                             |            |            |
                        Resident       Workforce    Platform
                        Services       Rostering   Operations
```

The objective is to provide centrally managed services while maintaining appropriate facility and role-based access controls.

---

# Target System Architecture

The architecture will evolve as the project progresses.

```text
                         USERS
                           |
                         HTTPS
                           |
                           v
                    API / Entry Layer
                           |
                           v
                     Load Balancer
                           |
                           v
                   FastAPI Application
                           |
          -------------------------------------
          |                  |                |
          v                  v                v
 Resident Services    Rostering Services   Operational
                                           Services
          |                  |
          |                  v
          |             Event Queue
          |                  |
          |                  v
          |           Matching Worker
          |                  |
          --------------------
                   |
                   v
               PostgreSQL
                   |
        -------------------------
        |                       |
        v                       v
 Object Storage             Monitoring
Reports/Documents          Logs & Metrics
                                |
                                v
                         Alerts / Dashboards
```

Future cloud infrastructure will introduce managed services where appropriate.

---

# Event-Driven Rostering

The replacement-worker workflow provides a practical scenario for asynchronous processing.

Instead of forcing an API request to perform every operation synchronously:

```text
Unfilled Shift
      |
      v
Staffing Event
      |
      v
Message Queue
      |
      v
Matching Worker
      |
      v
Eligible Staff
      |
      v
Notification
```

This architecture will allow the project to explore:

- Message queues
- Asynchronous processing
- Retry strategies
- Dead-letter queues
- Idempotency
- Failure handling
- Service decoupling
- Queue monitoring

---

# Reliability Scenario

The project will deliberately simulate failures rather than demonstrating only successful requests.

Example:

```text
Unfilled shift created
        |
        v
Event added to queue
        |
        v
Matching worker fails
        |
        v
Queue backlog increases
        |
        v
Monitoring detects abnormal behaviour
        |
        v
Alert generated
        |
        v
Engineer follows runbook
        |
        v
Worker restored
        |
        v
Pending events processed
        |
        v
Incident documented
        |
        v
Root Cause Analysis completed
```

This scenario provides a practical environment for demonstrating SRE and incident-management concepts.

---

# DevOps Strategy

Application changes will eventually follow an automated delivery workflow.

```text
Developer
    |
    v
Git / GitHub
    |
    v
Pull Request
    |
    v
Automated Tests
    |
    v
Security Scanning
    |
    v
Container Build
    |
    v
Container Security Scan
    |
    v
Deployment
    |
    v
Health Validation
    |
    v
Monitoring
```

The objective is to reduce manual deployment risk and make releases repeatable.

---

# Infrastructure as Code

Cloud infrastructure will be defined using Infrastructure as Code rather than relying entirely on manually created resources.

Terraform is planned for provisioning components such as:

- Networking
- Compute
- Managed databases
- Load balancing
- Storage
- IAM resources
- Monitoring resources
- Security configuration

This allows infrastructure changes to be version controlled and reviewed alongside application changes.

---

# Observability

The platform will progressively implement the three major observability signals:

### Metrics

Used to understand system behaviour such as:

- Request volume
- Response latency
- Error rates
- CPU and memory utilisation
- Database performance
- Queue depth
- Failed staffing events

### Logs

Used for investigation and troubleshooting.

### Traces

May be introduced later to follow requests across multiple application components.

Planned observability technologies include tools such as:

- Prometheus
- Grafana
- Cloud-native monitoring services
- Centralised logging

---

# Example Reliability Targets

Future SLO exercises may define targets such as:

```text
Roster API availability:
99.9%

Resident API availability:
99.9%

Unfilled shift event processing:
95% within defined processing threshold

Database request latency:
p95 within defined application target
```

These values will be refined after the relevant services exist and measurable baseline data is available.

---

# Data Domains

The initial data model is expected to grow around the following entities:

```text
Facility
   |
   +---- Residents
   |
   +---- Shifts
           |
           +---- Shift Assignments

Staff
   |
   +---- Role
   +---- Availability
   +---- Qualifications
   +---- Shift Assignments

Resident
   |
   +---- Appointments
   +---- Care Records
   +---- Reports
   +---- Documents
```

The database design will be implemented incrementally rather than creating the entire schema before the corresponding application functionality exists.

---

# Technology Stack

## Backend

Planned/core technologies:

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL

## DevOps

Planned technologies:

- Git
- GitHub
- GitHub Actions
- Docker
- Container security scanning

## Cloud & Infrastructure

Planned technologies include:

- AWS or Azure
- Terraform
- Managed PostgreSQL
- Object storage
- Load balancing
- IAM
- Secret management
- Message/event services

The final cloud service selection will be documented through architecture decisions rather than choosing services solely for technology coverage.

## Reliability & Monitoring

Planned technologies:

- Prometheus
- Grafana
- Cloud monitoring
- Structured logging
- Alerting
- Health checks
- Runbooks
- Incident reports

## Container Orchestration

Kubernetes will be introduced only when the application architecture provides a meaningful reason to demonstrate orchestration, scaling, health probes, deployment strategies, and recovery.

---

# Engineering Principles

## Incremental Development

The platform will be built in small, testable features.

## Stable Components

Adding a new feature should not require unrelated working components to be rewritten.

## Regression Protection

Existing functionality must continue working when new functionality is introduced.

## Clear Change Boundaries

Each development task will define:

- Files expected to change
- Components that should remain unchanged
- Acceptance criteria
- Regression checks
- Documentation requirements

## Secure by Design

Security controls will be introduced as architectural requirements rather than treated as a final project step.

## Observable by Design

Services should provide enough health, logging, and metric information to understand their behaviour in production-like environments.

## Failure Is Expected

The platform will be tested under failure scenarios rather than assuming every dependency is permanently available.

---

# Development Roadmap

## Phase 1 — Foundation

- [ ] Define project requirements
- [ ] Define user roles
- [ ] Define core workflows
- [ ] Design high-level architecture
- [ ] Define initial data model
- [ ] Establish repository structure

## Phase 2 — Backend Foundation

- [ ] Create FastAPI application
- [ ] Add health endpoints
- [ ] Configure environment management
- [ ] Add automated backend tests

## Phase 3 — Database

- [ ] Configure PostgreSQL
- [ ] Configure SQLAlchemy
- [ ] Introduce database migrations
- [ ] Add database health checks

## Phase 4 — Resident Operations

- [ ] Resident model
- [ ] Resident schemas
- [ ] Resident CRUD API
- [ ] Validation
- [ ] Resident API tests

## Phase 5 — Workforce Foundation

- [ ] Facility model
- [ ] Staff model
- [ ] Staff roles
- [ ] Availability
- [ ] Qualifications

## Phase 6 — Rostering

- [ ] Shift model
- [ ] Shift assignments
- [ ] Roster API
- [ ] Unfilled shift detection
- [ ] Conflict validation

## Phase 7 — Staffing Continuity

- [ ] Replacement-worker matching
- [ ] Staffing events
- [ ] Event queue
- [ ] Asynchronous worker
- [ ] Notifications
- [ ] Retry handling
- [ ] Failure handling

## Phase 8 — Authentication & Security

- [ ] Authentication
- [ ] Role-Based Access Control
- [ ] Least-privilege API access
- [ ] Audit logging
- [ ] Secret management
- [ ] Security scanning

## Phase 9 — Containers

- [ ] Dockerise API
- [ ] Containerise supporting services
- [ ] Add container health checks
- [ ] Add container security scanning

## Phase 10 — CI/CD

- [ ] Automated tests
- [ ] Security checks
- [ ] Container build
- [ ] Deployment pipeline
- [ ] Deployment validation
- [ ] Rollback strategy

## Phase 11 — Cloud Infrastructure

- [ ] Network architecture
- [ ] Managed database
- [ ] Compute
- [ ] Load balancing
- [ ] Object storage
- [ ] IAM
- [ ] Secrets
- [ ] Infrastructure as Code

## Phase 12 — Observability

- [ ] Structured logging
- [ ] Metrics
- [ ] Prometheus
- [ ] Grafana dashboards
- [ ] Cloud monitoring
- [ ] Alerts

## Phase 13 — Reliability Engineering

- [ ] Define SLIs
- [ ] Define SLOs
- [ ] Create operational runbooks
- [ ] Simulate service failures
- [ ] Simulate database failures
- [ ] Simulate worker/queue failures
- [ ] Create incident reports
- [ ] Perform Root Cause Analysis

## Phase 14 — Resilience & Disaster Recovery

- [ ] Automated backups
- [ ] Restore testing
- [ ] Define RPO
- [ ] Define RTO
- [ ] Disaster recovery design
- [ ] Recovery exercise

---

# Repository Structure

The planned repository structure is:

```text
secure-aged-care-cloud-platform/
|
+-- api/
|   +-- application backend
|
+-- architecture/
|   +-- system architecture
|   +-- data models
|   +-- architecture decisions
|
+-- database/
|   +-- database-related resources
|
+-- documentation/
|   +-- requirements
|   +-- user roles
|   +-- workflows
|
+-- incident-reports/
|   +-- simulated and test incident reports
|
+-- kubernetes/
|   +-- orchestration configuration
|
+-- monitoring/
|   +-- monitoring configuration and dashboards
|
+-- runbooks/
|   +-- operational recovery procedures
|
+-- scripts/
|   +-- operational and automation scripts
|
+-- security/
|   +-- security configuration and documentation
|
+-- terraform/
|   +-- cloud infrastructure
|
+-- .github/workflows/
|   +-- CI/CD workflows
|
+-- README.md
```

The structure will evolve only when implementation requirements justify additional components.

---

# Project Status

**Current stage:** Project foundation and architecture definition.

The repository is being rebuilt from a clean baseline around the Secure Aged Care Cloud Platform problem statement.

Implementation will proceed incrementally, with each completed phase tested and documented before the next major capability is introduced.

---

# Portfolio Goal

This project is intended to demonstrate the ability to connect technical engineering decisions with a realistic operational problem.

The completed platform should provide practical examples for discussing:

- Backend architecture
- REST APIs
- Relational databases
- Cloud architecture
- Infrastructure as Code
- CI/CD
- Containers
- Kubernetes
- Event-driven systems
- IAM and RBAC
- Secrets management
- Monitoring and observability
- SLI/SLO design
- Incident response
- Root Cause Analysis
- Backup and disaster recovery
- Reliability engineering

The goal is not simply to demonstrate that individual technologies were used, but to explain **why they were introduced, what problem they solve, how they interact, and how the platform behaves when something fails.**