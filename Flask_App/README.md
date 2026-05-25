# Maintenance Management System

## Overview

This project is a database-driven maintenance management system developed using Python, Flask, and MySQL.

The system is designed to manage industrial machines, maintenance activities, downtime records, and maintenance analytics for manufacturing environments.

It demonstrates concepts related to:
- Industry 4.0
- Industrial digitalization
- Maintenance analytics
- Production IT systems
- Database-driven web applications

---

## Features

### Machine Management
- Add new machines
- Store machine location and status
- Track installation dates
- Delete machine records

### Maintenance Management
- Add maintenance logs
- Record issue descriptions
- Store technician information
- Track downtime duration
- Delete maintenance logs

### Analytics Dashboard
- Total machine count
- Total maintenance records
- Total downtime analysis
- Most problematic machine detection

---

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- SQL
- Jinja2 Templates

---

## Database Structure

### Machines Table

| Column | Description |
|---|---|
| machine_id | Primary key |
| machine_name | Machine name |
| location | Plant location |
| status | Machine status |
| install_date | Installation date |

### Maintenance Logs Table

| Column | Description |
|---|---|
| log_id | Primary key |
| machine_id | Foreign key |
| maintenance_date | Maintenance date |
| issue_description | Maintenance issue |
| technician_name | Technician name |
| downtime_minutes | Downtime duration |

---

## Project Structure

project4_maintenance_management_system/

├── Flask_App/

├── static/

├── templates/

├── venv/

├── requirements.txt

├── README.md

└── .gitignore

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository_link>
