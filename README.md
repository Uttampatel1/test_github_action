
# 🚀 Learn GitHub Actions

This repository is designed to help you understand and experiment with GitHub Actions. GitHub Actions is a powerful tool that allows you to automate, customize, and execute software development workflows directly in your GitHub repository.

## 📚 Table of Contents

-   [📖 Introduction](#introduction)
-   [🚀 Getting Started](#getting-started)
    -   [🔧 Prerequisites](#prerequisites)
-   [💡 Understanding GitHub Actions](#understanding-github-actions)
    -   [❓ What is GitHub Actions?](#what-is-github-actions)
    -   [📚 Key Concepts](#key-concepts)
    -   [📝 Basic Workflow Structure](#basic-workflow-structure)
-   [💻 Examples](#examples)
    -   [👋 Example 1: Hello World Action](#example-1-hello-world-action)
    -   [🔄 Example 2: Continuous Integration (CI)](#example-2-continuous-integration-ci)
-   [📖 Useful Resources](#useful-resources)
-   [🤝 Contributing](#contributing)
-   [📜 License](#license)

## 🎯 Introduction

GitHub Actions enables you to automate your software workflows, such as continuous integration (CI) and continuous deployment (CD). This repository provides examples and exercises to help you learn how to use GitHub Actions effectively.

## 🚀 Getting Started

### ✅ Prerequisites

To follow along with the examples and tutorials in this repository, you will need:

- A GitHub account
- Basic knowledge of Git and version control
- Familiarity with YAML syntax (optional, but helpful)



## 🤖 Understanding GitHub Actions

### ❓ What is GitHub Actions?

GitHub Actions is a CI/CD platform that allows you to automate tasks within your software development lifecycle. With GitHub Actions, you can create workflows that build, test, and deploy your code right from GitHub.

### 🗝️ Key Concepts

- **Workflow**: A configurable automated process that will run one or more jobs.
- **Job**: A set of steps that execute on the same runner.
- **Step**: A task that runs commands in a job.
- **Runner**: The machine that runs your jobs (e.g., Ubuntu, Windows, macOS).
- **Event**: Triggers that start a workflow (e.g., push, pull request, cron).

### 🧩 Basic Workflow Structure

Here's a simple example of a GitHub Actions workflow:

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm install

    - name: Run tests
      run: npm test
```

This workflow runs every time you push or create a pull request. It checks out your code, sets up Node.js, installs dependencies, and runs tests.

## 💡 Examples

### 👋 Example 1: Hello World Action

This is a simple example of a custom GitHub Action that prints "Hello, World!".

1. **Create an action file:**
   ```yaml
   name: Hello World

   on: [push]

   jobs:
     say_hello:
       runs-on: ubuntu-latest
       steps:
       - name: Print Hello World
         run: echo "Hello, World!"
   ```

2. **Commit and push the file to your repository.** The action will automatically run when you push changes.

### 🔄 Example 2: Continuous Integration (CI)

A basic CI pipeline that runs tests whenever code is pushed to the repository.

1. **Create a CI workflow:**
   ```yaml
   name: CI

   on: [push]

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
       - name: Checkout code
         uses: actions/checkout@v2

       - name: Set up Node.js
         uses: actions/setup-node@v2
         with:
           node-version: '14'

       - name: Install dependencies
         run: npm install

       - name: Run tests
         run: npm test
   ```

2. **Push to your repository** and see the workflow in action.

## 🔗 Useful Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [GitHub Actions Examples](https://github.com/actions/examples)
- [Learning Lab: GitHub Actions](https://lab.github.com/githubtraining/github-actions:-hello-world)


