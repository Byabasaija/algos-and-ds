# Problem Statement

You are given an array of integers representing the scores of students in a class. Each student can have multiple scores, and the array might contain scores of different students grouped together. Your task is to sort this array such that for each student's scores, the scores are sorted in ascending order, but the groups of scores for different students remain in the same order they appeared in the original array.

Additionally, you are given another array of the same length that represents the student IDs corresponding to each score in the first array. You should ensure that the scores are sorted correctly for each student, without changing the relative order of students in the array.

## Input

- An integer array `scores` of length `n` where `1 <= n <= 10^4`.
- An integer array `studentIds` of length `n` where `1 <= studentIds[i] <= 100`.

## Output

- An integer array of sorted scores as per the described rules.

## Example

```text
Input:
scores = [50, 40, 60, 30, 70, 20]
studentIds = [1, 1, 1, 2, 2, 2]

Output:
[40, 50, 60, 20, 30, 70]

```

## Constraints
You must sort the scores in-place.
You must not use any built-in sorting functions.

