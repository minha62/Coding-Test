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

## Basic Aggregate Functions
### 620. Not Boring Movies
```sql
select * from cinema where mod(id,2)=1 and description<>'boring' order by rating desc;
```
