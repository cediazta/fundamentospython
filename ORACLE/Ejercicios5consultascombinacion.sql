-- 05 - CONSULTAS DE COMBINACION_JOIN

-- Ejercicio 1:
SELECT emp.apellido, emp.oficio, emp.salario, dept.dnombre
FROM emp
INNER JOIN dept
ON emp.dept_no = dept.dept_no
WHERE emp.salario > 300000;

-- Ejercicio 2:
SELECT sala.nombre, hospital.nombre
FROM sala  
INNER JOIN hospital
ON sala.hospital_cod = hospital.hospital_cod;

-- Ejercicio 3:
SELECT count(emp.apellido) AS TRABAJADORES, dept.loc
FROM emp 
RIGHT JOIN dept 
ON emp.dept_no = dept.dept_no
group by dept.loc;

-- EJERCICIO 4:
SELECT dept.dnombre, COUNT(emp.apellido) AS PERSONAS, emp.oficio
FROM emp 
INNER JOIN dept 
ON emp.dept_no = dept.dept_no
GROUP BY emp.oficio, dept.dnombre;

-- Ejercicio 5:
SELECT COUNT(sala.sala_cod), sala.nombre, hospital.nombre
FROM sala 
INNER JOIN hospital 
ON sala.hospital_cod = hospital.hospital_cod 
GROUP BY sala.nombre, hospital.nombre;

-- Ejercicio 6:  (DUDA)
SELECT count(emp.apellido), dept.dnombre
FROM emp 
INNER JOIN dept 
ON emp.dept_no = dept.dept_no 
GROUP BY dept.nombre 
WHERE emp.fecha_alt 
BETWEEN '__/__/97'
AND '__/__/98';

-- Ejercicio 7: (duda)
SELECT dept.loc, count(emp.apellido) AS PERSONAS
FROM dept 
INNER JOIN emp 
ON emp.dept_no = dept.dept_no
GROUP BY dept.loc 
where dept.loc >= 4;

-- Ejercicio 8:
SELECT dept.loc, AVG(emp.salario) AS MEDIASALARIAL
FROM dept 
INNER JOIN emp 
ON emp.dept_no = dept.dept_no
GROUP BY dept.loc
WHERE dept.loc = 'MADRID'
AND dept.loc = 'BARCELONA';


