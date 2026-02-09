-- EJERCICIO 1:
-- dar de alta con fecha actual al empleado Jose Escriche Barrera como programador perteneciente al departamento de produccion. Tendra un salario base de 70000 pts/mes y no cobrara comision.
select * from emp;
select dept_no from dept where dnombre = 'PRODUCCIÓN'; -- 40
-- SOLUCION --
insert into emp (fecha_alt, apellido, oficio, dept_no, salario, comision) values (09/02/26, 'Escriche Barrera', 'PROGRAMADOR', (select dept_no from dept where dnombre = 'PRODUCCION'), 70000, 0); 


-- EJERCICIO 2:
-- Se requiere dar de alta un dpto de informatica situado en Fuenlabrada (Madrid).
select * from dept;
select max(dept_no) + 10 from dept; -- 50
-- SOLUCION --
insert into dept (dept_no, dnombre, loc) values ((select max(dept_no) + 10 from dept), 'INFORMATICA', 'Fuenlabrada(Madrid)');


-- EJERCICIO 3:
-- El dpto de ventas, por motivos peseteros, se traslada a Teruel.
-- Realizar dicha modificacion.
select * from dept;
-- SOLUCION --
update dept set loc = 'TERUEL' where loc = 'BARCELONA';


-- EJERCICIO 4:
-- En el dpto anterior (VENTAS), se dan de alta dos empleados:
-- Julian Romeral y Luis Alonso.
-- Su salario base es el menor que cobre un empleado
-- y cobraran una comision de 15 de dicho salario.
select dept_no from dept where dnombre = 'VENTAS'; -- 30
select min(salario) - 1000 from emp; -- 103000
select * from EMP;
-- SOLUCION --
insert into emp (dept_no, apellido, salario, comision) values ((select dept_no from dept where dnombre = 'VENTAS'),'Romeral', (select min(salario) - 1000 from emp), 15);

insert into emp (dept_no, apellido, salario, comision) values ((select dept_no from dept where dnombre = 'VENTAS'),'Alonso', (select min(salario) - 1000 from emp), 15);


-- EJERCICIO 5:
-- Modificar la comision de los empleados de la empresa, de forma que todos tengan un incremento del 10% del salario.
select apellido, comision from emp;
-- SOLUCION --
update emp set comision = comision + 15;


-- EJERCICIO 6:
-- Incrementar un 5% el salario de los interinos de la plantilla que trabajen en el turno de noche.
select apellido, funcion, turno, salario from plantilla;
select apellido, funcion, turno, salario from plantilla where funcion = 'INTERINO' AND TURNO = 'N';
-- SOLUCION --
update plantilla set salario = salario * 1.1 where funcion = 'INTERINO' AND TURNO = 'N';


-- EJERCICIO 7:
-- Incrementar en 5000 pts el salario de los empleados del dptode ventas y del presidente, tomando en cuenta los que se dieron de alta antes que el presidente de la empresa. 
select * from emp;
select fecha_alt from emp where oficio = 'PRESIDENTE'; -- 17/11/95 

select * from dept;
select dept_no from dept where dnombre = 'VENTAS'; -- 30
select fecha_alt from emp where oficio = 'PRESIDENTE';

select apellido, fecha_alt from emp where fecha_alt < (select fecha_alt from emp where oficio = 'PRESIDENTE') AND dept_no = (select dept_no from dept where dnombre = 'VENTAS');

update emp set

----------- ACABARLOS CON SOLUCIONES -----------





