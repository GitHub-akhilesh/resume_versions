# Resume Version 3: Python Full Stack Developer
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Python full stack developer focused on asynchronous backends for high-volume FinTech. Django and Django REST Framework where the domain is CRUD-heavy, FastAPI where latency matters, Celery and Redis for whatever belongs off the request path. Currently on services clearing 500,000+ transactions a day for 2 million+ users, streaming live status over WebSockets in under 500ms. Reads the query plan before adding the index.

## 2. Technical Skills
* **Core Python:** Python, Django, Django REST Framework, FastAPI, Celery, SQLAlchemy, asyncio
* **APIs & Security:** RESTful APIs, JWT authentication, OAuth, RBAC, FastAPI WebSockets, API versioning
* **Data & Messaging:** PostgreSQL, MySQL, SQLite, Redis, Celery queues, indexing, partitioning, query optimization
* **Tooling & Frontend:** Git, GitHub, Docker, Linux, Postman, CI/CD, React.js, JavaScript (ES6+), HTML5, CSS3

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present | New Delhi, India*
* Moved monolithic web services onto async **FastAPI** and **Django** microservices serving **2 million+ users**.
* Scaled AEPS, MATM and VATM orchestration on **Django REST Framework** to **500,000+ daily transactions** at a **99% success rate**.
* Cut authentication latency **50%** with **JWT**, **RBAC** and OTP verification.
* Pushed slow work off the request path with **Celery** and **Redis**, clearing **35%** of the backlog that showed up at peak traffic.
* Partitioned and indexed the **PostgreSQL** and **MySQL** schemas, taking transaction query latency down **45%**.
* Streamed live transaction status over **FastAPI WebSockets** — updates land in under **500ms**.

### Freelance Software Engineer
**Workforce Telemetry & Operations**
*06/2023 – 11/2023 | Remote, India*
* Built a workforce telemetry and geofencing system on **FastAPI** and async **SQLAlchemy** for **1,000+ field agents**.
* Held **99.9% uptime** on the GPS ingestion API while it absorbed **10,000+ concurrent** location pings.
* Wired the telemetry dashboard in **React.js** to FastAPI WebSocket endpoints, **30%** quicker to load.

## 4. Projects
### Facial Recognition Attendance System
*Stack: Python / OpenCV / Pandas / Tkinter / MySQL*
Automated attendance tracking in Python with OpenCV (Haar Cascade and LBPH) face recognition, MySQL persistence, and Pandas-generated Excel reports.

### Himalayan Edges Commerce Platform
*Stack: Python / Django / Django REST Framework / SQLite / AWS / PWA*
PWA-enabled e-commerce platform on Django and Django REST Framework, deployed to AWS, lifting page speed and client usage by 30%.

### Async Telemetry Ingestion & Reporting Service
*Stack: Python / FastAPI / Celery / Redis / PostgreSQL / Pandas*
FastAPI ingestion service with Celery and Redis task queues writing to partitioned PostgreSQL tables, plus Pandas reporting jobs over aggregated telemetry.

### Persistent Task Management Dashboard
*Stack: Python / Tkinter / JSON / MVC*
Python desktop utility for task planning, category filtering, and JSON persistence, structured on a clean MVC separation.

## 5. Education
### Bachelor of Technology (B.Tech.)
**Kanpur Institute of Technology** | *Kanpur, UP*
*07/2019 – 05/2023*

## 6. Certifications
* Database Systems & SQL Certification
* Data Structures & Algorithms Certification
* IIT Kanpur Cyber Security Certification
* Advanced MERN Stack Developer Certification

## 7. Achievements
* Graduated with First Class Honors, maintaining top academic rank.
* Earned a 4-Star Gold Badge in SQL on HackerRank.

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
Python full stack developer focused on asynchronous backends for high-volume FinTech. Django and Django REST Framework where the domain is CRUD-heavy, FastAPI where latency matters, Celery and Redis for whatever belongs off the request path. Currently on services clearing 500,000+ transactions a day for 2 million+ users, streaming live status over WebSockets in under 500ms. Reads the query plan before adding the index.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Moved monolithic web services onto async \textbf{FastAPI} and \textbf{Django} microservices serving \textbf{2 million+ users}.
    \item Scaled AEPS, MATM and VATM orchestration on \textbf{Django REST Framework} to \textbf{500,000+ daily transactions} at a \textbf{99\% success rate}.
    \item Cut authentication latency \textbf{50\%} with \textbf{JWT}, \textbf{RBAC} and OTP verification.
    \item Pushed slow work off the request path with \textbf{Celery} and \textbf{Redis}, clearing \textbf{35\%} of the backlog that showed up at peak traffic.
    \item Partitioned and indexed the \textbf{PostgreSQL} and \textbf{MySQL} schemas, taking transaction query latency down \textbf{45\%}.
    \item Streamed live transaction status over \textbf{FastAPI WebSockets} --- updates land in under \textbf{500ms}.
\end{itemize}

\vspace{4pt}
{\textbf{Freelance Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Workforce Telemetry \& Operations}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Built a workforce telemetry and geofencing system on \textbf{FastAPI} and async \textbf{SQLAlchemy} for \textbf{1,000+ field agents}.
    \item Held \textbf{99.9\% uptime} on the GPS ingestion API while it absorbed \textbf{10,000+ concurrent} location pings.
    \item Wired the telemetry dashboard in \textbf{React.js} to FastAPI WebSocket endpoints, \textbf{30\%} quicker to load.
\end{itemize}

\resumesection{Projects}
{\textbf{Facial Recognition Attendance System}} \\
{\small Automated attendance tracking in Python with OpenCV (Haar Cascade and LBPH) face recognition, MySQL persistence, and Pandas-generated Excel reports.} \\
{\footnotesize\textbf{STACK:} Python / OpenCV / Pandas / Tkinter / MySQL}

\vspace{4pt}
{\textbf{Himalayan Edges Commerce Platform}} \\
{\small PWA-enabled e-commerce platform on Django and Django REST Framework, deployed to AWS, lifting page speed and client usage by 30\%.} \\
{\footnotesize\textbf{STACK:} Python / Django / Django REST Framework / SQLite / AWS / PWA}

\vspace{4pt}
{\textbf{Async Telemetry Ingestion \& Reporting Service}} \\
{\small FastAPI ingestion service with Celery and Redis task queues writing to partitioned PostgreSQL tables, plus Pandas reporting jobs over aggregated telemetry.} \\
{\footnotesize\textbf{STACK:} Python / FastAPI / Celery / Redis / PostgreSQL / Pandas}

\vspace{4pt}
{\textbf{Persistent Task Management Dashboard}} \\
{\small Python desktop utility for task planning, category filtering, and JSON persistence, structured on a clean MVC separation.} \\
{\footnotesize\textbf{STACK:} Python / Tkinter / JSON / MVC}

\resumesection{Skills}
\textbf{Core Python:} Python, Django, Django REST Framework, FastAPI, Celery, SQLAlchemy, asyncio \\
\textbf{APIs \& Security:} RESTful APIs, JWT authentication, OAuth, RBAC, FastAPI WebSockets, API versioning \\
\textbf{Data \& Messaging:} PostgreSQL, MySQL, SQLite, Redis, Celery queues, indexing, partitioning, query optimization \\
\textbf{Tooling \& Frontend:} Git, GitHub, Docker, Linux, Postman, CI/CD, React.js, JavaScript (ES6+), HTML5, CSS3

\resumesection{Education}
{\textbf{Bachelor of Technology (B.Tech.)}} \\
{\textbf{\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~07/2019 -- 05/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Kanpur, UP}

\resumesection{Certifications}
Database Systems \& SQL Certification \quad | \quad Data Structures \& Algorithms Certification \\
IIT Kanpur Cyber Security Certification \quad | \quad Advanced MERN Stack Developer Certification

\resumesection{Achievements}
\begin{itemize}
    \item Graduated with First Class Honors, maintaining top academic rank.
    \item Earned a 4-Star Gold Badge in SQL on HackerRank.
\end{itemize}

\end{document}
```
