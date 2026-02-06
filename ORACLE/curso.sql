SELECT apellido, funcion,
CASE TURNO
    WHEN 'T' THEN 'TARDE'
    WHEN 'M' THEN 'MAÑANA'
    ELSE 'NOCHE'
END AS TURNOBONITO, turno 
FROM plantilla;