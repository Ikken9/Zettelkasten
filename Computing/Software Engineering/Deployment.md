# Deployment


## **CI/CD**
Stands for continuous integration and continuous delivery/deployment, aims to streamline and accelerate the software development lifecycle.

[Continuous integration](https://www.redhat.com/en/topics/integration?cicd=32h281b "Red Hat | Understanding enterprise integration") (CI) refers to the practice of [automatically](https://www.redhat.com/en/topics/automation?cicd=32h281b "Understanding automation") and frequently integrating code changes into a shared source code repository. [Continuous delivery](https://www.redhat.com/en/topics/devops/what-is-continuous-delivery?cicd=32h281b "What is continuous delivery?") and/or deployment (CD) is a 2 part process that refers to the integration, testing, and delivery of code changes. Continuous delivery stops short of automatic production deployment, while continuous deployment automatically releases the updates into the production environment.

Helps organizations avoid bugs and code failures while maintaining a continuous cycle of software development and updates.   
  
As apps grow larger, features of CI/CD can help decrease complexity, increase efficiency, and streamline workflows.

Because CI/CD automates the manual human intervention traditionally needed to get new code from a commit into production, downtime is minimized and code releases happen faster. And with the ability to more quickly integrate updates and changes to code, user feedback can be incorporated more frequently and effectively, meaning positive outcomes for end users and more satisfied customers overall.


## Deployment Patterns

#### **Canary releases**
A canary release is a method of spotting possible issues before they affect all consumers. Before making a new feature available to everyone, the plan is only to show it to a select group of users. We monitor what transpires after the feature is available in a canary release. If there are issues with the release, we fix them. We transfer the canary release to the actual production environment once its stability has been established.

#### **Blue/green deployments**
Here we have run two similar environments simultaneously, lowering risk and downtime. These surroundings are referred to be blue and green. Only one of the environments is active at any given moment. A router or load balancer that aids in traffic control is used in a blue-green implementation. The blue/green deployment also provides a quick means of performing a rollback. We switch the router back to the blue environment if anything goes wrong in the green environment.

#### **Feature toggles**
Here we can turn a switch on/off with feature toggles at runtime. We may roll out new software without exposing our users to any other brand-new or modified functionality. When we build new functionality, we can use feature toggles to enable continuous deployments by splitting releases from deployments.

#### **A/B testing**
Two versions of an app are compared using A/B testing to see which one performs better. An experiment is like A/B testing. In A/B testing, we randomly present users with two or more page versions. Then, we use statistical analysis to determine which variant is more effective in achieving our objectives.

#### **Dark launches**
In a "dark launch," we introduce a new feature to a select group of users rather than the general public. These users must be aware that they are helping us test the functionality. We need to point out the new functionality to them. It is nicknamed a "dark launch" for this reason. Users are introduced to the program to get feedback and test its effectiveness.