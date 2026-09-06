# Resume Version 3: Python Full Stack Developer
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Python backend engineer, 3+ years on services clearing 500,000+ transactions a day for 2 million+ users, served by Django REST Framework and async FastAPI services. Took transaction query p95 down 45% by partitioning and indexing PostgreSQL, cleared 35% of the peak backlog onto Celery and Redis workers, and streams live status over WebSockets in under 500ms. Reads the query plan before adding the index.

## 2. Technical Skills
* **Core Python:** Python, Django, Django REST Framework, FastAPI, Flask, Celery, SQLAlchemy, Alembic, asyncio
* **APIs & Security:** RESTful APIs, OpenAPI/Swagger, JWT, OAuth 2.0, RBAC, rate limiting, idempotency keys, FastAPI WebSockets, API versioning
* **Data & Messaging:** PostgreSQL, MySQL, Redis, Celery queues, covering indexes, partitioning, query plan analysis
* **Testing & DevOps:** pytest, Docker, Kubernetes, GitHub Actions CI/CD, Linux, Postman, Prometheus, Grafana, React.js, JavaScript (ES6+)

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. --- India's national digital services platform, 2M+ users**
*12/2023 – Present | New Delhi, India*
* Scaled AEPS, MATM and VATM orchestration to **500,000+ daily transactions** at a **99% success rate**, by making the **Django REST Framework** payment path idempotent with request keys, backoff retries and nightly reconciliation.
* Took transaction query p95 down **45%** across **PostgreSQL** and **MySQL**, by partitioning the hot tables and adding covering indexes chosen from the query plan.
* Cleared **35%** of the peak-traffic backlog, by moving slow work off the request path onto **Celery** workers with **Redis** broking and idempotent task retries.
* Delivered live transaction status in under **500ms**, by streaming updates over **FastAPI WebSockets** instead of client polling.
* Contained a bad release to one service instead of the whole portal for **2 million+ users**, by moving monolithic web services onto async **FastAPI** and **Django** microservices behind a versioned REST gateway.
* Cut authentication latency **50%**, by issuing **JWT** access/refresh pairs with **RBAC** claims and caching OTP verification state in **Redis**.

### Software Engineer
**Contract engagement --- field-workforce logistics, 1,000+ agents**
*06/2023 – 11/2023 | Remote, India*
* Built a workforce telemetry and geofencing system for **1,000+ field agents** end to end, on **FastAPI** and async **SQLAlchemy** with **Alembic** migrations.
* Held **99.9% uptime** while absorbing **10,000+ concurrent** location pings, by batching writes through a **Celery** and **Redis** ingestion pipeline.
* Brought dashboard load time down **30%**, by wiring the **React.js** telemetry view to **FastAPI WebSocket** endpoints instead of polling.

## 4. Projects
### DigiPay API Platform
*Stack: Python / FastAPI / PostgreSQL / Docker / GitHub Actions*
FastAPI service with versioned routers, correlation-ID request tracing, auth and rate-limit middleware and a documented deprecation policy, packaged with Docker and a CI pipeline. github.com/GitHub-akhilesh/Django_apis_digipay

### Polyglot Task Microservices
*Stack: Python / Django / Flask / FastAPI / Docker / Kubernetes*
Django REST API, Flask utility service and FastAPI notification service running side by side under Docker Compose with Kubernetes manifests, fronted by a React web client. github.com/GitHub-akhilesh/To-do-list-app

### Facial Recognition Attendance System
*Stack: Python / OpenCV / Pandas / Tkinter / MySQL*
Automated attendance capture in Python using OpenCV Haar Cascade and LBPH recognition, with MySQL persistence and Pandas-generated Excel reports. github.com/GitHub-akhilesh/automatic-attendance-through-face-detection

### Async Telemetry Ingestion & Reporting Service
*Stack: Python / FastAPI / Celery / Redis / PostgreSQL / Pandas*
FastAPI ingestion service with Celery and Redis task queues writing to partitioned PostgreSQL tables, plus Pandas reporting jobs over aggregated telemetry.

## 5. Education
### Bachelor of Technology (B.Tech.)
**Kanpur Institute of Technology** | *Kanpur, UP*
*07/2019 – 05/2023*

## 6. Certifications
* IIT Kanpur Cyber Security Certification

## 7. Achievements
* HackerRank 4-Star Gold badge in SQL.

## 8. ATS Score Estimate
* **95/100** — keyword coverage is concentrated on a single stack, so role-matched screens score higher and nothing dilutes the match.

## 9. Missing Skills Recommendations
* Add testing depth with pytest, pytest-asyncio, and factory fixtures for DRF/FastAPI endpoints.
* Mention Celery observability (Flower, task retries, dead-letter handling) and worker autoscaling.
* Add type safety and validation specifics: mypy, Pydantic models, and schema versioning.

## 10. Complete LaTeX Resume Code
```latex
\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.45in]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{fontawesome5}
\usepackage{enumitem}

\definecolor{primaryblue}{HTML}{0c4f6b}
\definecolor{darkgray}{HTML}{333333}

\hypersetup{colorlinks=true, linkcolor=primaryblue, urlcolor=primaryblue}

\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}

\newcommand{\resumesection}[1]{%
  \vspace{6pt}%
  {\fontfamily{phv}\selectfont\textbf{\large\MakeUppercase{#1}}}%
  \vspace{2pt}%
  \hrule%
  \vspace{4pt}%
}

\setlist[itemize]{leftmargin=*,noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt,label=\textbullet}

\begin{document}

\begin{center}
    {\fontfamily{phv}\selectfont\textbf{\Huge AKHILESH KUMAR MISHRA}} \\
    \vspace{3pt}
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{Python Full Stack Developer | Django $\cdot$ FastAPI $\cdot$ REST APIs}}} \\
    \vspace{4pt}
    {\small
    \textcolor{primaryblue}{\faPhone*}~+91 88580 45785 \quad | \quad
    \href{mailto:makhileshkumar1@gmail.com}{\textcolor{primaryblue}{\faEnvelope}~makhileshkumar1@gmail.com} \quad | \quad
    \href{https://linkedin.com/in/akhilesh-kumar-mishra-a46030231}{\textcolor{primaryblue}{\faLinkedin}~linkedin.com/in/akhilesh-kumar-mishra} \quad | \quad
    \href{https://github.com/GitHub-akhilesh}{\textcolor{primaryblue}{\faGithub}~github.com/GitHub-akhilesh}
    }
\end{center}
\vspace{-10pt}

\resumesection{Summary}
Python backend engineer, 3+ years on services clearing 500,000+ transactions a day for 2 million+ users, served by Django REST Framework and async FastAPI services. Took transaction query p95 down 45\% by partitioning and indexing PostgreSQL, cleared 35\% of the peak backlog onto Celery and Redis workers, and streams live status over WebSockets in under 500ms. Reads the query plan before adding the index.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. --- India's national digital services platform, 2M+ users}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Scaled AEPS, MATM and VATM orchestration to \textbf{500,000+ daily transactions} at a \textbf{99\% success rate}, by making the \textbf{Django REST Framework} payment path idempotent with request keys, backoff retries and nightly reconciliation.
    \item Took transaction query p95 down \textbf{45\%} across \textbf{PostgreSQL} and \textbf{MySQL}, by partitioning the hot tables and adding covering indexes chosen from the query plan.
    \item Cleared \textbf{35\%} of the peak-traffic backlog, by moving slow work off the request path onto \textbf{Celery} workers with \textbf{Redis} broking and idempotent task retries.
    \item Delivered live transaction status in under \textbf{500ms}, by streaming updates over \textbf{FastAPI WebSockets} instead of client polling.
    \item Contained a bad release to one service instead of the whole portal for \textbf{2 million+ users}, by moving monolithic web services onto async \textbf{FastAPI} and \textbf{Django} microservices behind a versioned REST gateway.
    \item Cut authentication latency \textbf{50\%}, by issuing \textbf{JWT} access/refresh pairs with \textbf{RBAC} claims and caching OTP verification state in \textbf{Redis}.
\end{itemize}

\vspace{4pt}
{\textbf{Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Contract engagement --- field-workforce logistics, 1,000+ agents}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Built a workforce telemetry and geofencing system for \textbf{1,000+ field agents} end to end, on \textbf{FastAPI} and async \textbf{SQLAlchemy} with \textbf{Alembic} migrations.
    \item Held \textbf{99.9\% uptime} while absorbing \textbf{10,000+ concurrent} location pings, by batching writes through a \textbf{Celery} and \textbf{Redis} ingestion pipeline.
    \item Brought dashboard load time down \textbf{30\%}, by wiring the \textbf{React.js} telemetry view to \textbf{FastAPI WebSocket} endpoints instead of polling.
\end{itemize}

\resumesection{Projects}
{\textbf{DigiPay API Platform}} \\
{\small FastAPI service with versioned routers, correlation-ID request tracing, auth and rate-limit middleware and a documented deprecation policy, packaged with Docker and a CI pipeline. github.com/GitHub-akhilesh/Django\_apis\_digipay} \\
{\footnotesize\textbf{STACK:} Python / FastAPI / PostgreSQL / Docker / GitHub Actions}

\vspace{4pt}
{\textbf{Polyglot Task Microservices}} \\
{\small Django REST API, Flask utility service and FastAPI notification service running side by side under Docker Compose with Kubernetes manifests, fronted by a React web client. github.com/GitHub-akhilesh/To-do-list-app} \\
{\footnotesize\textbf{STACK:} Python / Django / Flask / FastAPI / Docker / Kubernetes}

\vspace{4pt}
{\textbf{Facial Recognition Attendance System}} \\
{\small Automated attendance capture in Python using OpenCV Haar Cascade and LBPH recognition, with MySQL persistence and Pandas-generated Excel reports. github.com/GitHub-akhilesh/automatic-attendance-through-face-detection} \\
{\footnotesize\textbf{STACK:} Python / OpenCV / Pandas / Tkinter / MySQL}

\vspace{4pt}
{\textbf{Async Telemetry Ingestion \& Reporting Service}} \\
{\small FastAPI ingestion service with Celery and Redis task queues writing to partitioned PostgreSQL tables, plus Pandas reporting jobs over aggregated telemetry.} \\
{\footnotesize\textbf{STACK:} Python / FastAPI / Celery / Redis / PostgreSQL / Pandas}

\resumesection{Skills}
\textbf{Core Python:} Python, Django, Django REST Framework, FastAPI, Flask, Celery, SQLAlchemy, Alembic, asyncio \\
\textbf{APIs \& Security:} RESTful APIs, OpenAPI/Swagger, JWT, OAuth 2.0, RBAC, rate limiting, idempotency keys, FastAPI WebSockets, API versioning \\
\textbf{Data \& Messaging:} PostgreSQL, MySQL, Redis, Celery queues, covering indexes, partitioning, query plan analysis \\
\textbf{Testing \& DevOps:} pytest, Docker, Kubernetes, GitHub Actions CI/CD, Linux, Postman, Prometheus, Grafana, React.js, JavaScript (ES6+)

\resumesection{Education}
{\textbf{Bachelor of Technology (B.Tech.)}} \\
{\textbf{\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~07/2019 -- 05/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Kanpur, UP}

\resumesection{Certifications}
IIT Kanpur Cyber Security Certification \\


\resumesection{Achievements}
\begin{itemize}
    \item HackerRank 4-Star Gold badge in SQL.
\end{itemize}

\end{document}
```
