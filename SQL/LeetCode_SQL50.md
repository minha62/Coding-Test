## SELECT
### 1757. Recyclable and Low Fat Products
```sql
select product_id from Products where low_fats='Y' and recyclable='Y';
```

### 584. Find Customer Referee
```sql
select name from Customer where referee_id!=2 or referee_id is null
```

### 595. Big Countries
```sql
select name, population, area from World where area>=3000000 or population>=25000000;
```

### 1148. Article Views I
```sql
select distinct(author_id) id from Views where author_id=viewer_id  order by id asc;
```

### 1683. Invalid Tweets
```sql
select tweet_id from Tweets where length(content)>15;
```

<br>

## Basic Joins
### 1378. Replace Employee ID With The Unique Identifier
```sql
select unique_id, name
from Employees left outer join EmployeeUNI
using (id);
```

### 1068. Product Sales Analysis I
```sql
select product_name, year, price
from Sales natural join Product;
```
```sql
select product_name, year, price
from Sales inner join Product
using (product_id);
```

### 🐳 1581. Customer Who Visited but Did Not Make Any Transactions 🐳
```sql
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;
```
```sql
SELECT customer_id, count(*) AS count_no_trans
FROM Visits v LEFT OUTER JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;
```


<br>

## Basic Aggregate Functions
### 620. Not Boring Movies
```sql
select * from cinema where mod(id,2)=1 and description<>'boring' order by rating desc;
```



<br>

## Sorting and Grouping

### 2356. Number of Unique Subjects Taught by Each Teacher

```sql
select teacher_id, count(distinct subject_id) cnt from Teacher group by teacher_id;
```
