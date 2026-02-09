-- 1. Insertar un nuevo empleado de la plantilla
-- Su nombre es Cabrales, sala 4, turno N y trabajara en el hospital El Carmen.
-- El id debemos buscar el maximo libre.
select * from plantilla;
select max(empleado_no) + 1 from plantilla; -- 9902

select hospital_cod from HOSPITAL where NOMBRE='El Carmen';

insert into plantilla (hospital_cod, sala_cod, empleado_no, apellido, turno) values ((select hospital_cod from HOSPITAL where NOMBRE='El Carmen'), 4, (select max(empleado_no) + 1 from plantilla), 'cabrales', 'N');



-- 2. Eliminar de la plantilla todas las personas que no tienen un hospital asignado.
delete from plantilla where hospital_cod is null or hospital_cod not in (select hospital from hospital);



