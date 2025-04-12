# **Model Relationships in Django**  

## **1. Introduction**  
In Django, models represent database tables, and relationships define how these models interact with each other. Django supports three main types of relationships:  
- **One-to-One (OneToOneField)**  
- **Many-to-One (ForeignKey)**  
- **Many-to-Many (ManyToManyField)**  

Understanding these relationships is crucial for designing efficient database schemas.  

---

## **2. Types of Relationships**  

### **2.1 One-to-One Relationship (`OneToOneField`)**  
- Used when one record in a model is related to exactly one record in another model.  
- Example: A `User` and a `Profile` (each user has only one profile).  

#### **Syntax:**  
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

#### **Key Points:**  
- `on_delete=models.CASCADE` ensures that if a `User` is deleted, their `Profile` is also deleted.  
- Access related objects using:  
  ```python
  user = User.objects.get(id=1)
  profile = user.profile  # Access profile from user
  ```

---

### **2.2 Many-to-One Relationship (`ForeignKey`)**  
- Used when one model can be referenced by multiple instances of another model.  
- Example: A `Author` can have multiple `Book`s.  

#### **Syntax:**  
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

#### **Key Points:**  
- `on_delete` specifies behavior when the referenced object is deleted (`CASCADE`, `PROTECT`, `SET_NULL`, etc.).  
- Access related objects using:  
  ```python
  author = Author.objects.get(id=1)
  books = author.book_set.all()  # All books by this author
  ```

---

### **2.3 Many-to-Many Relationship (`ManyToManyField`)**  
- Used when multiple records in one model relate to multiple records in another model.  
- Example: A `Student` can enroll in multiple `Course`s, and a `Course` can have many students.  

#### **Syntax:**  
```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```

#### **Key Points:**  
- Django automatically creates an intermediary join table.  
- Access related objects using:  
  ```python
  course = Course.objects.get(id=1)
  students = course.students.all()  # All students in this course
  ```

---

## **3. Advanced Relationship Options**  

### **3.1 `related_name` Attribute**  
- Used to specify a custom name for reverse relations.  
- Example:  
  ```python
  class Book(models.Model):
      author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
  ```
  Now, instead of `author.book_set.all()`, use `author.books.all()`.  

### **3.2 `through` Model (Custom Intermediate Table)**  
- Used to add extra fields to a `ManyToManyField`.  
- Example:  
  ```python
  class Enrollment(models.Model):
      student = models.ForeignKey(Student, on_delete=models.CASCADE)
      course = models.ForeignKey(Course, on_delete=models.CASCADE)
      date_enrolled = models.DateField()

  class Course(models.Model):
      students = models.ManyToManyField(Student, through="Enrollment")
  ```

---

## **4. Best Practices**  
1. **Use `related_name`** for clarity in reverse lookups.  
2. **Choose `on_delete` carefully** to avoid unintended data loss.  
3. **Optimize queries** using `select_related` (for `ForeignKey`) and `prefetch_related` (for `ManyToManyField`).  

---

## **5. Summary Table**  

| Relationship       | Field Type         | Example Use Case          | Reverse Access          |
|--------------------|--------------------|--------------------------|-------------------------|
| One-to-One         | `OneToOneField`    | User ↔ Profile           | `user.profile`          |
| Many-to-One        | `ForeignKey`       | Author ↔ Book            | `author.book_set.all()` |
| Many-to-Many       | `ManyToManyField`  | Student ↔ Course         | `course.students.all()` |

---
