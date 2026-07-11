# AI/ML Internship — Home Assignment 01

Beginner Python assignments from my AI/ML internship, covering rule-based systems that simulate unsupervised learning concepts using plain Python (no external ML libraries).

## Assignment: Movie Recommendation System

A rule-based system that groups user behavior and recommends movies based on watched genres — simulating how real-world recommendation engines work, but using basic Python data structures instead of ML models.

### Tasks Implemented
1. **Search a user** — find a user by name and display their watched genres.
2. **Predict/Recommend a movie** — suggest a movie based on each genre the user watched.
3. **Count users by pattern** — count how many users watched a specific genre (e.g., Action).
4. **Find the most common genre** — identify the most-watched genre across all users.

### Bonus: Common Applications of Clustering (Simulated with Rules)
Since real clustering algorithms weren't covered yet, these are simulated using basic Python logic (loops, dictionaries, sets):

- **Customer Segmentation** — buckets customers into High/Medium/Low value using spend thresholds.
- **Product Recommendation** — recommends products based on overlapping purchases between users.
- **Market Basket Analysis** — finds which products are most frequently bought together.
- **Fraud Detection (Pattern Discovery)** — flags transactions that are unusually high compared to a user's average spend.

## AI Concept

This is a **rule-based system**, not a machine learning model. It uses predefined `if/else` logic and dictionary lookups to make decisions, rather than learning patterns from data automatically (which is what real unsupervised learning / clustering algorithms like K-Means do).

## How to Run

```bash
python movie_recommendation_homework.py
```

You'll be prompted to enter a user name — try `Rahul`, `Anita`, or `Riya` (the sample users in the dataset).

## Tech Used
- Python 3 (no external libraries — only built-in `itertools`)
