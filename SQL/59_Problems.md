> 출처: [하범핀 블로그](https://blog.naver.com/PostView.naver?blogId=tkdqja8643&logNo=221317891450)

1. 덧셈연산자 이용. 모든 사원에 대해 $300 급여 인상 계산. 사원명/급여/인상된급여 출력
```sql
SELECT ENAME 사원명, SAL 급여, SAL+300 인상된급여
FROM EMP;
```

2. 사원명/급여/연간총수입을 총 수입이 많은 것부터 작은 순으로 출력. 연간 총 수입은 급여*12+100
```sql
SELECT ENAME 사원명, SAL 급여, SAL*12+100 연간_총_수입
FROM EMP
ORDER BY SAL DESC;
```
   _연간총수입순으로 정렬하는 건 급여순으로 정렬하는 것이랑 동일_

3. 급여가 2000이 넘는 사원명/급여 출력. 급여가 많은 사원부터 출력
```sql
SELECT ENAME 사원명, SAL 급여
FROM EMP
WHERE SAL>=2000
ORDER BY SAL DESC;
```

4. 사원번호가 7788인 사원명/부서번호 출력
```sql
SELECT ENAME 사원명, DEPTNO 부서번호
FROM EMP
WHERE EMPNO LIKE 7788;
```

5. 급여가 2000~3000에 포함되지 않는 사원명/급여 출력
```sql
SELECT ENAME 사원명, SAL 급여
FROM EMP
WHERE NOT SAL BETWEEN 2000 AND 3000;
```

6. 1981/02/20~1981/05/01에 입사한 사원명/담당업무/입사일 출력
```sql
SELECT ENAME 사원명, JOB 담당업무, HIREDATE 입사일
FROM EMP
WHERE HIREDATE BETWEEN '1981/2/20' AND '1981/5/1';
```

7. 부서번호 20, 30에 속한 사원명/부서번호 출력. 이름 내림차순 출력
```sql
SELECT ENAME 사원명, DEPTNO 부서번호
FROM EMP
WHERE DEPTNO BETWEEN 20 AND 30
ORDER BY ENAME DESC;
```

8. 사원 급여가 2000~3000 사이, 부서번호가 20또는 30인 사원명/급여/부서번호 출력. 이름 오름차순 출력
```sql
SELECT ENAME 사원명, SAL 급여, DEPTNO 부서번호
FROM EMP
WHERE SAL BETWEEN 2000 AND 3000 AND DEPTNO IN(20,30)
ORDER BY ENAME ASC;
```

9. 1981년도에 입사한 사원명/입사일 출력 (LIKE 연산자, 와일드카드 사용)
```sql
SELECT ENAME 사원명, HIREDATE 입사일
FROM EMP
WHERE HIREDATE LIKE '81%'
```

10. 관리자가 없는 사원명/담당업무 출력
```sql
SELECT ENAME 사원명, JOB 담당업무
FROM EMP
WHERE MGR IS NULL;
```

11. 커미션을 받을 자격이 있는 사원명/급여/커미션 출력. 급여 및 커미션을 기준으로 내림차순
```sql
SELECT ENAME 사원명, SAL 급여, COMM 커미션
FROM EMP
WHERE NOT COMM IS NULL
ORDER BY SAL, COMM DESC;
```

12. 이름의 세번째 문자가 R인 사원명
```sql
SELECT ENAME 사원명
FROM EMP
WHERE ENAME LIKE '__R%';
```

13. 이름에 A와 E를 모두 포함하고 있는 사원명
```sql
SELECT ENAME 사원명
FROM EMP
WHERE ENAME LIKE '%A%' AND ENAME LIKE '%E%'
```

14. 담당업무가 CLERK 또는 SALESMAN이면서 급여가 $950, $1300, $1600이 아닌 사원명/담당업무/급여
```sql
SELECT ENAME 사원명, JOB 담당업무, SAL 급여
FROM EMP
WHERE JOB IN('CLERK', 'SALESMAN') AND SAL NOT IN(950, 1300, 1600);
```

15. 커미션이 $500 이상인 사원명/급여/커미션
```sql
SELECT ENAME 사원명, SAL 급여, COMM 커미션
FROM EMP
WHERE COMM>=500;
```

16. SUBSTR 함수를 사용하여 사원명, 사원들이 입사한 년도, 입사한 달만 출력
```sql
SELECT ENAME 사원명, SUBSTR(HIREDATE,1,2) 입사_년, SUBSTR(HIREDATE,4,2) 입사_달
FROM EMP;
```

17. SUBSTR 함수를 사용하여 4월에 입사한 사원 출력
```sql
SELECT * FROM EMP
WHERE SUBSTR(HIREDATE,5,1)=4;
```

18. MOD 함수를 사용하여 사원번호가 짝수인 사람 출력
```sql
SELECT * FROM EMP
WHERE MOD(EMPNO,2)=0;
```

19. 입사일을 년도는 2자리(YY), 월은 숫자(MON)로 표시하고 요일은 약어(DY)로 지정하여 출력
```sql
SELECT SUBSTR(HIREDATE,1,2) YY, SUBSTR(HIREDATE,4,2) MON, SUBSTR(HIREDATE,7,2) DY
FROM EMP;
```

20. 올해 며칠이 지났는지 출력. 현재날짜에서 올해 1월 1일을 뺀 결과를 출력하고 TO_DATE 함수를 사용하여 데이터 형 일치
```sql
SELECT TO_DATE(SYSDATE) - TO_DATE('2024-01-01','YYYY-MM-DD') FROM DUAL;
```

21. 사원들의 상관의 사번 출력. 단, 상관이 없는 사원은 NULL 대신 0 출력
```sql
SELECT NVL(MGR,0) FROM EMP; 
```

22. DECODE 함수로 직급에 따라 급여 인상하기. 담당업무가 'ANALYST'인 사원은 200, 'SALESMAN'인 사원은 180, 'MANAGER'인 사원은 150, 'CLERK'인 사원은 100 인상
```sql
SELECT ENAME 이름, SAL 급여, DECODE(JOB,
  'ANALYST',SAL+200,
  'SALESMAN',SAL+180,
  'MANAGER',SAL+150,
  'CLERK',SAL+100) 인상된급여
FROM EMP; 
```

23. 모든 사원의 급여 최고액/최저액/총액/평균 출력. 평균은 정수로 반올림
```SQL
SELECT MAX(SAL) 최고액, MIN(SAL) 최저액, SUM(SAL) 총액, ROUND(AVG(SAL)) 평균
```

24. 각 담당 업무 유형별로 급여 최고액/최저액/총액/평균 출력. 평균은 정수로 반올림
```SQL
SELECT JOB 담당 업무, MAX(SAL) 최고액, MIN(SAL) 최저액, SUM(SAL) 총액, ROUND(AVG(SAL)) 평균
FROM EMP
GROUP BY JOB;
```

25. COUNT(*) 함수를 이용해 담당업무가 동일한 사원 수 출력
```sql
SELECT JOB 담당업무, COUNT(*) 사원수
FROM EMP
GROUP BY JOB;
```

26. 관리자 수 나열
```sql
SELECT COUNT(DISTINCT MGR) 관리자수 FROM EMP;
```

27. 급여 최고액, 최저액의 차액 출력
```sql
SELECT MAX(SAL) 최고액, MIN(SAL) 최저액, MAX(SAL)-MIN(SAL) 차액
FROM EMP;
```

28. 직급별 사원의 최저 급여 출력. 관리자를 알 수 없는 사원의 최저 급여가 2000 미만인 그룹은 제외. 급여 내림차순으로 정렬
```sql
SELECT JOB 직급, MIN(SAL) 최저액
FROM EMP
HAVING MIN(SAL)>=2000
GROUP BY JOB
ORDER BY MIN(SAL) DESC;
```

29. 각 부서에 대해 부서번호, 사원수, 부서 내 모든 사원의 평균 급여 출력. 평균 급여는 소수점 둘째 자리로 반올림
```sql
SELECT DEPTNO 부서번호, COUNT(DEPTNO) 사원수, ROUND(AVG(SAL),2) 평균급여
FROM EMP
GROUP BY DEPTNO;
```

30. 각 부서에 대해 부서번호 이름, 지역명, 사원수, 부서 내 모든 사원의 평균 급여 출력. 평균 급여는 정수로 반올림. DECODE 사용
```sql
SELECT DEPTNO, DECODE(DEPTNO,
  10,'ACCOUNTING',
  20,'RESEARCH',
  30,'SALES',
  40,'OPERATIONS') AS 이름, DECODE(DEPTNO,
  10,'NEW YORK',
  20,'DALLAS',
  30,'CHICAGO',
  40,'BOSTON') AS 지역명, COUNT(*) AS 사원수, ROUNT(AVG(SAL)) AS 평균급여
FROM EMP
GROUP BY DEPTNO;
```
