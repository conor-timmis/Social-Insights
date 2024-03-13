# [SOCIAL INSIGHTS](https://social-insights-5fd3e17a0651.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/conor-timmis/Social-Insights)](https://github.com/conor-timmis/Social-Insights/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/conor-timmis/Social-Insights)](https://github.com/conor-timmis/Social-Insights/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/conor-timmis/Social-Insights)](https://github.com/conor-timmis/Social-Insights)


Welcome to Social Insights, a survey about Social Media and how it affects people. I made this survey to understand better how social media addiction impacts lives, especially since the pandemic. Many people, especially younger ones, seem to spend a lot of time on their phones instead of living in the real world.

At first, I've asked basic questions, but I plan to ask more detailed ones later to get better information.

Once I have enough data, I hope to figure out what's wrong with the internet today. It often feels like the internet controls us, our behaviour and shows us what it wants us to see based on algorithms.


![screenshot](documentation/preview.png)


## UX


My design process focused on creating a straightforward user experience by keeping the program's flow as linear as possible. Initially, users are prompted to provide essential information such as their name, age, and screen time. This will make for comparing/categorising easier in future development. Then from there the user will be asked questions with are somewhat categorised by how they operate, so I have implemented a couple of yes or no questions, then it leads onto the scale of 1-10 questions, then into the multiple choice questions which have been marked as A, B or C to answer.


## Features


### Existing Features

- **{{ Inputs }}**

    - Inputs are to be used to answer the questions, and they are also gated behind other functions to stop people from mis-answering questions e.g Numbers being used in the Name Question will loop so you have to answer appropriately.

![screenshot](documentation/features/inputs.png)

- **{{ Scale Questions }}**

    - The Scale Questions are in junction with the Scale function to make sure you can answer with numbers 1 through 10 depending on your answer and making sure you cannot input any other way.

![screenshot](documentation/features/scaleqs.png)

- **{{ Multiple Choice Questions }}**

    - Multiple choice questions allow the user to choose a different answer between the 3 given using A, B or C, to switch things up from the norm.

![screenshot](documentation/features/mpchoice.png)

- **{{ Feedback }}**

    - The feedback feature is based on how you as a user answer the questions. If you are someone who answers based on a lot of usage of social media, it will feedback one way, same with the opposite and even a middle ground feedback.

![screenshot](documentation/features/feedback.png)


### Future Features


- {{ Comparisons }}
    - I would like to implement a way to compare how your answers based on your age compare with other people within your age bracket, e.g 19-24 year olds with 9 hour screen times but you have 2 hours.
- {{ Charts }}
    - I'd like a way for people to access the API in a way where they can view peoples answers in averages between ages too, possibly within bar or pie charts.
- {{ Usage Tracker }}
    - I would like to implement a way where users as well as myself can access how many people have gave answers over the entirety of the surveys lifetime.


## Tools & Technologies Used


- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![Git](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.