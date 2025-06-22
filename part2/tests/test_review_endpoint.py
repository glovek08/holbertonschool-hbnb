import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Datos de prueba válidos
        self.valid_review_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "rating": 5,
            "comment": "Excelente lugar, muy recomendado",
        }

    # ==================== TESTS PARA POST /reviews ====================

    def test_create_review_success(self):
        """Test: Crear review exitosamente"""
        response = self.client.post("/reviews/", json=self.valid_review_data)

        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["owner_id"], "user123")
        self.assertEqual(data["place_id"], "place456")
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["comment"], "Excelente lugar, muy recomendado")

    def test_create_review_missing_owner_id(self):
        """Test: Error al crear review sin owner_id"""
        invalid_data = {
            "place_id": "place456",
            "rating": 5,
            "comment": "Falta owner_id",
        }

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("message", data)

    def test_create_review_missing_place_id(self):
        """Test: Error al crear review sin place_id"""
        invalid_data = {"owner_id": "user123", "rating": 5, "comment": "Falta place_id"}

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("message", data)

    def test_create_review_missing_rating(self):
        """Test: Error al crear review sin rating"""
        invalid_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "comment": "Falta rating",
        }

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("message", data)

    def test_create_review_missing_comment(self):
        """Test: Error al crear review sin comment"""
        invalid_data = {"owner_id": "user123", "place_id": "place456", "rating": 5}

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("message", data)

    def test_create_review_invalid_rating_type(self):
        """Test: Error al crear review con rating no numérico"""
        invalid_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "rating": "cinco",
            "comment": "Rating inválido",
        }

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("message", data)

    def test_create_review_invalid_rating_range(self):
        """Test: Error al crear review con rating fuera de rango"""
        invalid_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "rating": 10,  # Fuera del rango 1-5
            "comment": "Rating fuera de rango",
        }

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_create_review_empty_fields(self):
        """Test: Error al crear review con campos vacíos"""
        invalid_data = {"owner_id": "", "place_id": "", "rating": 5, "comment": ""}

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_create_review_null_values(self):
        """Test: Error al crear review con valores null"""
        invalid_data = {
            "owner_id": None,
            "place_id": "place456",
            "rating": 5,
            "comment": "Owner ID es null",
        }

        response = self.client.post("/reviews/", json=invalid_data)
        self.assertEqual(response.status_code, 400)

    # ==================== TESTS PARA GET /reviews ====================

    def test_get_all_reviews(self):
        """Test: Obtener todas las reviews"""
        # Primero crear algunas reviews
        self.client.post("/reviews/", json=self.valid_review_data)

        review_data_2 = {
            "owner_id": "user456",
            "place_id": "place789",
            "rating": 3,
            "comment": "Regular, podría mejorar",
        }
        self.client.post("/reviews/", json=review_data_2)

        response = self.client.get("/reviews/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 2)

    def test_get_all_reviews_empty_list(self):
        """Test: Obtener lista vacía cuando no hay reviews"""
        # Asumiendo que la base de datos está vacía al inicio
        response = self.client.get("/reviews/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)

    # ==================== TESTS PARA GET /reviews/<review_id> ====================

    def test_get_review_by_id_success(self):
        """Test: Obtener review por ID exitosamente"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        self.assertEqual(response.status_code, 201)
        review_id = response.get_json()["id"]

        # Obtener la review por ID
        response = self.client.get(f"/reviews/{review_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], review_id)
        self.assertEqual(data["owner_id"], "user123")
        self.assertEqual(data["place_id"], "place456")
        self.assertEqual(data["rating"], 5)

    def test_get_review_by_id_not_found(self):
        """Test: Error al obtener review que no existe"""
        response = self.client.get("/reviews/nonexistent-id")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn("error", data)

    def test_get_review_by_id_empty_string(self):
        """Test: Error al obtener review con ID vacío"""
        response = self.client.get("/reviews/")
        # Esto debería redirigir al endpoint de listar todas las reviews
        self.assertEqual(response.status_code, 200)

    def test_get_review_by_id_special_characters(self):
        """Test: Error al obtener review con caracteres especiales en ID"""
        response = self.client.get("/reviews/@#$%")
        self.assertEqual(response.status_code, 404)

    # ==================== TESTS PARA PUT /reviews/<review_id> ====================

    def test_update_review_success(self):
        """Test: Actualizar review exitosamente"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        self.assertEqual(response.status_code, 201)
        review_id = response.get_json()["id"]

        # Actualizar la review
        update_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "rating": 4,
            "comment": "Actualizado: Muy buen lugar",
        }

        response = self.client.put(f"/reviews/{review_id}", json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["rating"], 4)
        self.assertEqual(data["comment"], "Actualizado: Muy buen lugar")

    def test_update_review_not_found(self):
        """Test: Error al actualizar review que no existe"""
        response = self.client.put(
            "/reviews/nonexistent-id", json=self.valid_review_data
        )
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn("error", data)

    def test_update_review_missing_fields(self):
        """Test: Error al actualizar review con campos faltantes"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        review_id = response.get_json()["id"]

        # Intentar actualizar con datos incompletos
        incomplete_data = {"rating": 4}

        response = self.client.put(f"/reviews/{review_id}", json=incomplete_data)
        self.assertEqual(response.status_code, 400)

    def test_update_review_invalid_data(self):
        """Test: Error al actualizar review con datos inválidos"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        review_id = response.get_json()["id"]

        # Intentar actualizar con datos inválidos
        invalid_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "rating": 15,  # Fuera de rango
            "comment": "Rating inválido",
        }

        response = self.client.put(f"/reviews/{review_id}", json=invalid_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_update_review_empty_fields(self):
        """Test: Error al actualizar review con campos vacíos"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        review_id = response.get_json()["id"]

        # Intentar actualizar con campos vacíos
        empty_data = {"owner_id": "", "place_id": "", "rating": 5, "comment": ""}

        response = self.client.put(f"/reviews/{review_id}", json=empty_data)
        self.assertEqual(response.status_code, 400)

    # ==================== TESTS PARA DELETE /reviews/<review_id> ====================

    def test_delete_review_success(self):
        """Test: Eliminar review exitosamente"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        self.assertEqual(response.status_code, 201)
        review_id = response.get_json()["id"]

        # Eliminar la review
        response = self.client.delete(f"/reviews/{review_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Review deleted successfully")

        # Verificar que la review fue eliminada
        response = self.client.get(f"/reviews/{review_id}")
        self.assertEqual(response.status_code, 404)

    def test_delete_review_not_found(self):
        """Test: Error al eliminar review que no existe"""
        response = self.client.delete("/reviews/nonexistent-id")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn("error", data)

    def test_delete_review_twice(self):
        """Test: Error al eliminar la misma review dos veces"""
        # Crear una review primero
        response = self.client.post("/reviews/", json=self.valid_review_data)
        review_id = response.get_json()["id"]

        # Eliminar la review por primera vez
        response = self.client.delete(f"/reviews/{review_id}")
        self.assertEqual(response.status_code, 200)

        # Intentar eliminar nuevamente
        response = self.client.delete(f"/reviews/{review_id}")
        self.assertEqual(response.status_code, 404)

    # ==================== TESTS PARA GET /reviews/places/<place_id>/reviews ====================

    def test_get_reviews_by_place_success(self):
        """Test: Obtener reviews por place_id exitosamente"""
        place_id = "place123"

        # Crear varias reviews para el mismo lugar
        review_1 = {
            "owner_id": "user1",
            "place_id": place_id,
            "rating": 5,
            "comment": "Excelente lugar",
        }
        review_2 = {
            "owner_id": "user2",
            "place_id": place_id,
            "rating": 4,
            "comment": "Muy bueno",
        }

        self.client.post("/reviews/", json=review_1)
        self.client.post("/reviews/", json=review_2)

        response = self.client.get(f"/reviews/places/{place_id}/reviews")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 2)

        # Verificar que todas las reviews son del lugar correcto
        for review in data:
            self.assertEqual(review["place_id"], place_id)

    def test_get_reviews_by_place_not_found(self):
        """Test: Error al obtener reviews de place que no existe"""
        response = self.client.get("/reviews/places/nonexistent-place/reviews")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn("error", data)

    def test_get_reviews_by_place_no_reviews(self):
        """Test: Obtener lista vacía para place sin reviews"""
        response = self.client.get("/reviews/places/empty-place/reviews")
        # Si el place existe pero no tiene reviews, debería retornar lista vacía
        # Si el place no existe, debería retornar 404
        self.assertIn(response.status_code, [200, 404])
        if response.status_code == 200:
            data = response.get_json()
            self.assertIsInstance(data, list)
            self.assertEqual(len(data), 0)

    def test_get_reviews_by_place_empty_place_id(self):
        """Test: Error con place_id vacío"""
        response = self.client.get("/reviews/places//reviews")
        self.assertEqual(response.status_code, 404)

    # ==================== TESTS ADICIONALES ====================

    def test_invalid_http_methods(self):
        """Test: Métodos HTTP no permitidos"""
        # PATCH no debería estar permitido
        response = self.client.patch("/reviews/")
        self.assertEqual(response.status_code, 405)

        # OPTIONS debería estar permitido (CORS)
        response = self.client.options("/reviews/")
        self.assertIn(response.status_code, [200, 204])

    def test_create_review_content_type(self):
        """Test: Error con Content-Type incorrecto"""
        response = self.client.post(
            "/reviews/", data="invalid data", content_type="text/plain"
        )
        self.assertEqual(response.status_code, 400)

    def test_create_review_extreme_values(self):
        """Test: Crear review con valores extremos"""
        # Texto muy largo
        long_comment = "a" * 1000
        extreme_data = {
            "owner_id": "user123",
            "place_id": "place456",
            "rating": 1,  # Valor mínimo válido
            "comment": long_comment,
        }

        response = self.client.post("/reviews/", json=extreme_data)
        # Debería manejar textos largos apropiadamente
        self.assertIn(response.status_code, [201, 400])

    def test_rating_boundary_values(self):
        """Test: Probar valores límite para rating"""
        # Rating = 1 (mínimo válido)
        min_data = self.valid_review_data.copy()
        min_data["rating"] = 1
        response = self.client.post("/reviews/", json=min_data)
        self.assertEqual(response.status_code, 201)

        # Rating = 5 (máximo válido)
        max_data = self.valid_review_data.copy()
        max_data["rating"] = 5
        max_data["owner_id"] = "user124"  # Diferente para evitar duplicados
        response = self.client.post("/reviews/", json=max_data)
        self.assertEqual(response.status_code, 201)

        # Rating = 0 (inválido)
        invalid_min_data = self.valid_review_data.copy()
        invalid_min_data["rating"] = 0
        invalid_min_data["owner_id"] = "user125"
        response = self.client.post("/reviews/", json=invalid_min_data)
        self.assertEqual(response.status_code, 400)

        # Rating = 6 (inválido)
        invalid_max_data = self.valid_review_data.copy()
        invalid_max_data["rating"] = 6
        invalid_max_data["owner_id"] = "user126"
        response = self.client.post("/reviews/", json=invalid_max_data)
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main(verbosity=2)
