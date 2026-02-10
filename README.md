# Chapter 9 – File I/O (Python)

Random Access Memory (RAM) is **volatile**, which means all data is lost once a program terminates.  
To **store data permanently**, we use **files**.

A **file** is data stored on a storage device.  
Python programs can interact with files by **reading** data from them and **writing** data to them.

---

## Types of Files

There are mainly **two types of files**:

1. **Text Files**  
   Examples: `.txt`, `.c`, `.py`

2. **Binary Files**  
   Examples: `.jpg`, `.png`, `.dat`

---

## File Handling in Python

Python provides many built-in functions to:
- Read files
- Write files
- Update files
- Delete files

---

## Opening a File

Python uses the `open()` function to open a file.

### Syntax
```python
open("filename", "mode")   # mode is optional (default is read mode)
```

### Example
```python
open("this.txt", "r")
```

---

## Reading a File in Python

### Example
```python
# Open the file in read mode
f = open("this.txt", "r")

# Read its contents
text = f.read()

# Print the contents
print(text)

# Close the file
f.close()
```

> Always close the file after use to free system resources.

---

## Other Methods to Read a File

### Read One Line at a Time
```python
f.readline()
```

- Reads a **single line** from the file each time it is called.

---

## Modes of Opening a File

| Mode | Description |
|-----|------------|
| `r` | Read mode |
| `w` | Write mode |
| `a` | Append mode |
| `+` | Update (read & write) |
| `rb` | Read in binary mode |
| `rt` | Read in text mode |

---

## Writing Files in Python

To write data to a file:
1. Open the file in **write (`w`)** or **append (`a`)** mode
2. Use `write()` method

### Example
```python
# Open the file in write mode
f = open("this.txt", "w")

# Write content to the file
f.write("this is nice")

# Close the file
f.close()
```

⚠️ **Note:**  
- `w` mode **overwrites** the file if it already exists.

---

## The `with` Statement

The **best and safest way** to work with files is using the `with` statement.

- Automatically closes the file
- Cleaner and safer code

### Example
```python
with open("this.txt", "r") as f:
    text = f.read()
    print(text)
```

---

## Practice Set – Chapter 9

1. Write a program to read a file **`poems.txt`** and check whether it contains the word **"twinkle"**.
2. A `game()` function returns a score.  
   Read **`Hi-score.txt`** and update it whenever a new high score is achieved.
3. Generate multiplication tables from **2 to 20** and store them in **different files** inside a folder for a 13-year-old.
4. Replace the word **"Donkey"** with `#####` wherever it appears in a file.
5. Repeat question 4 for a **list of censored words**.
6. Write a program to scan a **log file** and check whether it contains the word **"python"**.
7. Find the **line number** where the word **"python"** appears.
8. Write a program to **copy** the contents of a file **`this.txt`** to another file.
9. Check whether **two files are identical**.
10. Write a program to **wipe out the contents** of a file.
11. Rename a file to **`renamed_by_python.txt`**.

---

## Key Takeaways

- Files allow **permanent data storage**
- `open()` is used to access files
- Always close files or use `with`
- Different modes control file behavior
- Python makes file handling simple and powerful

---

Happy Coding 🚀  
Practice File I/O regularly to master real-world Python programs!
