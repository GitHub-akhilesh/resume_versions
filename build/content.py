# -*- coding: utf-8 -*-
"""Role-specific resume content. One dict per version; nothing off-stack leaks in."""

V1 = {  # ---------------- MERN ----------------
 "ats": "96",
 "title": "Full Stack Engineer (MERN) | React &middot; Node.js &middot; MongoDB &mdash; Payments at 2M+ Users",
 "summary": "500,000+ payment transactions a day for 2 million+ users on India's national e-governance platform. Cut p95 read latency 40% by rewriting the MongoDB aggregation pipelines behind it, and held AEPS and MATM settlement at a 99% success rate by making the payment path idempotent and self-reconciling. React, TypeScript and Node.js end to end &mdash; schema design through Dockerised CI/CD.",
 "skills": [
   ("Frontend", "React.js, Next.js SSR/ISR, TypeScript, JavaScript (ES6+), Redux Toolkit, React Query, Tailwind CSS, Material UI, code splitting, Core Web Vitals"),
   ("Backend &amp; APIs", "Node.js, Express.js, REST API design, OpenAPI/Swagger, WebSockets, JWT, OAuth 2.0, RBAC, rate limiting, idempotency keys, API versioning"),
   ("Data &amp; Caching", "MongoDB, aggregation pipelines, compound indexing, sharding, Mongoose, Redis, PostgreSQL, query profiling, schema design"),
   ("Testing, Cloud &amp; Practice", "Jest, React Testing Library, Supertest, Docker, GitHub Actions CI/CD, AWS EC2/S3/CloudFront, Nginx, Grafana, Sentry, Agile/Scrum, code review"),
 ],
 "exp": [[
   "Held AEPS and MATM settlement at a <strong>99% success rate</strong> through peak load, by making the UPI and XML payment path idempotent &mdash; request keys, exponential-backoff retries and an automated end-of-day reconciliation job.",
   "Cut <strong>p95 read latency 40%</strong> on the transaction APIs serving <strong>2 million+ users</strong>, by collapsing N+1 <strong>Mongoose</strong> queries into a single <strong>MongoDB</strong> aggregation pipeline and compound-indexing the hot collections.",
   "Streamed <strong>500,000+ daily transactions</strong> to operations in real time, by building the transaction and geolocation dashboards in <strong>React.js</strong> and <strong>Redux Toolkit</strong> over a <strong>WebSocket</strong> feed with memoised selectors.",
   "Contained a bad release to one service instead of the whole portal for <strong>2 million+ users</strong>, by decomposing a monolithic e-governance system into <strong>Node.js</strong> and <strong>Express.js</strong> microservices behind a versioned REST gateway.",
   "Blocked <strong>99.9%</strong> of unauthorized access attempts on the payments API, by adding <strong>JWT</strong> access/refresh rotation, <strong>Redis</strong>-backed sessions, device binding, RBAC middleware and per-device OTP rate limiting.",
   "Retired manual releases across all <strong>3</strong> payment platforms, by containerising the services with <strong>Docker</strong> and gating every merge on <strong>GitHub Actions</strong> running <strong>Jest</strong> unit and <strong>Supertest</strong> integration suites.",
 ],[
   "Shipped a field-workforce platform used by <strong>1,000+ agents</strong> end to end &mdash; schema design through AWS deployment &mdash; on <strong>React.js</strong>, <strong>Node.js</strong>, <strong>Express.js</strong> and <strong>MongoDB</strong>.",
   "Brought dashboard load time down <strong>30%</strong>, by route-level code splitting of the <strong>React.js</strong> map view, virtualising marker rendering and streaming positions over <strong>WebSockets</strong> instead of polling.",
   "Removed <strong>45%</strong> of redundant API calls, by moving server state onto <strong>React Query</strong> with stale-while-revalidate caching and consolidating client state in <strong>Redux Toolkit</strong>.",
 ]],
 "projects": [
   ("Himalayan Edges &mdash; MERN Commerce PWA",
    "Lifted page-load speed and client usage 30% at a 20% cart conversion rate, by shipping a service-worker offline cache, route-level code splitting and S3-backed asset delivery on a React, Express and MongoDB storefront.",
    "React.js / Node.js / Express.js / MongoDB / PWA / AWS S3"),
   ("DigiPay Web SDK &amp; React Widgets",
    "Embeddable React component library and browser SDK published from an npm workspaces monorepo, giving merchant sites a drop-in payment UI over a versioned REST API. github.com/GitHub-akhilesh/Django_apis_digipay",
    "React.js / TypeScript / npm workspaces / Webpack / REST"),
   ("Task Platform &mdash; React Web and React Native",
    "React web client and React Native mobile app over a containerised REST backend, built as a workspace monorepo with Webpack builds and Docker Compose orchestration. github.com/GitHub-akhilesh/To-do-list-app",
    "React.js / React Native / Node.js / Docker / Webpack"),
   ("Real-Time Geofencing &amp; Telemetry Dashboard",
    "Delivers live GPS positions and geofence alerts to 1,000+ field agents with no polling anywhere in the path, by streaming over WebSockets from an Express ingestion API into time-indexed MongoDB collections.",
    "React.js / Node.js / Express.js / WebSockets / MongoDB / Redis"),
 ],
 "certs": ["IIT Kanpur Cyber Security Certification"],
}

V2 = {  # ---------------- Java ----------------
 "ats": "96",
 "title": "Java Full Stack Developer | Spring Boot &middot; Microservices &middot; REST APIs",
 "summary": "Backend engineer running payment infrastructure that clears 500,000+ transactions a day for 2M+ users. Java/Spring Boot, Kafka, microservices. Wallet and ledger services settle over 10 billion INR daily with balances that reconcile, and AEPS, MATM and VATM orchestration holds a 99% success rate at peak through idempotent request handling and automated reconciliation. Cut p95 database latency 45% with covering indexes and Redis caching.",
 "skills": [
   ("Core", "Java, Spring Boot, Spring Security, Spring Data JPA, Hibernate, microservices, REST APIs"),
   ("Data &amp; Messaging", "Apache Kafka, MySQL, PostgreSQL, MongoDB, Redis, transaction boundaries, covering indexes, query tuning"),
   ("Platform &amp; Delivery", "Docker, Kubernetes, GitHub Actions CI/CD, Maven, Gradle, JUnit 5, Mockito, Testcontainers, Prometheus, Grafana"),
   ("Also", "Python, React.js, JavaScript (ES6+), JWT, RBAC, OpenAPI/Swagger, idempotency keys"),
 ],
 "exp": [[
   "Held AEPS, MATM and VATM orchestration at a <strong>99% success rate</strong> across <strong>500,000+ daily transactions</strong>, by making the <strong>Spring Boot</strong> payment path idempotent with request keys, backoff retries and automated end-of-day reconciliation.",
   "Settled over <strong>10 billion INR</strong> a day with balances that reconcile, by building the wallet and ledger services on <strong>Spring Data JPA</strong> and <strong>Hibernate</strong> with explicit transaction boundaries and optimistic locking.",
   "Cut p95 read/write latency <strong>45%</strong> across <strong>MySQL</strong> and <strong>PostgreSQL</strong>, by adding covering indexes, tuning the JPA fetch strategy to kill N+1 queries and caching hot lookups in <strong>Redis</strong>.",
   "Contained a bad release to one service instead of the whole portal for <strong>2 million+ users</strong>, by splitting monolithic e-governance systems into <strong>Spring Boot</strong> microservices behind a versioned REST gateway.",
   "Blocked <strong>99.9%</strong> of unauthorized access attempts, by adding <strong>Spring Security</strong> with <strong>JWT</strong>, method-level <strong>RBAC</strong>, device binding and OTP retry limits.",
   "Lifted async throughput <strong>35%</strong>, by moving inter-service calls onto <strong>Apache Kafka</strong> with dead-letter topics, and surfacing consumer lag in <strong>Prometheus</strong> and <strong>Grafana</strong>.",
 ],[
   "Shipped a workforce tracking platform for <strong>1,000+ field agents</strong> end to end on <strong>Java</strong>, <strong>Spring Boot</strong> and <strong>React.js</strong> &mdash; schema design through AWS deployment.",
   "Brought dashboard load time down <strong>30%</strong>, by streaming live coordinates from Spring Boot <strong>WebSocket</strong> endpoints into a <strong>React.js</strong> and <strong>Ant Design</strong> map view instead of polling.",
   "Enforced Admin, Supervisor and Employee boundaries across <strong>100+ client accounts</strong>, by adding <strong>Spring Security</strong> method-level authorization and <strong>JWT</strong> claims to the operations API.",
 ]],
 "projects": [
   ("Enterprise Authentication &amp; Authorization Service",
    "Spring Security service handling user registration, password hashing, JWT issuance and validation, and role-mapped access control across protected REST routes.",
    "Java / Spring Boot / Spring Security / JWT / Hibernate / MySQL"),
   ("Himalayan Edges Commerce Platform",
    "PWA-enabled e-commerce platform on Spring Boot REST services with modular controllers and normalized MySQL schemas, load-verified at 500+ concurrent users.",
    "Java / Spring Boot / Spring Data JPA / MySQL / AWS / PWA"),
   ("Attendance Management &amp; Reporting Platform",
    "Spring Boot service exposing REST endpoints for student registration, daily attendance logging, and scheduled Excel report generation, cutting manual record-keeping by 70%.",
    "Java / Spring Boot / Spring Data JPA / MySQL / REST APIs"),
   ("Wallet &amp; Transaction Ledger Service",
    "Wallet and ledger service built on Spring Data JPA and Hibernate, using managed transaction boundaries and indexed MySQL schemas to keep balances consistent under concurrent settlement.",
    "Java / Spring Boot / Spring Data JPA / Hibernate / MySQL / Redis"),
 ],
 "certs": ["IIT Kanpur Cyber Security Certification"],
}

V3 = {  # ---------------- Python ----------------
 "ats": "95",
 "title": "Python Full Stack Developer | Django &middot; FastAPI &middot; REST APIs",
 "summary": "500,000+ transactions a day for 2 million+ users on India national e-governance platforms, served by Django REST Framework and async FastAPI services. Took transaction query p95 down 45% by partitioning and indexing PostgreSQL, cleared 35% of the peak backlog onto Celery and Redis workers, and streams live status over WebSockets in under 500ms. Reads the query plan before adding the index.",
 "skills": [
   ("Core Python", "Python, Django, Django REST Framework, FastAPI, Flask, Celery, SQLAlchemy, Alembic, asyncio"),
   ("APIs &amp; Security", "RESTful APIs, OpenAPI/Swagger, JWT, OAuth 2.0, RBAC, rate limiting, idempotency keys, FastAPI WebSockets, API versioning"),
   ("Data &amp; Messaging", "PostgreSQL, MySQL, Redis, Celery queues, covering indexes, partitioning, query plan analysis"),
   ("Testing &amp; DevOps", "pytest, Docker, Kubernetes, GitHub Actions CI/CD, Linux, Postman, Prometheus, Grafana, React.js, JavaScript (ES6+)"),
 ],
 "exp": [[
   "Scaled AEPS, MATM and VATM orchestration to <strong>500,000+ daily transactions</strong> at a <strong>99% success rate</strong>, by making the <strong>Django REST Framework</strong> payment path idempotent with request keys, backoff retries and nightly reconciliation.",
   "Took transaction query p95 down <strong>45%</strong> across <strong>PostgreSQL</strong> and <strong>MySQL</strong>, by partitioning the hot tables and adding covering indexes chosen from the query plan.",
   "Cleared <strong>35%</strong> of the peak-traffic backlog, by moving slow work off the request path onto <strong>Celery</strong> workers with <strong>Redis</strong> broking and idempotent task retries.",
   "Delivered live transaction status in under <strong>500ms</strong>, by streaming updates over <strong>FastAPI WebSockets</strong> instead of client polling.",
   "Contained a bad release to one service instead of the whole portal for <strong>2 million+ users</strong>, by moving monolithic web services onto async <strong>FastAPI</strong> and <strong>Django</strong> microservices behind a versioned REST gateway.",
   "Cut authentication latency <strong>50%</strong>, by issuing <strong>JWT</strong> access/refresh pairs with <strong>RBAC</strong> claims and caching OTP verification state in <strong>Redis</strong>.",
 ],[
   "Built a workforce telemetry and geofencing system for <strong>1,000+ field agents</strong> end to end, on <strong>FastAPI</strong> and async <strong>SQLAlchemy</strong> with <strong>Alembic</strong> migrations.",
   "Held <strong>99.9% uptime</strong> while absorbing <strong>10,000+ concurrent</strong> location pings, by batching writes through a <strong>Celery</strong> and <strong>Redis</strong> ingestion pipeline.",
   "Brought dashboard load time down <strong>30%</strong>, by wiring the <strong>React.js</strong> telemetry view to <strong>FastAPI WebSocket</strong> endpoints instead of polling.",
 ]],
 "projects": [
   ("DigiPay API Platform",
    "FastAPI service with versioned routers, correlation-ID request tracing, auth and rate-limit middleware and a documented deprecation policy, packaged with Docker and a CI pipeline. github.com/GitHub-akhilesh/Django_apis_digipay",
    "Python / FastAPI / PostgreSQL / Docker / GitHub Actions"),
   ("Polyglot Task Microservices",
    "Django REST API, Flask utility service and FastAPI notification service running side by side under Docker Compose with Kubernetes manifests, fronted by a React web client. github.com/GitHub-akhilesh/To-do-list-app",
    "Python / Django / Flask / FastAPI / Docker / Kubernetes"),
   ("Facial Recognition Attendance System",
    "Automated attendance capture in Python using OpenCV Haar Cascade and LBPH recognition, with MySQL persistence and Pandas-generated Excel reports. github.com/GitHub-akhilesh/automatic-attendance-through-face-detection",
    "Python / OpenCV / Pandas / Tkinter / MySQL"),
   ("Async Telemetry Ingestion &amp; Reporting Service",
    "FastAPI ingestion service with Celery and Redis task queues writing to partitioned PostgreSQL tables, plus Pandas reporting jobs over aggregated telemetry.",
    "Python / FastAPI / Celery / Redis / PostgreSQL / Pandas"),
 ],
 "certs": ["IIT Kanpur Cyber Security Certification"],
}

V4 = {  # ---------------- Software Engineer (generalist) ----------------
 "ats": "95",
 "title": "Software Development Engineer | Microservices &middot; Distributed Systems &middot; Full Stack",
 "summary": "Distributed systems for national e-governance and FinTech &mdash; 2 million+ users and 500,000+ transactions a day across Spring Boot, FastAPI and Node.js services. Cut p95 latency 45% across MySQL, PostgreSQL and MongoDB, lifted message throughput 35% on Kafka, and put every service behind Prometheus and Grafana. Hired and onboarded 4 engineers and moved the team onto Docker-based CI/CD.",
 "skills": [
   ("Languages", "Java, Python, JavaScript (ES6+), TypeScript, SQL, C++, HTML5, CSS3"),
   ("Backend &amp; Architecture", "Spring Boot, Django, FastAPI, Node.js, Express.js, React.js, Next.js, microservices, REST APIs, idempotency, rate limiting, WebSockets"),
   ("Data &amp; Messaging", "MySQL, PostgreSQL, MongoDB, Redis, Apache Kafka, Celery, Hibernate/JPA, sharding, partitioning, query tuning"),
   ("Testing, DevOps &amp; Observability", "pytest, JUnit, Jest, Docker, Kubernetes, GitHub Actions CI/CD, Linux, Jira, Prometheus, Grafana"),
 ],
 "exp": [[
   "Sustained <strong>500,000+ daily transactions</strong> at a <strong>99% success rate</strong> across AEPS, MATM and UPI, by making the settlement path idempotent with request keys, backoff retries and automated reconciliation.",
   "Cut p95 read/write latency <strong>45%</strong> across <strong>MySQL</strong>, <strong>PostgreSQL</strong> and <strong>MongoDB</strong>, by sharding and partitioning the hot tables and tuning the slowest queries against their plans.",
   "Contained a bad release to one service instead of the whole platform for <strong>2 million+ users</strong>, by splitting monolithic backends into <strong>Spring Boot</strong>, <strong>FastAPI</strong> and <strong>Node.js</strong> microservices behind a versioned gateway.",
   "Lifted message throughput <strong>35%</strong>, by moving inter-service work onto <strong>Apache Kafka</strong>, <strong>Celery</strong> and <strong>Redis</strong> with dead-letter handling for poison messages.",
   "Blocked <strong>99.9%</strong> of unauthorized access attempts, by adding <strong>JWT</strong> rotation, <strong>RBAC</strong>, device binding and OTP rate limiting across every payment entry point.",
   "Replaced a manual release process across all <strong>3</strong> payment platforms, by containerising every service with <strong>Docker</strong>, shipping through <strong>GitHub Actions</strong> and putting each one on <strong>Prometheus</strong> and <strong>Grafana</strong> dashboards.",
   "Improved team onboarding efficiency <strong>40%</strong>, by hiring and onboarding <strong>4 engineers</strong> and writing the runbooks and service documentation they start from.",
 ],[
   "Engineered a workforce telemetry platform for <strong>1,000+ field agents</strong> end to end &mdash; <strong>React.js</strong> front end, <strong>FastAPI</strong> backend, AWS deployment.",
   "Held <strong>99.9% uptime</strong> while processing <strong>10,000+ concurrent</strong> GPS pings, through a <strong>FastAPI</strong>, <strong>Celery</strong> and <strong>Redis</strong> ingestion pipeline.",
   "Brought dashboard load time down <strong>30%</strong>, by building the live map in <strong>React.js</strong> with <strong>Ant Design</strong> over a WebSocket feed instead of polling.",
 ]],
 "projects": [
   ("DigiPay Developer Platform",
    "Monorepo platform pairing a FastAPI service &mdash; versioned routers, correlation-ID tracing, auth and rate-limit middleware &mdash; with published SDK packages and embeddable React widgets. github.com/GitHub-akhilesh/Django_apis_digipay",
    "FastAPI / React / TypeScript / Docker / npm workspaces"),
   ("Polyglot Microservices Task Platform",
    "Django, Flask and FastAPI services orchestrated under Docker Compose with Kubernetes manifests, fronted by a React web client and a React Native mobile app. github.com/GitHub-akhilesh/To-do-list-app",
    "Django / Flask / FastAPI / React / React Native / Kubernetes"),
   ("Transaction Orchestration &amp; Ledger Platform",
    "Microservice platform orchestrating AEPS, MATM and UPI settlement with a transactional wallet ledger, idempotent retries, automated reconciliation and Kafka event fan-out.",
    "Spring Boot / FastAPI / Kafka / PostgreSQL / Redis"),
   ("LabX Design System",
    "Industrial data and visual automation project documented end to end &mdash; business case, HLD, LLD, data-flow and database design &mdash; and published as a live site. github.com/GitHub-akhilesh/labx-design",
    "Python / System Design / Technical Documentation / GitHub Pages"),
 ],
 "certs": ["IIT Kanpur Cyber Security Certification"],
}

VERSIONS = {"version1": V1, "version2": V2, "version3": V3, "version4": V4}
