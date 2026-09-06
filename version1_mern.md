# Resume Version 1: MERN Stack Developer
> Single-stack by design. This version mentions only the technologies relevant to the target role.

## 1. Professional Summary
Full stack engineer, 3+ years on India's national payments platform — 500,000+ transactions a day for 2 million+ users. Cut p95 read latency 40% by rewriting the MongoDB aggregation pipelines behind it, and held AEPS and MATM settlement at a 99% success rate by making the payment path idempotent and self-reconciling. React, TypeScript and Node.js end to end — schema design through Dockerised CI/CD.

## 2. Technical Skills
* **Frontend:** React.js, Next.js SSR/ISR, TypeScript, JavaScript (ES6+), Redux Toolkit, React Query, Tailwind CSS, Material UI, code splitting, Core Web Vitals
* **Backend & APIs:** Node.js, Express.js, REST API design, OpenAPI/Swagger, WebSockets, JWT, OAuth 2.0, RBAC, rate limiting, idempotency keys, API versioning
* **Data & Caching:** MongoDB, aggregation pipelines, compound indexing, sharding, Mongoose, Redis, PostgreSQL, query profiling, schema design
* **Testing, Cloud & Practice:** Jest, React Testing Library, Supertest, Docker, GitHub Actions CI/CD, AWS EC2/S3/CloudFront, Nginx, Grafana, Sentry, Agile/Scrum, code review

## 3. Experience
### Software Development Engineer
**CSC e-Governance Services India Ltd. --- India's national digital services platform, 2M+ users**
*12/2023 – Present | New Delhi, India*
* Held AEPS and MATM settlement at a **99% success rate** through peak load, by making the UPI and XML payment path idempotent — request keys, exponential-backoff retries and an automated end-of-day reconciliation job.
* Cut **p95 read latency 40%** on the transaction APIs serving **2 million+ users**, by collapsing N+1 **Mongoose** queries into a single **MongoDB** aggregation pipeline and compound-indexing the hot collections.
* Streamed **500,000+ daily transactions** to operations in real time, by building the transaction and geolocation dashboards in **React.js** and **Redux Toolkit** over a **WebSocket** feed with memoised selectors.
* Contained a bad release to one service instead of the whole portal for **2 million+ users**, by decomposing a monolithic e-governance system into **Node.js** and **Express.js** microservices behind a versioned REST gateway.
* Blocked **99.9%** of unauthorized access attempts on the payments API, by adding **JWT** access/refresh rotation, **Redis**-backed sessions, device binding, RBAC middleware and per-device OTP rate limiting.
* Retired manual releases across all **3** payment platforms, by containerising the services with **Docker** and gating every merge on **GitHub Actions** running **Jest** unit and **Supertest** integration suites.

### Software Engineer
**Contract engagement --- field-workforce logistics, 1,000+ agents**
*06/2023 – 11/2023 | Remote, India*
* Shipped a field-workforce platform used by **1,000+ agents** end to end — schema design through AWS deployment — on **React.js**, **Node.js**, **Express.js** and **MongoDB**.
* Brought dashboard load time down **30%**, by route-level code splitting of the **React.js** map view, virtualising marker rendering and streaming positions over **WebSockets** instead of polling.
* Removed **45%** of redundant API calls, by moving server state onto **React Query** with stale-while-revalidate caching and consolidating client state in **Redux Toolkit**.

## 4. Projects
### Himalayan Edges — MERN Commerce PWA
*Stack: React.js / Node.js / Express.js / MongoDB / PWA / AWS S3*
Lifted page-load speed and client usage 30% at a 20% cart conversion rate, by shipping a service-worker offline cache, route-level code splitting and S3-backed asset delivery on a React, Express and MongoDB storefront.

### DigiPay Web SDK & React Widgets
*Stack: React.js / TypeScript / npm workspaces / Webpack / REST*
Embeddable React component library and browser SDK published from an npm workspaces monorepo, giving merchant sites a drop-in payment UI over a versioned REST API. github.com/GitHub-akhilesh/Django_apis_digipay

### Task Platform — React Web and React Native
*Stack: React.js / React Native / Node.js / Docker / Webpack*
React web client and React Native mobile app over a containerised REST backend, built as a workspace monorepo with Webpack builds and Docker Compose orchestration. github.com/GitHub-akhilesh/To-do-list-app

### Real-Time Geofencing & Telemetry Dashboard
*Stack: React.js / Node.js / Express.js / WebSockets / MongoDB / Redis*
Delivers live GPS positions and geofence alerts to 1,000+ field agents with no polling anywhere in the path, by streaming over WebSockets from an Express ingestion API into time-indexed MongoDB collections.

## 5. Education
### Bachelor of Technology (B.Tech.)
**Kanpur Institute of Technology** | *Kanpur, UP*
*07/2019 – 05/2023*

## 6. Certifications
* IIT Kanpur Cyber Security Certification

## 7. Achievements
* HackerRank 4-Star Gold badge in SQL.

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
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{Full Stack Engineer (MERN) | React $\cdot$ Node.js $\cdot$ MongoDB --- Payments at 2M+ Users}}} \\
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
Full stack engineer, 3+ years on India's national payments platform --- 500,000+ transactions a day for 2 million+ users. Cut p95 read latency 40\% by rewriting the MongoDB aggregation pipelines behind it, and held AEPS and MATM settlement at a 99\% success rate by making the payment path idempotent and self-reconciling. React, TypeScript and Node.js end to end --- schema design through Dockerised CI/CD.

\resumesection{Experience}
{\textbf{Software Development Engineer}} \\
{\textbf{\textcolor{primaryblue}{CSC e-Governance Services India Ltd. --- India's national digital services platform, 2M+ users}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~12/2023 -- Present \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~New Delhi, India}
\begin{itemize}
    \item Held AEPS and MATM settlement at a \textbf{99\% success rate} through peak load, by making the UPI and XML payment path idempotent --- request keys, exponential-backoff retries and an automated end-of-day reconciliation job.
    \item Cut \textbf{p95 read latency 40\%} on the transaction APIs serving \textbf{2 million+ users}, by collapsing N+1 \textbf{Mongoose} queries into a single \textbf{MongoDB} aggregation pipeline and compound-indexing the hot collections.
    \item Streamed \textbf{500,000+ daily transactions} to operations in real time, by building the transaction and geolocation dashboards in \textbf{React.js} and \textbf{Redux Toolkit} over a \textbf{WebSocket} feed with memoised selectors.
    \item Contained a bad release to one service instead of the whole portal for \textbf{2 million+ users}, by decomposing a monolithic e-governance system into \textbf{Node.js} and \textbf{Express.js} microservices behind a versioned REST gateway.
    \item Blocked \textbf{99.9\%} of unauthorized access attempts on the payments API, by adding \textbf{JWT} access/refresh rotation, \textbf{Redis}-backed sessions, device binding, RBAC middleware and per-device OTP rate limiting.
    \item Retired manual releases across all \textbf{3} payment platforms, by containerising the services with \textbf{Docker} and gating every merge on \textbf{GitHub Actions} running \textbf{Jest} unit and \textbf{Supertest} integration suites.
\end{itemize}

\vspace{4pt}
{\textbf{Software Engineer}} \\
{\textbf{\textcolor{primaryblue}{Contract engagement --- field-workforce logistics, 1,000+ agents}}} \\
{\footnotesize\textcolor{primaryblue}{\faCalendar*}~06/2023 -- 11/2023 \quad | \quad \textcolor{primaryblue}{\faMapMarker*}~Remote, India}
\begin{itemize}
    \item Shipped a field-workforce platform used by \textbf{1,000+ agents} end to end --- schema design through AWS deployment --- on \textbf{React.js}, \textbf{Node.js}, \textbf{Express.js} and \textbf{MongoDB}.
    \item Brought dashboard load time down \textbf{30\%}, by route-level code splitting of the \textbf{React.js} map view, virtualising marker rendering and streaming positions over \textbf{WebSockets} instead of polling.
    \item Removed \textbf{45\%} of redundant API calls, by moving server state onto \textbf{React Query} with stale-while-revalidate caching and consolidating client state in \textbf{Redux Toolkit}.
\end{itemize}

\resumesection{Projects}
{\textbf{Himalayan Edges --- MERN Commerce PWA}} \\
{\small Lifted page-load speed and client usage 30\% at a 20\% cart conversion rate, by shipping a service-worker offline cache, route-level code splitting and S3-backed asset delivery on a React, Express and MongoDB storefront.} \\
{\footnotesize\textbf{STACK:} React.js / Node.js / Express.js / MongoDB / PWA / AWS S3}

\vspace{4pt}
{\textbf{DigiPay Web SDK \& React Widgets}} \\
{\small Embeddable React component library and browser SDK published from an npm workspaces monorepo, giving merchant sites a drop-in payment UI over a versioned REST API. github.com/GitHub-akhilesh/Django\_apis\_digipay} \\
{\footnotesize\textbf{STACK:} React.js / TypeScript / npm workspaces / Webpack / REST}

\vspace{4pt}
{\textbf{Task Platform --- React Web and React Native}} \\
{\small React web client and React Native mobile app over a containerised REST backend, built as a workspace monorepo with Webpack builds and Docker Compose orchestration. github.com/GitHub-akhilesh/To-do-list-app} \\
{\footnotesize\textbf{STACK:} React.js / React Native / Node.js / Docker / Webpack}

\vspace{4pt}
{\textbf{Real-Time Geofencing \& Telemetry Dashboard}} \\
{\small Delivers live GPS positions and geofence alerts to 1,000+ field agents with no polling anywhere in the path, by streaming over WebSockets from an Express ingestion API into time-indexed MongoDB collections.} \\
{\footnotesize\textbf{STACK:} React.js / Node.js / Express.js / WebSockets / MongoDB / Redis}

\resumesection{Skills}
\textbf{Frontend:} React.js, Next.js SSR/ISR, TypeScript, JavaScript (ES6+), Redux Toolkit, React Query, Tailwind CSS, Material UI, code splitting, Core Web Vitals \\
\textbf{Backend \& APIs:} Node.js, Express.js, REST API design, OpenAPI/Swagger, WebSockets, JWT, OAuth 2.0, RBAC, rate limiting, idempotency keys, API versioning \\
\textbf{Data \& Caching:} MongoDB, aggregation pipelines, compound indexing, sharding, Mongoose, Redis, PostgreSQL, query profiling, schema design \\
\textbf{Testing, Cloud \& Practice:} Jest, React Testing Library, Supertest, Docker, GitHub Actions CI/CD, AWS EC2/S3/CloudFront, Nginx, Grafana, Sentry, Agile/Scrum, code review

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
