-- Ejercicio 1
-- numero empleado, 
-- apellido 
-- y fecha de alta del empleado mas antiguo de la empresa
select emp_no, apellido, fecha_alt from emp where fecha_alt=(select fecha_alt from emp where fecha_alt = '20/10/86');

-- Ejercicio 2
-- numero de empleado,
-- apellido,
-- fecha de alta del empleado mas moderno de la empresa
select fecha_alt FROM emp order by fecha_alt desc;
select emp_no, apellido, fecha_alt from emp where fecha_alt =(select fecha_alt from emp where fecha_alt = '11/12/97');

-- Ejercicio 3:
-- apellido,
-- salario,
-- mismo oficio que jimenez
select apellido, salario from emp where oficio in (select oficio from emp where oficio = 'DIRECTOR');

-- Ejercicio 4
-- apellido,
-- oficio,
-- salario, 
-- numero de dpto
-- de los empleados con salario mayor que el mejor salario del departamento 30.
select apellido, oficio, salario, dept_no from emp where salario > (select salario from emp where salario = 370500);

-- Ejercicio 5
-- mostrar apellido,
-- funcion u oficio,
-- sala o dpto,
-- de todos los empleados que trabajen en empresa o plantilla.
select emp.apellido, emp.oficio, dept.dnombre as oficina from emp 
inner join DEPT
on emp.dept_no = dept.dept_no
union
select plantilla.apellido, plantilla.funcion, sala.nombre as oficina from plantilla  
inner join sala 
on plantilla.hospital_cod = sala.hospital_cod;

-- Ejercicio 6
-- apellidos
-- oficio
-- de los empleados del dpto 20
-- cuyo trabajo sea al mismo que el de cualquier empleado de ventas.




select emp.apellido, dept.dnombre 
from emp 
INNER join dept 
on emp.dept_no = dept.dept_no
where dnombre = 'VENTAS';





where emp.apellido in (select apellido, oficio from emp where dept_no = 20);











