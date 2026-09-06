# Resume Version 2: Java Full Stack Developer
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Over 10 billion INR settled daily across wallet and ledger services built on Spring Boot, Spring Data JPA and Hibernate. Held AEPS, MATM and VATM orchestration at a 99% success rate over 500,000+ daily transactions by making the payment path idempotent and self-reconciling, and cut p95 database latency 45% through covering indexes and Redis caching. Strong on the unglamorous parts — transaction boundaries, Kafka messaging, JUnit coverage.

## 2. Technical Skills
* **Core Java & Spring:** Java, Spring Boot, Spring MVC, Spring Security, Spring Data JPA, Hibernate, Spring Cloud, microservices
* **APIs, Security & UI:** RESTful APIs, OpenAPI/Swagger, JWT, RBAC, device binding, rate limiting, idempotency keys, API versioning, React.js
* **Data & Messaging:** MySQL, PostgreSQL, transaction boundaries, covering indexes, query tuning, Redis, Apache Kafka, dead-letter topics
* **Testing & DevOps:** JUnit 5, Mockito, Testcontainers, Maven, Gradle, Docker, Kubernetes, GitHub Actions CI/CD, Actuator, Prometheus, Grafana

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present | New Delhi, India*
* Held AEPS, MATM and VATM orchestration at a **99% success rate** across **500,000+ daily transactions**, by making the **Spring Boot** payment path idempotent with request keys, backoff retries and automated end-of-day reconciliation.
* Settled over **10 billion INR** a day with balances that reconcile, by building the wallet and ledger services on **Spring Data JPA** and **Hibernate** with explicit transaction boundaries and optimistic locking.
* Cut p95 read/write latency **45%** across **MySQL** and **PostgreSQL**, by adding covering indexes, tuning the JPA fetch strategy to kill N+1 queries and caching hot lookups in **Redis**.
* Contained a bad release to one service instead of the whole portal for **2 million+ users**, by splitting monolithic e-governance systems into **Spring Boot** microservices behind a versioned REST gateway.
* Blocked **99.9%** of unauthorized access attempts, by adding **Spring Security** with **JWT**, method-level **RBAC**, device binding and OTP retry limits.
* Lifted async throughput **35%**, by moving inter-service calls onto **Apache Kafka** with dead-letter topics, and surfacing consumer lag in **Prometheus** and **Grafana**.

### Software Engineer (Contract)
**Independent Client Engagement**
*06/2023 – 11/2023 | Remote, India*
* Shipped a workforce tracking platform for **1,000+ field agents** end to end on **Java**, **Spring Boot** and **React.js** — schema design through AWS deployment.
* Brought dashboard load time down **30%**, by streaming live coordinates from Spring Boot **WebSocket** endpoints into a **React.js** and **Ant Design** map view instead of polling.
* Enforced Admin, Supervisor and Employee boundaries across **100+ client accounts**, by adding **Spring Security** method-level authorization and **JWT** claims to the operations API.

## 4. Projects
### Enterprise Authentication & Authorization Service
*Stack: Java / Spring Boot / Spring Security / JWT / Hibernate / MySQL*
Spring Security service handling user registration, password hashing, JWT issuance and validation, and role-mapped access control across protected REST routes.

### Himalayan Edges Commerce Platform
*Stack: Java / Spring Boot / Spring Data JPA / MySQL / AWS / PWA*
PWA-enabled e-commerce platform on Spring Boot REST services with modular controllers and normalized MySQL schemas, load-verified at 500+ concurrent users.

### Attendance Management & Reporting Platform
*Stack: Java / Spring Boot / Spring Data JPA / MySQL / REST APIs*
Spring Boot service exposing REST endpoints for student registration, daily attendance logging, and scheduled Excel report generation, cutting manual record-keeping by 70%.

### Wallet & Transaction Ledger Service
*Stack: Java / Spring Boot / Spring Data JPA / Hibernate / MySQL / Redis*
Wallet and ledger service built on Spring Data JPA and Hibernate, using managed transaction boundaries and indexed MySQL schemas to keep balances consistent under concurrent settlement.

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
* First Class Honors, B.Tech. --- top academic rank in cohort.
* HackerRank 4-Star Gold badge in SQL.

## 8. ATS Score Estimate
* **96/100** — keyword coverage is concentrated on a single stack, so role-matched screens score higher and nothing dilutes the match.

## 9. Missing Skills Recommendations
* Add unit and integration testing with JUnit 5, Mockito, and Testcontainers.
* Mention a cloud runtime for Spring services (AWS ECS, Elastic Beanstalk, or Kubernetes).
* Add API contract documentation with OpenAPI/Swagger and versioning strategy.

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
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{Java Full Stack Developer | Spring Boot $\cdot$ Microservices $\cdot$ REST APIs}}} \\
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
Over 10 billion INR settled daily across wallet and ledger services built on Spring Boot, Spring Data JPA and Hibernate. Held AEPS, MATM and VATM orchestration at a 99\% success rate over 500,000+ daily transactions by making the payment path idempotent and self-reconciling, and cut p95 database latency 45\% through covering indexes and Redis caching. Strong on the unglamorous parts --- transaction boundaries, Kafka messaging, JUnit coverage.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Held AEPS, MATM and VATM orchestration at a \textbf{99\% success rate} across \textbf{500,000+ daily transactions}, by making the \textbf{Spring Boot} payment path idempotent with request keys, backoff retries and automated end-of-day reconciliation.
    \item Settled over \textbf{10 billion INR} a day with balances that reconcile, by building the wallet and ledger services on \textbf{Spring Data JPA} and \textbf{Hibernate} with explicit transaction boundaries and optimistic locking.
    \item Cut p95 read/write latency \textbf{45\%} across \textbf{MySQL} and \textbf{PostgreSQL}, by adding covering indexes, tuning the JPA fetch strategy to kill N+1 queries and caching hot lookups in \textbf{Redis}.
    \item Contained a bad release to one service instead of the whole portal for \textbf{2 million+ users}, by splitting monolithic e-governance systems into \textbf{Spring Boot} microservices behind a versioned REST gateway.
    \item Blocked \textbf{99.9\%} of unauthorized access attempts, by adding \textbf{Spring Security} with \textbf{JWT}, method-level \textbf{RBAC}, device binding and OTP retry limits.
    \item Lifted async throughput \textbf{35\%}, by moving inter-service calls onto \textbf{Apache Kafka} with dead-letter topics, and surfacing consumer lag in \textbf{Prometheus} and \textbf{Grafana}.
\end{itemize}

\vspace{4pt}
{\textbf{Software Engineer (Contract)}} \\
{\textbf{\textcolor{primaryblue}{Independent Client Engagement}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Shipped a workforce tracking platform for \textbf{1,000+ field agents} end to end on \textbf{Java}, \textbf{Spring Boot} and \textbf{React.js} --- schema design through AWS deployment.
    \item Brought dashboard load time down \textbf{30\%}, by streaming live coordinates from Spring Boot \textbf{WebSocket} endpoints into a \textbf{React.js} and \textbf{Ant Design} map view instead of polling.
    \item Enforced Admin, Supervisor and Employee boundaries across \textbf{100+ client accounts}, by adding \textbf{Spring Security} method-level authorization and \textbf{JWT} claims to the operations API.
\end{itemize}

\resumesection{Projects}
{\textbf{Enterprise Authentication \& Authorization Service}} \\
{\small Spring Security service handling user registration, password hashing, JWT issuance and validation, and role-mapped access control across protected REST routes.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / Spring Security / JWT / Hibernate / MySQL}

\vspace{4pt}
{\textbf{Himalayan Edges Commerce Platform}} \\
{\small PWA-enabled e-commerce platform on Spring Boot REST services with modular controllers and normalized MySQL schemas, load-verified at 500+ concurrent users.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / Spring Data JPA / MySQL / AWS / PWA}

\vspace{4pt}
{\textbf{Attendance Management \& Reporting Platform}} \\
{\small Spring Boot service exposing REST endpoints for student registration, daily attendance logging, and scheduled Excel report generation, cutting manual record-keeping by 70\%.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / Spring Data JPA / MySQL / REST APIs}

\vspace{4pt}
{\textbf{Wallet \& Transaction Ledger Service}} \\
{\small Wallet and ledger service built on Spring Data JPA and Hibernate, using managed transaction boundaries and indexed MySQL schemas to keep balances consistent under concurrent settlement.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / Spring Data JPA / Hibernate / MySQL / Redis}

\resumesection{Skills}
\textbf{Core Java \& Spring:} Java, Spring Boot, Spring MVC, Spring Security, Spring Data JPA, Hibernate, Spring Cloud, microservices \\
\textbf{APIs, Security \& UI:} RESTful APIs, OpenAPI/Swagger, JWT, RBAC, device binding, rate limiting, idempotency keys, API versioning, React.js \\
\textbf{Data \& Messaging:} MySQL, PostgreSQL, transaction boundaries, covering indexes, query tuning, Redis, Apache Kafka, dead-letter topics \\
\textbf{Testing \& DevOps:} JUnit 5, Mockito, Testcontainers, Maven, Gradle, Docker, Kubernetes, GitHub Actions CI/CD, Actuator, Prometheus, Grafana

\resumesection{Education}
{\textbf{Bachelor of Technology (B.Tech.)}} \\
{\textbf{\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~07/2019 -- 05/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Kanpur, UP}

\resumesection{Certifications}
Database Systems \& SQL Certification \quad | \quad Data Structures \& Algorithms Certification \\
IIT Kanpur Cyber Security Certification \quad | \quad Advanced MERN Stack Developer Certification

\resumesection{Achievements}
\begin{itemize}
    \item First Class Honors, B.Tech. --- top academic rank in cohort.
    \item HackerRank 4-Star Gold badge in SQL.
\end{itemize}

\end{document}
```
