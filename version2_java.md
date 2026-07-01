# Resume Version 2: Java Full Stack Developer

## 1. Professional Summary
Software Development Engineer specializing in Java Full Stack development, with a track record of building secure, scalable enterprise FinTech and tracking platforms. Expert in Java, Spring Boot, Spring Security, Hibernate, Microservices, and database design using MySQL/PostgreSQL. Proven experience in re-architecting monoliths to high-performance microservices, designing transactional ledger platforms, and securing enterprise APIs with JWT/RBAC. Optimizes system latency and reduces failure rates through caching and containerized deployments.

## 2. Technical Skills
* **Backend:** Java, Spring Boot, Spring MVC, Spring Security, Spring Data JPA, Hibernate, Microservices
* **Frontend:** React.js, Angular, JavaScript, HTML, CSS, Bootstrap
* **Database:** MySQL, PostgreSQL
* **Tools:** Maven, Gradle, Git, GitHub, Postman, Docker

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present*
*E-Governance initiatives under the Ministry of Electronics & Information Technology*
* Re-architected monolithic e-governance systems into scalable **Java** and **Spring Boot** microservices, improving service reliability and deployment speed for 20 lakh+ users.
* Designed and scaled transaction orchestration services for AEPS, MATM, and VATM platforms using **Spring Boot**, handling 5 lakh+ daily transactions with a ~80% success rate.
* Secured enterprise APIs using **Spring Security** with **JWT Authentication** and Role-Based Access Control (**RBAC**), implementing device binding and OTP retry policies.
* Engineered high-performance wallet and ledger systems using **Spring Data JPA** and **Hibernate**, processing over ₹100 crore in daily transactions.
* Optimized database transactions and search queries in **MySQL** and **PostgreSQL** using indexing and cache tuning, reducing latency under peak loads.
* Established event-driven communication between microservices using Apache Kafka, enhancing asynchronous data processing speed.
* Configured system monitoring and observability using **Spring Boot Actuator**, **Prometheus**, and **Grafana**, ensuring high availability.
* Built automated CI/CD pipelines using **Maven**, **Git**, and **Docker**, accelerating testing and container deployment workflows.
* Led hiring and onboarding of 4 engineers, expanding technical team capacity and onboarding efficiency by 40%.

### Freelance Software Engineer
**Workforce Telemetry & Geofencing System**
*06/2023 – 11/2023*
*Real-Time Telemetry & Operations Platform*
* Created and developed a real-time workforce tracking application utilizing **Java**, **Spring Boot**, and **React.js**, serving **1,000+ active field agents**.
* Built a responsive map-based dashboard in **React.js** using **Ant Design** (antd), connecting via WebSockets to a Spring Boot backend for live coordinates.
* Implemented a secure backend API in Spring Boot using **Spring Security** and **JWT** to manage role-based dashboard access control (Admin, Supervisor, Employee).
* Utilized **Hibernate** and **Spring Data JPA** to manage and query location tracking logs, geofence violations, and route history.

## 4. Projects
### Himalayan Edges Website Development
*10/2024 – 11/2024*
* Created an e-commerce platform using **Spring Boot** and **React.js** with PWA capabilities, hosted on AWS, boosting speed and usage by 30%.
* Implemented role-based login authentication using Spring Security, securing credentials and accounts for 5,000+ users.
* Designed modular REST controllers and database schemas, verified with 500+ concurrent simulated users and a 20% cart conversion rate.
* Added Google Reviews integration to display user testimonials dynamically, increasing site conversions by 15%.

### Automatic Attendance System
*05/2024 – 07/2024*
* Created a student attendance system by linking a Python face detection script (OpenCV/LBPH) with a Spring Boot enterprise database.
* Developed a web administration dashboard in React to manage student registrations, log daily attendance, and export Excel reports, cutting manual tasks by 70%.

## 5. Education
### B.Tech.
**Kanpur Institute of Technology** | *Kanpur, UP*
*07/2019 – 05/2023*

## 6. Certifications
* GeeksforGeeks MERN Stack Certification
* Coding Ninjas DBMS Certification
* Coding Ninjas DSA Certification
* IIT Kanpur Prutor Cyber Security Certification

## 7. Achievements
* Graduated with First Class Honors, maintaining top academic rank.
* Earned a 4-Star Gold Badge in SQL on HackerRank.

## 8. ATS Score Estimate
* **93/100** - Highly optimized with core Java/Spring enterprise keywords. Strong metrics representation.

## 9. Missing Skills Recommendations
* Include experience with cloud services like AWS Elastic Beanstalk or AWS ECS.
* Mention unit testing with JUnit, Mockito, and integration tests.
* Mention enterprise messaging services like RabbitMQ or ActiveMQ.

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

\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    urlcolor=primaryblue,
}

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

\begin{center}
    {\fontfamily{phv}\selectfont\textbf{\Huge AKHILESH KUMAR MISHRA}} \\
    \vspace{3pt}
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{Java Full Stack Developer}}} \\
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
Software Development Engineer specializing in Java Full Stack development, with a track record of building secure, scalable enterprise FinTech and tracking platforms. Expert in Java, Spring Boot, Spring Security, Hibernate, Microservices, and database design using MySQL/PostgreSQL. Proven experience in re-architecting monoliths to high-performance microservices, designing transactional ledger platforms, and securing enterprise APIs with JWT/RBAC. Optimizes system latency and reduces failure rates through caching and containerized deployments.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Re-architected monolithic e-governance systems into scalable \textbf{Java} and \textbf{Spring Boot} microservices, improving service reliability and deployment speed for 20 lakh+ active users.
    \item Designed and scaled transaction orchestration services for AEPS, MATM, and VATM platforms using \textbf{Spring Boot}, handling 5 lakh+ daily transactions.
    \item Secured enterprise APIs using \textbf{Spring Security} with \textbf{JWT Authentication} and Role-Based Access Control (\textbf{RBAC}), implementing device binding.
    \item Engineered high-performance wallet and ledger systems using \textbf{Spring Data JPA} and \textbf{Hibernate}, processing over ₹100 crore in daily transactions.
    \item Optimized database transactions and search queries in \textbf{MySQL} and \textbf{PostgreSQL} using indexing and cache tuning.
    \item Established event-driven communication between microservices using Apache Kafka, enhancing asynchronous data processing speed.
\end{itemize}

\vspace{4pt}
{\textbf{Freelance Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Workforce Telemetry \& Operations}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Created and developed a real-time workforce tracking application utilizing \textbf{Java}, \textbf{Spring Boot}, and \textbf{React.js}.
    \item Built a responsive map-based dashboard in \textbf{React.js} using \textbf{Ant Design} (antd), connecting via WebSockets to a Spring Boot backend.
    \item Implemented a secure backend API in Spring Boot using \textbf{Spring Security} and \textbf{JWT} to manage role-based dashboard access control.
\end{itemize}

\resumesection{Projects}
{\textbf{Java Authentication \& Secure Login Portal}} \\
{\small Engineered a secure backend service featuring user registration, password hashing, JWT token generation, and secure routes mapping.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / Spring Security / JWT / Hibernate / MySQL}

\vspace{4pt}
{\textbf{Himalayan Edges Website Development}} \\
{\small Created an e-commerce platform using Spring Boot and React.js with PWA capabilities, hosted on AWS, boosting speed and usage by 30\%.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / React.js / MySQL / AWS / PWA}

\vspace{4pt}
{\textbf{Facial Recognition Attendance Dashboard}} \\
{\small Created a student attendance system by linking a Python face detection script (OpenCV) with a Spring Boot enterprise database backend.} \\
{\footnotesize\textbf{STACK:} Java / Spring Boot / Python / OpenCV / MySQL / React.js}

\vspace{4pt}
{\textbf{Traveling Portal \& Landing Page}} \\
{\small A fully responsive, modern front-end landing page for a travel agency built with HTML, CSS, and Bootstrap layouts.} \\
{\footnotesize\textbf{STACK:} HTML5 / CSS3 / JavaScript / Bootstrap}

\resumesection{Skills}
\textbf{Backend:} Java, Spring Boot, Spring MVC, Spring Security, Spring Data JPA, Hibernate, Microservices, Spring Cloud \\
\textbf{Frontend \& APIs:} React.js, JavaScript, HTML5, CSS3, RESTful APIs, JWT Security, RBAC \\
\textbf{Data \& Messaging:} MySQL, PostgreSQL, Redis cache, Apache Kafka, database transactions \\
\textbf{Tools:} Maven, Gradle, Git, GitHub, Postman, Docker, Spring Boot Actuator, Prometheus, Grafana

\resumesection{Education}
{\textbf{B.Tech.}} \\
{\textbf{\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~07/2019 -- 05/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Kanpur, UP}

\resumesection{Certifications}
GeeksforGeeks MERN Stack Certification \quad | \quad Coding Ninjas DBMS Certification \\
Coding Ninjas DSA Certification \quad | \quad IIT Kanpur Prutor Cyber Security Certification

\resumesection{Achievements}
\begin{itemize}
    \item Graduated with First Class Honors, maintaining top academic rank.
    \item Earned a 4-Star Gold Badge in SQL on HackerRank.
\end{itemize}

\end{document}
```
