---
title: Parallel Test Case Prioritization for Distributed System Using Search Algorithms
author: |
  | Team 6
  | Seyoung Song, Subeom Park, Yoonho Nam, Azret Kenzhaliev
papersize: A4
geometry: margin=2cm
fontsize: 12pt
mainfont: Latin Modern Roman
mathfont: Latin Modern Math
monofont: Hack Nerd Font Mono
CJKmainfont: Noto Serif CJK KR
---

# Abstract

TODO

# 1. Introduction

- Regression Test Case Prioritization
- Parallel Test Prioritization
- Parallel Test Prioritization, but different CPU

# 2. Parallel Test Prioritization

- Problem Description
- Problem Definition
- Effectiveness Measure

# 3. Algorithms

## 3.1. Greedy Algorithms

TODO

## 3.2. Simulated Annealing

TODO

## 3.3. Genetic Algorithms

TODO

# 4. Empirical Study

## 4.1. Research Questions

- RQ1: Which algorithm is most effective in solving the parallel test prioritization problem?
- RQ2: How do the number of computing resources and the relative performance between them influence the performance of the parallel test prioritization techniques?

## 4.2. Experimental Design

1. Sequential Test Prioritization
   - $c = \{1\}$
2. Parallel Test Prioritization
   - $c = \{2, 4, 8, 16\}$
3. Asymmetric Test Prioritization
   - $1:2$
   - $1:3$
   - $1:4$
   - $1:1:1:1:4:4:4:4$

| Computing Scenario                                 | relative performances $p$                        |
| -------------------------------------------------- | ------------------------------------------------ |
| Sequential Test Prioritization                     | [1]                                              |
| Parallel Test Prioritization ($c=2$)               | [1, 1]                                           |
| Parallel Test Prioritization ($c=4$)               | [1, 1, 1, 1]                                     |
| Parallel Test Prioritization ($c=8$)               | [1, 1, 1, 1, 1, 1, 1, 1]                         |
| Parallel Test Prioritization ($c=16$)              | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| Asymmetric Test Prioritization ($1:2$)             | [1, 2]                                           |
| Asymmetric Test Prioritization ($1:3$)             | [1, 3]                                           |
| Asymmetric Test Prioritization ($1:4$)             | [1, 4]                                           |
| Asymmetric Test Prioritization ($1:1:1:1:4:4:4:4$) | [1, 1, 1, 1, 4, 4, 4, 4]                         |

## 4.3. Subjects

TODO: Seyoung

27 Java Projects

## 4.4. Results and Analysis

TODO

# 5. Conclusion

- Discussion
  - Comparison With Sequential Test Prioritization
  - Practical Concerns
  - Generalizability
- Comments from Professor
  - How long should the entire test take for there to be real gains in prioritization?
  - The time gain from prioritization becomes smaller as the number of compute resources increases, so it may not be meaningful if you already have a lot of compute resources.

# References

[1] Z. Li, M. Harman, and R. M. Hierons, “Search Algorithms for Regression Test Case Prioritization,” IIEEE Trans. Software Eng., vol. 33, no. 4, pp. 225–237, Apr. 2007, doi: 10.1109/TSE.2007.38.

[2] J. Chen et al., “Optimizing test prioritization via test distribution analysis,” in Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering, Lake Buena Vista FL USA, Oct. 2018, pp. 656–667. doi: 10.1145/3236024.3236053.

[3] Q. Luo, K. Moran, L. Zhang, and D. Poshyvanyk, “How Do Static and Dynamic Test Case Prioritization Techniques Perform on Modern Software Systems? An Extensive Study on GitHub Projects,” IIEEE Trans. Software Eng., vol. 45, no. 11, pp. 1054–1080, Nov. 2019, doi: 10.1109/TSE.2018.2822270.

[4] J. Zhou, J. Chen, and D. Hao, “Parallel Test Prioritization,” ACM Trans. Softw. Eng. Methodol., vol. 31, no. 1, Sep. 2021, doi: 10.1145/3471906.
