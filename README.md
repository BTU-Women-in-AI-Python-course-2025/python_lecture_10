# Django

- **Model Relationships**:
  - ForeignKey - https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
  - ManyToManyField - https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_many/
  - OneToOneField - https://docs.djangoproject.com/en/5.1/topics/db/examples/one_to_one/
- **Select related** - https://docs.djangoproject.com/en/5.1/ref/models/querysets/#select-related
- **Prefetch related** - https://docs.djangoproject.com/en/5.1/ref/models/querysets/#prefetch-related
- **Model Methods and Properties**:
  - Model Methods - https://docs.djangoproject.com/en/5.1/topics/db/models/#model-methods
  - Model Properties - https://docs.djangoproject.com/en/5.1/glossary/#term-property


# 📚 Django Model Relationships, Methods, and Properties

## Tasks

### Task 1: Creating a ForeignKey Relationship
1. **Create two models:** `Author` and `Book`.
2. **In the `Book` model,** add a `ForeignKey` field to the `Author` model.
3. **Write a method** in the `Author` model that returns the number of books associated with the author.
4. **Test your models** by creating a few authors and books, then check the method.

### Task 2: Implementing a ManyToManyField
1. **Create two models:** `Student` and `Course`.
2. **In the `Student` model,** add a `ManyToManyField` to the `Course` model.
3. **Write a method** in the `Student` model that lists all the courses a student is enrolled in.
4. **Test your models** by enrolling students in different courses and calling the method.

### Task 3: Using Model Properties
1. **Add a `date_of_birth` field** to the `Student` model.
2. **Create a property** in the `Student` model that calculates and returns the student’s age.
3. **Test your property** by creating a student with a specific date of birth and checking if the age is calculated correctly.
