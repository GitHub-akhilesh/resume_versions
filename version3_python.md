# Resume Version 3: Python Full Stack Developer

## 1. Professional Summary
Software Development Engineer specializing in Python Full Stack development, with a track record of building secure, scalable backend architectures and web systems. Expert in Python, Django, Django REST Framework (DRF), FastAPI, Celery, and database design in PostgreSQL/MySQL. Proven experience in migrating monoliths to async microservices, designing event-driven pipelines using Celery/Redis, and building real-time dashboards via WebSockets. Optimizes database queries and scales backend infrastructures using Docker.

## 2. Technical Skills
* **Backend:** Python, Django, Django REST Framework, FastAPI, Celery
* **Frontend:** React.js, JavaScript, HTML5, CSS3, Bootstrap
* **Database:** PostgreSQL, MySQL, SQLite
* **API:** REST API, JWT, OAuth
* **Tools:** Git, GitHub, Docker, Linux, Postman

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present*
*E-Governance initiatives under the Ministry of Electronics & Information Technology*
* Re-architected monolithic web services into scalable, asynchronous **FastAPI** and **Django** microservices, improving deployment speeds and fault isolation for 20 lakh+ users.
* Designed and scaled transaction orchestration services for AEPS, MATM, and VATM platforms using Django REST Framework, handling 5 lakh+ daily transactions with a ~80% success rate.
* Implemented secure API authentication using **JWT** and role-based access control (**RBAC**), including OTP verification and device binding.
* Developed an asynchronous task queuing pipeline using **Celery** and **Redis** to handle high-volume wallet ledger records and notifications.
* Tuned **PostgreSQL** and **MySQL** database schemas using indexing and query partitioning, lowering average transaction query latency under peak loads.
* Constructed real-time transaction tracking APIs utilizing **FastAPI WebSockets** to stream live status updates to frontend clients.
* Set up centralized logging using **ELK Stack** and implemented system metrics collection with Prometheus and Grafana.
* Deployed containerized microservices using **Docker** and configured automated CI/CD testing pipelines with Git and GitHub Actions.
* Led hiring and onboarding of 4 engineers, expanding technical team capacity and onboarding efficiency by 40%.

### Freelance Software Engineer
**Workforce Telemetry & Geofencing System**
*06/2023 – 11/2023*
*Real-Time Telemetry & Operations Platform*
* Developed a real-time workforce telemetry and geofencing system utilizing **FastAPI**, **SQLAlchemy** (asyncio), and **React.js**.
* Built an interactive live telemetry dashboard in **React** using Ant Design (antd) to visualize real-time coordinates, speed, and geofence compliance.
* Implemented a high-performance, asynchronous ingestion API to capture GPS locations (`/api/v1/tracking/ingest`) using **FastAPI** and **aiosqlite**.
* Utilized **Celery** tasks and **Redis** as a message broker to queue location analytics, processing geofence entry/exit transitions asynchronously.

## 4. Projects
### Himalayan Edges Website Development
*10/2024 – 11/2024*
* Created an e-commerce platform using **Django** and **React.js** with PWA features, hosted on AWS, boosting speed and usage by 30%.
* Enforced role-based authentication with email verification using JWT in Django REST Framework, securing 5,000+ accounts.
* Designed modular model-view-controller architectures in Django, tested under 500+ concurrent users with a 20% cart conversion rate.
* Integrated Google Reviews dynamically to increase site authority and improve conversions by 15%.

### Automatic Attendance Through Face Detection
*05/2024 – 07/2024*
* Developed an automated attendance tracking application in **Python** using **OpenCV** (Haarcascade & LBPH) and **MySQL**.
* Created a custom desktop graphical interface using **Tkinter** for registering student profiles, capturing training images, and logging attendance.
* Programmed data export scripts using **Pandas** to compile attendance reports in Excel, reducing manual tracking work by 70%.

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
* **94/100** - Strong keyword concentration of Django, FastAPI, Celery, PostgreSQL, and Python. Solid metrics.

## 9. Missing Skills Recommendations
* Include familiarity with Python web frameworks like Flask (as a lighter alternative).
* Add testing experience using Pytest and mock objects.
* Mention experience with caching strategies using Redis/Memcached.

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
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{Python Full Stack Developer}}} \\
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
Software Development Engineer specializing in Python Full Stack development, with a track record of building secure, scalable backend architectures and web systems. Expert in Python, Django, Django REST Framework (DRF), FastAPI, Celery, and database design in PostgreSQL/MySQL. Proven experience in migrating monoliths to async microservices, designing event-driven pipelines using Celery/Redis, and building real-time dashboards via WebSockets. Optimizes database queries and scales backend infrastructures using Docker.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Re-architected monolithic web services into scalable, asynchronous \textbf{FastAPI} and \textbf{Django} microservices, improving reliability for 20 lakh+ users.
    \item Designed and scaled transaction orchestration services for AEPS, MATM, and VATM platforms using Django REST Framework, handling 5 lakh+ daily transactions.
    \item Implemented secure API authentication using \textbf{JWT} and role-based access control (\textbf{RBAC}), including OTP verification.
    \item Developed an asynchronous task queuing pipeline using \textbf{Celery} and \textbf{Redis} to handle high-volume wallet ledger records.
    \item Tuned \textbf{PostgreSQL} and \textbf{MySQL} database schemas using indexing and query partitioning, lowering transaction query latency.
    \item Constructed real-time transaction tracking APIs utilizing \textbf{FastAPI WebSockets} to stream live status updates.
\end{itemize}

\vspace{4pt}
{\textbf{Freelance Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Workforce Telemetry \& Operations}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Developed a real-time workforce telemetry and geofencing system utilizing \textbf{FastAPI}, \textbf{SQLAlchemy} (asyncio), and \textbf{React.js}.
    \item Built an interactive live telemetry dashboard in \textbf{React} using Ant Design (antd) to visualize coordinates, speed, and geofences.
    \item Implemented a high-performance, asynchronous ingestion API to capture GPS locations (\texttt{/api/v1/tracking/ingest}) using \textbf{FastAPI}.
\end{itemize}

\resumesection{Projects}
{\textbf{Facial Recognition Attendance Dashboard}} \\
{\small Developed an automated student attendance tracking application in Python using OpenCV (Haarcascade \& LBPH) and MySQL, with custom Excel reports via Pandas.} \\
{\footnotesize\textbf{STACK:} Python / OpenCV / Tkinter / MySQL / Pandas}

\vspace{4pt}
{\textbf{Himalayan Edges Website Development}} \\
{\small Created an e-commerce platform using Django and React.js with PWA features, hosted on AWS, boosting page speeds and usage by 30\%.} \\
{\footnotesize\textbf{STACK:} Python / Django / React.js / SQLite / AWS / PWA}

\vspace{4pt}
{\textbf{Persistent Task Management Dashboard}} \\
{\small Programmed a desktop utility for task planning, category filtering, and JSON data persistence, featuring clean MVC architecture patterns.} \\
{\footnotesize\textbf{STACK:} Python / Tkinter / JSON / MVC Patterns}

\vspace{4pt}
{\textbf{Traveling Portal \& Landing Page}} \\
{\small A fully responsive, modern front-end landing page for a travel agency designed with HTML, CSS, and Bootstrap layouts.} \\
{\footnotesize\textbf{STACK:} HTML5 / CSS3 / JavaScript / Bootstrap}

\resumesection{Skills}
\textbf{Backend:} Python, Django, FastAPI, Celery, Django REST Framework, SQLAlchemy (asyncio), Pandas \\
\textbf{Frontend \& APIs:} React.js, JavaScript, HTML5, CSS3, Bootstrap, RESTful APIs, WebSockets, JWT Security \\
\textbf{Data \& Messaging:} PostgreSQL, MySQL, SQLite, Redis cache/broker, database schema design, query indexing \\
\textbf{Tools \& Cloud:} Git, GitHub, Docker, Postman, Linux environments, OpenCV, LBPH face recognition

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
