CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      with n_high AS(
      SELECT salary,
      DENSE_RANK() OVER(ORDER BY salary desc) as salary_ranks
      FROM Employee )
      
      SELECT salary FROM n_high
      WHERE salary_ranks=N
      LIMIT 1

  );
END