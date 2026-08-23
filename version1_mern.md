# Resume Version 1: MERN Stack Developer
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Software Development Engineer specializing in the MERN stack, building secure, high-throughput FinTech and transaction platforms. Deep expertise in React.js, Next.js, Redux Toolkit, Node.js, Express.js, and MongoDB. Scaled Node.js microservices to serve 2 million+ users and 500,000+ daily transactions, cut MongoDB response times by 40% through indexing and aggregation tuning, and delivered real-time monitoring dashboards over WebSockets. Ships containerized releases through Docker and GitHub Actions.

## 2. Technical Skills
* **Frontend:** React.js, Next.js, Redux Toolkit, React Query, JavaScript (ES6+), TypeScript, HTML5, CSS3, Tailwind CSS, Material UI
* **Backend & APIs:** Node.js, Express.js, RESTful APIs, WebSockets, JWT authentication, RBAC, middleware design, API versioning
* **Database & Caching:** MongoDB, Mongoose, aggregation pipelines, schema design, indexing, sharding, Redis
* **Tooling & Cloud:** Git, GitHub, GitHub Actions, Docker, CI/CD pipelines, Jest, Postman, AWS S3

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. (MeitY, Government of India)**
*12/2023 – Present | New Delhi, India*
* Re-architected monolithic e-governance portals into **Node.js** and **Express.js** microservices, improving fault isolation and deployment speed for **2 million+ active users**.
* Built real-time transaction monitoring and location tracking dashboards with **React.js**, **Redux Toolkit**, and **WebSockets**, surfacing **500,000+ daily transactions** with sub-second updates.
* Integrated third-party UPI and XML payment APIs through **Express.js** service controllers, adding retry and reconciliation handling that raised AEPS and MATM settlement reliability at peak load.
* Hardened authentication with **JWT** and **Redis**-backed sessions, layering device binding and OTP throttling to shut down credential-stuffing and replay attempts.
* Tuned **MongoDB** schemas with compound indexing, sharding, and **Mongoose** aggregation rewrites, cutting database response times by **40%**.
* Automated build, test, and container delivery with **Docker**, **GitHub Actions**, and **Git**, removing manual release steps from every deployment.

### Freelance Software Engineer
**Workforce Telemetry & Operations**
*06/2023 – 11/2023 | Remote, India*
* Designed and shipped a real-time workforce tracking platform on **React.js**, **Node.js**, **Express.js**, and **MongoDB**, serving **1,000+ active field agents**.
* Built an interactive map tracking interface in **React.js** with **Ant Design**, streaming live coordinates over WebSockets and cutting UI load times by **30%**.
* Managed client state and request caching with **Redux Toolkit** and **React Query**, eliminating **45%** of redundant API calls.

## 4. Projects
### MERN FinTech & Commerce Suite
*Stack: React.js / Redux Toolkit / Node.js / Express.js / MongoDB / JWT*
Full-stack applications with JWT-secured authentication, role-based admin dashboards, and versioned REST APIs built on React, Redux Toolkit, Express, and MongoDB.

### Himalayan Edges E-Commerce Platform
*Stack: React.js / Node.js / Express.js / MongoDB / PWA / AWS S3*
PWA-enabled storefront built on the MERN stack and deployed to AWS, lifting page-load speed and client usage by 30% at a 20% cart conversion rate.

### Real-Time Geofencing & Telemetry Dashboard
*Stack: React.js / Node.js / Express.js / WebSockets / MongoDB*
Live workforce tracking dashboard streaming GPS coordinates and geofence alerts to a React map view over WebSockets, backed by an Express ingestion API and indexed MongoDB collections.

### Role-Based Authentication & Admin Portal
*Stack: Node.js / Express.js / MongoDB / JWT / React Router*
Reusable Express authentication service with password hashing, JWT access and refresh token rotation, and RBAC middleware consumed by React protected routes.

## 5. Education
### Bachelor of Technology (B.Tech.)
**Kanpur Institute of Technology** | *Kanpur, UP*
*07/2019 – 05/2023*

## 6. Certifications
* Advanced MERN Stack Developer Certification
* Data Structures & Algorithms Certification
* Database Systems & SQL Certification
* IIT Kanpur Cyber Security Certification

## 7. Achievements
* Graduated with First Class Honors, maintaining top academic rank.
* Earned a 4-Star Gold Badge in SQL on HackerRank.

## 8. ATS Score Estimate
* **96/100** — keyword coverage is concentrated on a single stack, so role-matched screens score higher and nothing dilutes the match.

## 9. Missing Skills Recommendations
* Add automated testing depth: Jest and React Testing Library unit coverage, plus Supertest for Express route integration tests.
* Mention a managed deployment target for Node services (AWS ECS, Elastic Beanstalk, or Render) alongside Docker.
* Add server-side rendering and caching specifics for Next.js (ISR, route handlers, edge caching).

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
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{MERN Stack Developer | React.js $\cdot$ Node.js $\cdot$ Express.js $\cdot$ MongoDB}}} \\
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
Software Development Engineer specializing in the MERN stack, building secure, high-throughput FinTech and transaction platforms. Deep expertise in React.js, Next.js, Redux Toolkit, Node.js, Express.js, and MongoDB. Scaled Node.js microservices to serve 2 million+ users and 500,000+ daily transactions, cut MongoDB response times by 40\% through indexing and aggregation tuning, and delivered real-time monitoring dashboards over WebSockets. Ships containerized releases through Docker and GitHub Actions.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. (MeitY, Government of India)}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Re-architected monolithic e-governance portals into \textbf{Node.js} and \textbf{Express.js} microservices, improving fault isolation and deployment speed for \textbf{2 million+ active users}.
    \item Built real-time transaction monitoring and location tracking dashboards with \textbf{React.js}, \textbf{Redux Toolkit}, and \textbf{WebSockets}, surfacing \textbf{500,000+ daily transactions} with sub-second updates.
    \item Integrated third-party UPI and XML payment APIs through \textbf{Express.js} service controllers, adding retry and reconciliation handling that raised AEPS and MATM settlement reliability at peak load.
    \item Hardened authentication with \textbf{JWT} and \textbf{Redis}-backed sessions, layering device binding and OTP throttling to shut down credential-stuffing and replay attempts.
    \item Tuned \textbf{MongoDB} schemas with compound indexing, sharding, and \textbf{Mongoose} aggregation rewrites, cutting database response times by \textbf{40\%}.
    \item Automated build, test, and container delivery with \textbf{Docker}, \textbf{GitHub Actions}, and \textbf{Git}, removing manual release steps from every deployment.
\end{itemize}

\vspace{4pt}
{\textbf{Freelance Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Workforce Telemetry \& Operations}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Designed and shipped a real-time workforce tracking platform on \textbf{React.js}, \textbf{Node.js}, \textbf{Express.js}, and \textbf{MongoDB}, serving \textbf{1,000+ active field agents}.
    \item Built an interactive map tracking interface in \textbf{React.js} with \textbf{Ant Design}, streaming live coordinates over WebSockets and cutting UI load times by \textbf{30\%}.
    \item Managed client state and request caching with \textbf{Redux Toolkit} and \textbf{React Query}, eliminating \textbf{45\%} of redundant API calls.
\end{itemize}

\resumesection{Projects}
{\textbf{MERN FinTech \& Commerce Suite}} \\
{\small Full-stack applications with JWT-secured authentication, role-based admin dashboards, and versioned REST APIs built on React, Redux Toolkit, Express, and MongoDB.} \\
{\footnotesize\textbf{STACK:} React.js / Redux Toolkit / Node.js / Express.js / MongoDB / JWT}

\vspace{4pt}
{\textbf{Himalayan Edges E-Commerce Platform}} \\
{\small PWA-enabled storefront built on the MERN stack and deployed to AWS, lifting page-load speed and client usage by 30\% at a 20\% cart conversion rate.} \\
{\footnotesize\textbf{STACK:} React.js / Node.js / Express.js / MongoDB / PWA / AWS S3}

\vspace{4pt}
{\textbf{Real-Time Geofencing \& Telemetry Dashboard}} \\
{\small Live workforce tracking dashboard streaming GPS coordinates and geofence alerts to a React map view over WebSockets, backed by an Express ingestion API and indexed MongoDB collections.} \\
{\footnotesize\textbf{STACK:} React.js / Node.js / Express.js / WebSockets / MongoDB}

\vspace{4pt}
{\textbf{Role-Based Authentication \& Admin Portal}} \\
{\small Reusable Express authentication service with password hashing, JWT access and refresh token rotation, and RBAC middleware consumed by React protected routes.} \\
{\footnotesize\textbf{STACK:} Node.js / Express.js / MongoDB / JWT / React Router}

\resumesection{Skills}
\textbf{Frontend:} React.js, Next.js, Redux Toolkit, React Query, JavaScript (ES6+), TypeScript, HTML5, CSS3, Tailwind CSS, Material UI \\
\textbf{Backend \& APIs:} Node.js, Express.js, RESTful APIs, WebSockets, JWT authentication, RBAC, middleware design, API versioning \\
\textbf{Database \& Caching:} MongoDB, Mongoose, aggregation pipelines, schema design, indexing, sharding, Redis \\
\textbf{Tooling \& Cloud:} Git, GitHub, GitHub Actions, Docker, CI/CD pipelines, Jest, Postman, AWS S3

\resumesection{Education}
{\textbf{Bachelor of Technology (B.Tech.)}} \\
{\textbf{\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~07/2019 -- 05/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Kanpur, UP}

\resumesection{Certifications}
Advanced MERN Stack Developer Certification \quad | \quad Data Structures \& Algorithms Certification \\
Database Systems \& SQL Certification \quad | \quad IIT Kanpur Cyber Security Certification

\resumesection{Achievements}
\begin{itemize}
    \item Graduated with First Class Honors, maintaining top academic rank.
    \item Earned a 4-Star Gold Badge in SQL on HackerRank.
\end{itemize}

\end{document}
```
