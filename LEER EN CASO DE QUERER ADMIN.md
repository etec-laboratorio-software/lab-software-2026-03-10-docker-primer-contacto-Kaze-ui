Cuando estás en una computadora nueva, podes crear tu usario normal desde el front sin problemas. Pero para registrarse como administrador tenes que darle permisos a un usuario ya existente.

# 1. Entrar al contenedor del backend
sudo docker exec -it kaze_backend bash

# 2. Instalar sqlite3 (necesario porque el contenedor no lo trae por defecto)
apt-get update && apt-get install -y sqlite3

# 3. Abrir la base de datos con SQLite
sqlite3 /app/data/sql_app.db

# 4. Ver los usuarios registrados
SELECT id_usuario, nombre_usuario, email, tipo_usuario FROM usuario;

# 5. Cambiar el tipo_usuario a admin (reemplazá 'nombre_usuario' por el que quieras)
UPDATE usuario SET tipo_usuario = 'admin' WHERE nombre_usuario = 'nombre_usuario';

# 6. Verificar que el cambio se aplicó
SELECT id_usuario, nombre_usuario, email, tipo_usuario FROM usuario;

# 7. Salir de SQLite
.quit

# 8. Salir del contenedor
exit