# **Model Methods and Properties in Django**

## **1. Introduction**
Django models aren't just for defining database structure - they can also contain **business logic** through:
- **Model Methods** (functions that perform actions)
- **Model Properties** (computed fields that behave like attributes)

These keep related logic neatly encapsulated within the model (fat models, thin views).

---

## **2. Model Methods**
### **When to Use?**
- When you need to perform **actions** related to a model instance.
- Examples: Calculating totals, formatting data, triggering side effects.

### **Types of Model Methods**
#### **a) Standard Instance Methods**
```python
from django.db import models

class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def mark_as_paid(self):
        """Business logic to handle payment"""
        self.is_paid = True
        self.save()
        self.send_confirmation_email()  # Another custom method
```

**Usage:**
```python
order = Order.objects.get(id=1)
order.mark_as_paid()  # Updates DB and sends email
```

#### **b) `__str__()` Method (Recommended)**
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"
```
→ Used in Django admin and shell for readable representation.

#### **c) `get_absolute_url()` (For Detail Views)**
```python
from django.urls import reverse

class BlogPost(models.Model):
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
```
→ Lets templates use `{{ object.get_absolute_url }}`

---

## **3. Model Properties (`@property`)**
### **When to Use?**
- When you need **computed fields** that don't require DB storage.
- They behave like attributes (no parentheses needed).

### **Example: Age from Birthdate**
```python
from django.db import models
from datetime import date

class Person(models.Model):
    birth_date = models.DateField()

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
```

**Usage:**
```python
person = Person.objects.get(id=1)
print(person.age)  # No parentheses! Computed on access
```

### **Caching Properties with `@cached_property`**
```python
from django.utils.functional import cached_property

class Product(models.Model):
    @cached_property
    def expensive_calculation(self):
        # Simulate heavy computation
        return some_heavy_operation()
```
→ Calculated once per instance access.

---

## **4. Model Method Types Cheat Sheet**
| Type                  | Syntax                  | When to Use                     | Example                     |
|-----------------------|------------------------|--------------------------------|----------------------------|
| Instance Method       | `def method(self):`    | Action that modifies the model | `publish()`, `refund()`    |
| `__str__`            | `def __str__(self):`  | Human-readable representation  | `return self.name`         |
| `get_absolute_url`   | `def get_absolute_url(self):` | URL for detail views       | `reverse('view-name')`     |
| `@property`          | `@property def x(self):` | Computed attribute          | Age from birthdate         |
| `@cached_property`   | `@cached_property def x(self):` | Expensive computations | Cached API call result     |

---

## **5. Best Practices**
1. **Keep Business Logic in Models** (Fat models, thin views)
2. **Name Methods Verb-Noun** (`calculate_tax()` vs `tax()`)
3. **Use `@property` for Derived Data** (Fields that don't need storage)
4. **Add Type Hints for Clarity** (Python 3.6+):
   ```python
   def get_price_with_vat(self) -> float:
       return float(self.price * 1.2)
   ```

---

## **6. Practical Example: E-Commerce Model**
```python
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('Product', through='OrderItem')
    
    @property
    def total(self) -> float:
        """Calculates order total by summing items"""
        return sum(item.price for item in self.items.all())
    
    def apply_discount(self, percent: float):
        """Applies discount to all items"""
        for item in self.orderitem_set.all():
            item.price *= (1 - percent/100)
            item.save()
    
    def __str__(self):
        return f"Order #{self.id} (${self.total})"
```

---

## **7. Common Pitfalls**
1. **DB Hits in Loops**:
   ```python
   # BAD: N+1 queries
   for order in Order.objects.all():
       print(order.total)  # Hits DB for items each time
   
   # GOOD: Prefetch related
   for order in Order.objects.prefetch_related('items').all():
       print(order.total)
   ```
2. **Overusing `@property`** - Don't put heavy computations here without caching.

---

## **8. Further Reading**
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Python Properties Guide](https://realpython.com/python-property/)
- [Django Model Best Practices](https://steelkiwi.com/blog/best-practices-working-django-models-python/)
