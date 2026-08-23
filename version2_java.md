# Resume Version 2: Java Full Stack Developer
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Java full stack developer building secure, high-volume enterprise FinTech systems. Core stack is Spring Boot, Spring Security, Spring Data JPA and Hibernate over MySQL and PostgreSQL, with Kafka for anything that shouldn't block a request. Owns wallet and ledger services settling over 10 billion INR a day, and transaction orchestration holding a 99% success rate across 500,000+ daily transactions. Strong on the unglamorous parts — transaction boundaries, indexing, cache tuning.

## 2. Technical Skills
* **Core Java & Spring:** Java, Spring Boot, Spring MVC, Spring Security, Spring Data JPA, Hibernate, Spring Cloud, Microservices
* **APIs, Security & UI:** RESTful APIs, JWT authentication, RBAC, device binding, API versioning, React.js, JavaScript (ES6+), HTML5, CSS3
* **Data & Messaging:** MySQL, PostgreSQL, transaction management, indexing, query tuning, Redis, Apache Kafka
* **Build & DevOps:** Maven, Gradle, Git, GitHub, Docker, CI/CD, Postman, Spring Boot Actuator, Prometheus, Grafana

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present | New Delhi, India*
* Split monolithic e-governance systems into **Java** and **Spring Boot** microservices, improving release speed and fault isolation for **2 million+ users**.
* Ran AEPS, MATM and VATM transaction orchestration on **Spring Boot** at a **99% success rate** across **500,000+ daily transactions**.
* Cut unauthorized access attempts **99.9%** with **Spring Security**: **JWT**, **RBAC**, device binding and OTP retry limits.
* Built the wallet and ledger services on **Spring Data JPA** and **Hibernate** — over **10 billion INR** settled daily, and balances that reconcile.
* Dropped read/write latency **45%** across **MySQL** and **PostgreSQL** through indexing and cache tuning.
* Moved inter-service communication onto **Apache Kafka**, lifting async throughput **35%**.

### Freelance Software Engineer
**Workforce Telemetry & Operations**
*06/2023 – 11/2023 | Remote, India*
* Built a workforce tracking platform on **Java**, **Spring Boot** and **React.js** for **1,000+ field agents**.
* Streamed live coordinates from Spring Boot WebSocket endpoints into a **React.js** and **Ant Design** dashboard, **30%** quicker to load than the first cut.
* Enforced Admin, Supervisor and Employee boundaries on the operations API with **Spring Security** and **JWT** across **100+ client accounts**.

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
* Graduated with First Class Honors, maintaining top academic rank.
* Earned a 4-Star Gold Badge in SQL on HackerRank.

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
Java full stack developer building secure, high-volume enterprise FinTech systems. Core stack is Spring Boot, Spring Security, Spring Data JPA and Hibernate over MySQL and PostgreSQL, with Kafka for anything that shouldn't block a request. Owns wallet and ledger services settling over 10 billion INR a day, and transaction orchestration holding a 99\% success rate across 500,000+ daily transactions. Strong on the unglamorous parts --- transaction boundaries, indexing, cache tuning.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Split monolithic e-governance systems into \textbf{Java} and \textbf{Spring Boot} microservices, improving release speed and fault isolation for \textbf{2 million+ users}.
    \item Ran AEPS, MATM and VATM transaction orchestration on \textbf{Spring Boot} at a \textbf{99\% success rate} across \textbf{500,000+ daily transactions}.
    \item Cut unauthorized access attempts \textbf{99.9\%} with \textbf{Spring Security}: \textbf{JWT}, \textbf{RBAC}, device binding and OTP retry limits.
    \item Built the wallet and ledger services on \textbf{Spring Data JPA} and \textbf{Hibernate} --- over \textbf{10 billion INR} settled daily, and balances that reconcile.
    \item Dropped read/write latency \textbf{45\%} across \textbf{MySQL} and \textbf{PostgreSQL} through indexing and cache tuning.
    \item Moved inter-service communication onto \textbf{Apache Kafka}, lifting async throughput \textbf{35\%}.
\end{itemize}

\vspace{4pt}
{\textbf{Freelance Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Workforce Telemetry \& Operations}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Built a workforce tracking platform on \textbf{Java}, \textbf{Spring Boot} and \textbf{React.js} for \textbf{1,000+ field agents}.
    \item Streamed live coordinates from Spring Boot WebSocket endpoints into a \textbf{React.js} and \textbf{Ant Design} dashboard, \textbf{30\%} quicker to load than the first cut.
    \item Enforced Admin, Supervisor and Employee boundaries on the operations API with \textbf{Spring Security} and \textbf{JWT} across \textbf{100+ client accounts}.
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
\textbf{Core Java \& Spring:} Java, Spring Boot, Spring MVC, Spring Security, Spring Data JPA, Hibernate, Spring Cloud, Microservices \\
\textbf{APIs, Security \& UI:} RESTful APIs, JWT authentication, RBAC, device binding, API versioning, React.js, JavaScript (ES6+), HTML5, CSS3 \\
\textbf{Data \& Messaging:} MySQL, PostgreSQL, transaction management, indexing, query tuning, Redis, Apache Kafka \\
\textbf{Build \& DevOps:} Maven, Gradle, Git, GitHub, Docker, CI/CD, Postman, Spring Boot Actuator, Prometheus, Grafana

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
