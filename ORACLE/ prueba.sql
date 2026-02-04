-- EJERCICIO 1 (Visualizar los salarios mayores para cada oficio.)
select max(SALARIO) as SALARIOSMAYORES, OFICIO
from EMP
group by OFICIO;

-- EJERCICIO 5 (Buscar aquellos departamentos con cuatro o más personas trabajando.)
select count(*) as PERSONAS, DEPT_NO
from EMP
group by DEPT_NO
having count(*) >= 4;

-- EJERCICIO 7 (Visualizar el número de enfermeros, enfermeras e interinos que hay en la plantilla, ordenados por la función.)
select count(*) as PERSONAS, FUNCION
from PLANTILLA
where FUNCION IN('INTERINO', 'ENFERMERO', 'ENFERMERA')
group by FUNCION;

-- EJERCICIO 8 (Visualizar departamentos, oficios y número de personas, para aquellos departamentos que tengan dos o más personas trabajando en el mismo oficio.)
select count(*) as PERSONAS, OFICIO, DEPT_NO
from EMP
group by OFICIO, DEPT_NO
having count(*) >=2;

-- EJERCICIO 12 (Calcular el salario medio de la plantilla de la sala 6, según la función que realizan. Indicar la función y el número de empleados.)
select avg(SALARIO) as MEDIASALARIAL, FUNCION, count(*) as EMPLEADOS
from PLANTILLA
where SALA_COD = 6
group by FUNCION;

-- EJERCICIO 13 (Averiguar los últimos empleados que se dieron de alta en la empresa en cada uno de los oficios, ordenados por la fecha.)
select max(FECHA_ALT) as MAXFECHAALTA, OFICIO
from EMP
group by OFICIO
order by MAXFECHAALTA desc;

-- EJERCICIO 16 (Mostrar el número de enfermeras que existan por cada sala.)
select count(*) as ENFERMERAS, SALA_COD
from PLANTILLA
where FUNCION = 'ENFERMERA'
group by SALA_COD;




