from locust import HttpUser, task, constant

class NotificationCapacityTest(HttpUser):
    wait_time = constant(1)  # No hay pausas; máxima presión continua

    @task
    def crear_notificacion(self):
        """Evalúa la capacidad de creación de notificaciones"""
        payload = {
            "user_id": 2,
            "title": "Prueba de capacidad",
            "message": "Simulación intensiva de notificaciones concurrentes",
            "type": "alert"
        }
        headers = {"Content-Type": "application/json"}
        self.client.post("/api/notifications/", json=payload, headers=headers)