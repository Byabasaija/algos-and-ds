## Palindrome Check

**Question:**  
Given a string, write a function to determine whether it is a palindrome, considering only alphanumeric characters and ignoring cases.

### Examples

Input: "A man, a plan, a canal: Panama" Output: true

Input: "race a car" Output: false


**Note:**  
- An empty string is considered a valid palindrome.

---

## Test Cases

| Input                             | Expected Output |
|----------------------------------|-----------------|
| `""`                             | `true`          |
| `" "`                            | `true`          |
| `"a"`                            | `true`          |
| `"ab"`                           | `false`         |
| `"A man, a plan, a canal: Panama"` | `true`        |
| `"race a car"`                   | `false`         |
| `"No lemon, no melon"`           | `true`          |
| `"Was it a car or a cat I saw?"` | `true`          |
| `"12321"`                        | `true`          |
| `"123ab321"`                     | `false`         |
