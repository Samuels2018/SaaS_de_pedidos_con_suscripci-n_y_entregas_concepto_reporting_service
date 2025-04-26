# Reporting Service - SaaS de pedidos con suscripción y entregas

Este microservicio forma parte de una arquitectura basada en microservicios para una plataforma SaaS de pedidos con suscripciones y entregas.  
El servicio de reportes permite obtener métricas clave como el uso mensual del sistema y las suscripciones activas.

## 🧰 Tecnologías usadas

- Python 3.11
- Flask
- Docker
- Pytest
- Postman (colección de pruebas)

---

## 🚀 Endpoints disponibles

### 📊 Reporte de uso mensual

**Descripción:** Devuelve el número de pedidos, entregas y nuevos usuarios en un mes específico.

**Parámetros:**
- `year`: Año del reporte (e.g., 2024)
- `month`: Mes del reporte (e.g., 04)

---

### 📈 Reporte de suscripciones activas

**Descripción:** Devuelve una lista con el total de suscripciones activas y planes utilizados.

---


### Clonar el repositorio
```bash```
git clone https://github.com/Samuels2018/SaaS_de_pedidos_con_suscripci-n_y_entregas_concepto_reporting_service.git
cd SaaS_de_pedidos_con_suscripci-n_y_entregas_concepto_reporting_service

FLASK_ENV=development
PORT=5005

## 🐳 Uso con Docker
./run.sh

## estructura del proyecto

├── app/
│   ├── __init__.py
│   ├── controllers/
│   ├── services/
│   └── routes/
├── tests/
│   └── reporting/
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md