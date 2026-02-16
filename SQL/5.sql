SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
    LAG(num,1) OVER (ORDER BY id) AS pre1,
    LAG(num,2) OVER (ORDER BY id) AS pre2
    FROM Logs
)t
WHERE num = pre1 AND num = pre2;