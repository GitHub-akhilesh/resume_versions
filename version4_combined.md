# Resume Version 4: Software Engineer (Generalist)
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Software engineer building distributed systems for national e-governance and FinTech platforms — microservice architecture, transaction-critical APIs, event-driven pipelines. Currently 2 million+ users and 500,000+ transactions a day across Java/Spring Boot, Python/FastAPI and Node.js services. Hired and onboarded 4 engineers and moved the team onto Docker-based CI/CD. Most useful when a system is either growing faster than its design or falling over under load.

## 2. Technical Skills
* **Languages:** Java, Python, JavaScript (ES6+), TypeScript, SQL, C++, HTML5, CSS3
* **Backend & Architecture:** Spring Boot, Django, FastAPI, Node.js, Express.js, React.js, Next.js, microservices, REST APIs, WebSockets
* **Data & Messaging:** MySQL, PostgreSQL, MongoDB, Redis, Apache Kafka, Celery, Hibernate/JPA, indexing & query tuning
* **DevOps & Observability:** Docker, Git, GitHub Actions, CI/CD, Linux, Postman, Jira, Prometheus, Grafana

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present | New Delhi, India*
* Split monolithic backends into distributed microservices across **Spring Boot**, **FastAPI** and **Node.js**, serving **2 million+ users**.
* Built the transaction-critical endpoints for AEPS, MATM and UPI, sustaining **500,000+ daily transactions**.
* Cut unauthorized access attempts **99.9%** with **JWT**, **RBAC**, device binding and OTP controls.
* Reduced read/write latency **45%** across **MySQL**, **PostgreSQL** and **MongoDB** using sharding, partitioning and query tuning.
* Lifted message throughput **35%** by moving inter-service work onto **Apache Kafka**, **Celery** and **Redis**.
* Stood up **Prometheus** and **Grafana** dashboards and automated container delivery for all **3** payment platforms with **Docker** and **GitHub Actions**.
* Hired and onboarded **4 engineers**, improving team onboarding efficiency **40%**.

### Freelance Software Engineer
**Workforce Telemetry & Operations**
*06/2023 – 11/2023 | Remote, India*
* Engineered a workforce telemetry platform — **React.js** front end, **FastAPI** backend — for **1,000+ field agents**.
* Processed **10,000+ concurrent** GPS pings at **99.9% uptime** through a **FastAPI**, **Celery** and **Redis** ingestion pipeline.
* Built the live map dashboard in **React.js** with **Ant Design**, **30%** quicker to load.

## 4. Projects
### Transaction Orchestration & Ledger Platform
*Stack: Spring Boot / FastAPI / Kafka / PostgreSQL / Redis*
Microservice platform orchestrating AEPS, MATM, and UPI settlement with a transactional wallet ledger, retry and reconciliation handling, and Kafka event fan-out.

### MERN FinTech & Commerce Suite
*Stack: React.js / Node.js / Express.js / MongoDB / JWT / Redux*
Full-stack applications with JWT-secured authentication, role-based admin dashboards, and versioned REST APIs on React, Express, and MongoDB.

### Real-Time Telemetry & Geofencing Engine
*Stack: React.js / FastAPI / Celery / Redis / PostgreSQL*
Workforce geolocation engine ingesting asynchronous GPS streams, rendering live map visualizations, and pushing geofence alerts over WebSockets.

### Enterprise Authentication & Authorization Service
*Stack: Spring Boot / Spring Security / JWT / MySQL*
Reusable auth service providing registration, password hashing, JWT issuance and rotation, and RBAC enforcement across protected REST routes.

## 5. Education
### Bachelor of Technology (B.Tech.)
**Kanpur Institute of Technology** | *Kanpur, UP*
*07/2019 – 05/2023*

## 6. Certifications
* Data Structures & Algorithms Certification
* Database Systems & SQL Certification
* Advanced MERN Stack Developer Certification
* IIT Kanpur Cyber Security Certification

## 7. Achievements
* Graduated with First Class Honors, maintaining top academic rank.
* Earned a 4-Star Gold Badge in SQL on HackerRank.

## 8. ATS Score Estimate
* **95/100** — keyword coverage is concentrated on a single stack, so role-matched screens score higher and nothing dilutes the match.

## 9. Missing Skills Recommendations
* Add a system design artifact: a short architecture write-up or diagram for the transaction platform.
* Mention SLOs, error budgets, and on-call/incident response practice alongside Prometheus and Grafana.
* Add infrastructure-as-code exposure (Terraform or Helm) to strengthen the platform story.

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
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{Software Development Engineer | Microservices $\cdot$ Distributed Systems $\cdot$ Full Stack}}} \\
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
Software engineer building distributed systems for national e-governance and FinTech platforms --- microservice architecture, transaction-critical APIs, event-driven pipelines. Currently 2 million+ users and 500,000+ transactions a day across Java/Spring Boot, Python/FastAPI and Node.js services. Hired and onboarded 4 engineers and moved the team onto Docker-based CI/CD. Most useful when a system is either growing faster than its design or falling over under load.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Split monolithic backends into distributed microservices across \textbf{Spring Boot}, \textbf{FastAPI} and \textbf{Node.js}, serving \textbf{2 million+ users}.
    \item Built the transaction-critical endpoints for AEPS, MATM and UPI, sustaining \textbf{500,000+ daily transactions}.
    \item Cut unauthorized access attempts \textbf{99.9\%} with \textbf{JWT}, \textbf{RBAC}, device binding and OTP controls.
    \item Reduced read/write latency \textbf{45\%} across \textbf{MySQL}, \textbf{PostgreSQL} and \textbf{MongoDB} using sharding, partitioning and query tuning.
    \item Lifted message throughput \textbf{35\%} by moving inter-service work onto \textbf{Apache Kafka}, \textbf{Celery} and \textbf{Redis}.
    \item Stood up \textbf{Prometheus} and \textbf{Grafana} dashboards and automated container delivery for all \textbf{3} payment platforms with \textbf{Docker} and \textbf{GitHub Actions}.
    \item Hired and onboarded \textbf{4 engineers}, improving team onboarding efficiency \textbf{40\%}.
\end{itemize}

\vspace{4pt}
{\textbf{Freelance Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Workforce Telemetry \& Operations}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Engineered a workforce telemetry platform --- \textbf{React.js} front end, \textbf{FastAPI} backend --- for \textbf{1,000+ field agents}.
    \item Processed \textbf{10,000+ concurrent} GPS pings at \textbf{99.9\% uptime} through a \textbf{FastAPI}, \textbf{Celery} and \textbf{Redis} ingestion pipeline.
    \item Built the live map dashboard in \textbf{React.js} with \textbf{Ant Design}, \textbf{30\%} quicker to load.
\end{itemize}

\resumesection{Projects}
{\textbf{Transaction Orchestration \& Ledger Platform}} \\
{\small Microservice platform orchestrating AEPS, MATM, and UPI settlement with a transactional wallet ledger, retry and reconciliation handling, and Kafka event fan-out.} \\
{\footnotesize\textbf{STACK:} Spring Boot / FastAPI / Kafka / PostgreSQL / Redis}

\vspace{4pt}
{\textbf{MERN FinTech \& Commerce Suite}} \\
{\small Full-stack applications with JWT-secured authentication, role-based admin dashboards, and versioned REST APIs on React, Express, and MongoDB.} \\
{\footnotesize\textbf{STACK:} React.js / Node.js / Express.js / MongoDB / JWT / Redux}

\vspace{4pt}
{\textbf{Real-Time Telemetry \& Geofencing Engine}} \\
{\small Workforce geolocation engine ingesting asynchronous GPS streams, rendering live map visualizations, and pushing geofence alerts over WebSockets.} \\
{\footnotesize\textbf{STACK:} React.js / FastAPI / Celery / Redis / PostgreSQL}

\vspace{4pt}
{\textbf{Enterprise Authentication \& Authorization Service}} \\
{\small Reusable auth service providing registration, password hashing, JWT issuance and rotation, and RBAC enforcement across protected REST routes.} \\
{\footnotesize\textbf{STACK:} Spring Boot / Spring Security / JWT / MySQL}

\resumesection{Skills}
\textbf{Languages:} Java, Python, JavaScript (ES6+), TypeScript, SQL, C++, HTML5, CSS3 \\
\textbf{Backend \& Architecture:} Spring Boot, Django, FastAPI, Node.js, Express.js, React.js, Next.js, microservices, REST APIs, WebSockets \\
\textbf{Data \& Messaging:} MySQL, PostgreSQL, MongoDB, Redis, Apache Kafka, Celery, Hibernate/JPA, indexing \& query tuning \\
\textbf{DevOps \& Observability:} Docker, Git, GitHub Actions, CI/CD, Linux, Postman, Jira, Prometheus, Grafana

\resumesection{Education}
{\textbf{Bachelor of Technology (B.Tech.)}} \\
{\textbf{\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~07/2019 -- 05/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Kanpur, UP}

\resumesection{Certifications}
Data Structures \& Algorithms Certification \quad | \quad Database Systems \& SQL Certification \\
Advanced MERN Stack Developer Certification \quad | \quad IIT Kanpur Cyber Security Certification

\resumesection{Achievements}
\begin{itemize}
    \item Graduated with First Class Honors, maintaining top academic rank.
    \item Earned a 4-Star Gold Badge in SQL on HackerRank.
\end{itemize}

\end{document}
```
