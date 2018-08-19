# https://leetcode.com/problems/students-report-by-geography/description/

SELECT c1.America,
       c2.Asia,
       c3.Europe
FROM (SELECT @c1 := @c1 + 1 AS Id,
             IF (continent = 'America',name,NULL) AS America
      FROM student,
           (SELECT @c1 := 0) init
      ORDER BY ISNULL(America), America) c1,
     (SELECT @c2 := @c2 + 1 AS Id,
             IF (continent = 'Asia',name,NULL) AS Asia
      FROM student,
           (SELECT @c2 := 0) init
      ORDER BY ISNULL(Asia), Asia) c2,
     (SELECT @c3 := @c3 + 1 AS Id,
             IF (continent = 'Europe',name,NULL) AS Europe
      FROM student,
           (SELECT @c3 := 0) init
      ORDER BY ISNULL(Europe), Europe) c3
WHERE c1.Id = c2.Id
AND   c2.Id = c3.Id
AND   NOT (ISNULL(c1.America) AND ISNULL(c2.Asia) AND ISNULL(c3.Europe));
