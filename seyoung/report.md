---
title: Parallel Test Case Prioritization for Distributed System Using Search Algorithms
author: |
  | Team 6
  | Seyoung Song, Subeom Park, Yoonho Nam, Azret Kenzhaliev
# citation
bibliography: report.bib
citation-style: ieee
link-citations: true
# number section heading
numbersections: true
# table-of-contents
toc: true
# size
papersize: A4
geometry: margin=2cm
# font
fontsize: 12pt
mainfont: Latin Modern Roman
mathfont: Latin Modern Math
monofont: Hack Nerd Font Mono
CJKmainfont: Noto Serif CJK KR
# abstract
abstract: Abstract (by Seyoung)
---

# Introduction

- Regression Test Case Prioritization
- Parallel Test Prioritization
- Parallel Test Prioritization, but different CPU

# Problem Description (by Subeom)

TODO: describe the problem (Parallel Test Prioritization)

- Problem Description
- Problem Definition
- Effectiveness Measure

# Algorithms

TODO: describe your approach

## Greedy Algorithms (by Azret)

## Simulated Annealing (by Subeom)

## Genetic Algorithms (by Yoonho)

# Experimental Design (by Seyoung)

## Research Questions

- RQ1: Which algorithm is most effective in solving the parallel test prioritization problem?
- RQ2: How do the number of computing resources and the relative performance between them influence the performance of the parallel test prioritization techniques?

\pagebreak

## Subjects

| **ID** | **Subjects**        | **SLOC** | **#Test** | **Time (s)** |
| -----: | :------------------ | -------: | --------: | -----------: |
|      1 | commons-cli         |     9053 |       192 |        3.064 |
|      2 | dictomaton          |     4318 |        53 |       14.067 |
|      3 | disklrucache        |     1921 |        61 |        2.364 |
|      4 | efflux              |     5633 |        40 |        0.581 |
|      5 | exp4j               |     5699 |       311 |       11.350 |
|      6 | gdx-artemis         |     3607 |        35 |        0.483 |
|      7 | geojson-jackson     |     1569 |        60 |        1.284 |
|      8 | gson-fire           |     3566 |        91 |        3.249 |
|      9 | jactor              |     6984 |        60 |       11.628 |
|     10 | jadventure          |     5276 |        74 |        2.311 |
|     11 | jarchivelib         |     2256 |        33 |        0.217 |
|     12 | java-faker          |     8541 |       571 |       34.154 |
|     13 | java-uuid-generator |     4321 |        46 |        0.937 |
|     14 | javapoet            |     9874 |       346 |       15.323 |
|     15 | jsonassert          |     3476 |       150 |        1.641 |
|     16 | jumblr              |     2970 |       103 |        0.905 |
|     17 | lastcalc            |     7271 |        34 |       13.672 |
|     18 | low-gc-membuffers   |    13099 |        51 |        1.784 |
|     19 | metrics             |     6493 |        76 |       43.964 |
|     20 | mp3agic             |    10037 |       495 |        4.815 |
|     21 | nv-websocket-client |     8617 |        73 |        1.014 |
|     22 | protoparser         |     5545 |       171 |        4.752 |
|     23 | restfixture         |     8243 |       290 |        6.716 |
|     24 | skype-java-api      |     9749 |        24 |       15.720 |
|     25 | stateless4j         |     2728 |        88 |        2.146 |
|     26 | stream-lib          |     8756 |       142 |      443.206 |
|     27 | xembly              |     3030 |        63 |        6.834 |

Table: Open-source subjects from GitHub

\pagebreak

## Settings

1. Sequential Test Prioritization
   - $c = \{1\}$
2. Parallel Test Prioritization
   - $c = \{2, 4, 8, 16\}$
3. Asymmetric Test Prioritization
   - $1:2$
   - $1:3$
   - $1:4$
   - $1:1:1:1:4:4:4:4$

| Computing Scenario                                 | Relative Performances                            |
| :------------------------------------------------- | :----------------------------------------------- |
| Sequential Test Prioritization                     | [1]                                              |
| Parallel Test Prioritization ($c=2$)               | [1, 1]                                           |
| Parallel Test Prioritization ($c=4$)               | [1, 1, 1, 1]                                     |
| Parallel Test Prioritization ($c=8$)               | [1, 1, 1, 1, 1, 1, 1, 1]                         |
| Parallel Test Prioritization ($c=16$)              | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| Asymmetric Test Prioritization ($1:2$)             | [1, 2]                                           |
| Asymmetric Test Prioritization ($1:3$)             | [1, 3]                                           |
| Asymmetric Test Prioritization ($1:4$)             | [1, 4]                                           |
| Asymmetric Test Prioritization ($1:1:1:1:4:4:4:4$) | [1, 1, 1, 1, 4, 4, 4, 4]                         |

Table: An example of computing scenarios

| **Performance of Computing Resources $p$** |
| :----------------------------------------- |
| Sequential ($c=1$)                         |
| Parallel ($c=2$)                           |
| Parallel ($c=4$)                           |
| Asymmetric ($1:3$)                         |
| Asymmetric ($1:1:2$)                       |
| Asymmetric ($2:2$)                         |
| Parallel ($c=8$)                           |
| Asymmetric ($1:7$)                         |
| Asymmetric ($2:6$)                         |
| Asymmetric ($3:5$)                         |
| Asymmetric ($4:4$)                         |
| Asymmetric ($2:2:2:2$)                     |
| Asymmetric ($1:1:3:3$)                     |
| Parallel ($c=12$)                          |
| Parallel ($c=25$)                          |
| Parallel ($c=50$)                          |
| Parallel ($c=100$)                         |
| Parallel ($c=200$)                         |

Table: Settings for additional experiments

| **Time Constraint $TC$** |
| :----------------------- |
| $1.25$                   |
| $1.5$                    |
| $1.75$                   |
| $2.0$                    |

Table: Settings for additional experiments

# Evaluation Results

TODO: describe the evaluation results

## Greedy Algorithms (by Azret)

## Simulated Annealing (by Subeom)

## Genetic Algorithms (by Yoonho)

## Comparison (by Seyoung)

| **Setting**                    |    **GA** | **SA** | **AGA** |
| ------------------------------ | --------: | -----: | ------: |
| Sequential                     | **0.932** |  0.868 |   0.876 |
| Parallel ($c=2$)               | **0.964** |  0.936 |   0.937 |
| Parallel ($c=4$)               | **0.980** |  0.966 |   0.966 |
| Parallel ($c=8$)               | **0.987** |  0.981 |   0.981 |
| Parallel ($c=16$)              | **0.990** |  0.988 |   0.988 |
| Asymmetric ($1:2$)             | **0.976** |  0.955 |   0.958 |
| Asymmetric ($1:3$)             | **0.982** |  0.963 |   0.968 |
| Asymmetric ($1:4$)             | **0.985** |  0.968 |   0.975 |
| Asymmetric ($1:1:1:1:4:4:4:4$) | **0.995** |  0.992 |   0.993 |

# Conclusion

- Discussion
  - Comparison With Sequential Test Prioritization
  - Practical Concerns
  - Generalizability
- Comments from Professor
  - How long should the entire test take for there to be real gains in prioritization?
  - The time gain from prioritization becomes smaller as the number of compute resources increases, so it may not be meaningful if you already have a lot of compute resources.

\pagebreak

References: [@li_search_2007; @chen_optimizing_2018; @luo_how_2019; @zhou_parallel_2021]

# References