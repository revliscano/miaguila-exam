# Locations Microservices
## Diagrama de arquitectura

![diagrama](https://i.ibb.co/DR5CRNy/diagrama.png)

## ¿Cómo probarlo?

1. Clonar repositorio

    `$ git clone https://github.com/revliscano/miaguila-exam.git`

2. Ejecutar `docker-compose`

    `$ docker-compose up -d`

    Los microservicios estarán disponibles en:
    - Storage Service: http://localhost:8001/
    - Postcode Service: http://localhost:8002/

3. Enviar archivo .csv como payload al endpoint:
    
    `POST: /api/v1/locations/uploadcsv/`
    
    Por ejemplo:
   
    ```python
    import requests
    
    file = open('path/al/archivo.csv')
    payload = {"file": ('locations.csv', file, 'multipart/form-data')}
    response = requests.post(
        f'http://localhost:8001{API_PREFIX}/uploadcsv/',
        files=payload
    )
    ```

## Más información

Este examen lo realicé con el framework FastAPI y se utilizó como motor de base de datos, PostgreSQL. 

Se escogió PostgreSQL debido a que permite copiar millones de registros provenientes de un CSV, de manera mucho más veloz que haciendo inserts.

La comunicación entrelos microservicios se realiza a través de HTTP (especfíciamente mediante el endpoint `POST: /api/v1/postcodes/combine/` del servicio Postcode Service. Esta se lleva a cabo de manera asíncrona a la subida de archivos por parte del usuario, gracias al soporte de tareas en segundo plano (BackgroundTasks) que FastAPI ofrece.
