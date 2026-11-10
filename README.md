# MLOPS 2026

## Introduction

The DevOps culture focuses on one goal throughout the entire software delivery lifecycle—not just development and operations: the rapid implementation of stable, high-quality software from concept to customer or user. The automation of software development, testing, and deployment through Continuous Delivery (CD) is a recognized key factor for DevOps, enabling faster implementation while ensuring necessary quality, security, and stability.   

Machine learning adds unique complexity to this traditional lifecycle. Because a machine learning model must be deployed to deliver real-world value, MLOps extends traditional DevOps principles and applies them to the data science realm, introducing structure and automation to model development, deployment, and ongoing monitoring and maintenance.

## Educational goals

- Discover the DevOps culture and its tooling ecosystem.
- Gain and share confidence in your code and operated systems.
- Maximize time-to-market, productivity, and security.
- Build robust and evolving applications and infrastructures.

## Prerequisites

Common computer skills and Linux basic knowledge.

## Modules

### Module 1: Fundamental knowledge

- Common tools
- Networking
- Programming tools
- Common Knowledge
- Languages

### Module 2: DevOps introduction

- Definition
- The reason to DevOps
- DevOps life cycle
- Site Reliability Engineering (SRE) implements DevOps
- SRE service levels
- SRE tools
- DevOps' history
- Agile vs Waterfall
- The Agile Manifesto
- Agile Principles
- Scrum
- Version management with SemVer
- Naming

### Module 3: Versioning with Git (SCM)

- Objectives
- Definition
- VCS motivations
- VCS Usages
- Semantic Versioning (SemVer)
- Centralized vs Distributed VCS
- Git: introduction
- Git: motivations
- Git: ecosystem
- Git: basic concepts
- Git: repository
- Git: common usage scenario
- Git: branching
- Git: branches merging
- Git: conflicts resolution
- Git: lab practicing
- Git: `.gitignore`
- Git: tagging
- Git best practices: use rebase instead of merge
- Git best practices: Conventional Commits
- Where can you use Git?
- Open-source project management

### Module 4: Continuous testing

- Benefits
- Types of tests
- Example
- Test coverage
- Test-driven development (TDD)
- TDD benefits
- Test automation
- Test writing best practices

### Module 5: Continuous Integration & Continuous Delivery (CI/CD)

- Simple deployment illustration
- Definitions
- Benefits
- CI/CD fundamentals
- CI/CD pipeline
- CI/CD platforms
- Registry deliveries

### Module 6: Containers with Docker

- The problems for developers
- Container definition
- Docker container
- Docker
- Container vs Virtual Machines vs Bare metal
- Docker architecture
- Docker components
- Example of a Docker workflow
- CLI commands
- Building Docker images
- Storage on Docker
- Running multi-container applications with Docker Compose
- Use cases
- Using Docker Compose
- Docker Compose example
- Docker Compose commands

### Module 7: Container orchestration with Kubernetes

- Requirements for Container-Based applications
- Container orchestration services
- Containers complexity
- Container orchestration tools
- Kubernetes
- Kubernetes cluster
- Kubernetes objects definitions
- Kubernetes object management
- Resource configuration organization
- Pod storage
- Networking
- Minikube

### Module 8: MLOps introduction

Course:

- Motivations
- What does it do?
- Why is it important?
- Data science landscape
- ML in research vs. production
- Challenges of deploying ML
- DevOps Principles
- MLOps Principles
- DevOps vs MLOps
- Different tasks (and definitions) of MLOps
- ML Lifecycle and Roles
- Tools
- Maturity levels of MLOps systems (according to Google)
- Real life applications

### Module 9: Data Versioning

Course:

- Git recap
- Data versioning
- Roadmap
- Problem definition
- Data versioning use cases
- Data is in the heart of any ML project
- Common data versioning solutions and their downsides
- What is DVC?
- Version extraction
- Practical example

Lab: Data versioning with DVC

- Version data using DVC
- Access the data in DVC using python API
- Access a specific version of the dataset

### Module 10: Data and Model Testing

Course: 

- Extension of 'Garbage in, garbage out' to ML systems
- Roadmap
- Tests everywhere
- ML pipeline testing
- Model testing
- Model evaluation
- Model validation
- Data testing
- Training-serving skew
- Tools
- PyTest

Lab: Testing

- Learn how to define a test function and how to write an assertion
- Learn the approach to data testing
- Learn the approach to feature engineering testing

Lab: CML

- Learn how to automate testing with Git and [CML](https://cml.dev/)
- Understand the processes that run after the Git Action workflow is triggered

### Module 11: Experiment tracking

Course:

- Motivations
- Roadmap
- Objectives
- Definition
- Basic concepts
- Practical example

Lab:

- Demonstrate how experiment tracking helps with linking the code, the results, and the environment details
- Note how this increases the reproducibility

### Module 12: Model deployment

Course: 

- Motivations
- Roadmap
- Vocabulary
- Deployment targets
- Latency constraints
- Deployment strategies
- Tests after deployment

Lab:

- Understand the steps of a model deployment
- Prepare and test the app locally
- Create a Docker container image

### Module 13: Monitoring

Course: 

- Motivations
- Roadmap
- Quick recap
- Extra layer of complexity
- System monitoring
- Data monitoring
- Model decay
- Stale models handling

Lab: Data drift detection and model degradation

- See a concrete example of data drift
- Learn how to detect and evaluate it

### Module 14: End-to-end ML platforms

Course:

- Architectural complexitiy
- Solution
- Platform comparison
- TensorFlow Extended (TFX)
- Comparison of the initial pipeline and TFX

Lab: TFX introduction

- Try out an example of end-to-end platform
- Deepen the notion of the pipeline and metadata
