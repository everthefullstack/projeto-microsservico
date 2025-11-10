from httpx import AsyncClient
import pytest


url_prefix: str = "/documentos/"

@pytest.mark.asyncio
async def test_insert_documento(http_client: AsyncClient):

    payload = {
        "titulo": "Como preparar sua moto para longas viagens",
        "conteudo": "Checklist completo para garantir conforto e seguranca em trajetos de longa distância.",
        "autor": "Vanessa Ribeiro",
        "data": "2025-11-09",
        "latitude": -16.6869,
        "longitude": -49.2648
    }

    response = await http_client.post(f"{url_prefix}", json=payload)
    data = response.json()
    print(data)

    assert response.status_code == 201
    assert "id" in data
    assert data["titulo"] == payload["titulo"]
    assert data["conteudo"] == payload["conteudo"]
    assert data["autor"] == payload["autor"]
    assert data["data"] == payload["data"]
    assert data["latitude"] == payload["latitude"]
    assert data["longitude"] == payload["longitude"]

@pytest.mark.asyncio
async def test_insert_documento_sem_campo_latitude(http_client: AsyncClient):

    payload = {
        "titulo": "Como preparar sua moto para longas viagens",
        "conteudo": "Checklist completo para garantir conforto e segurança em trajetos de longa distância.",
        "autor": "Vanessa Ribeiro",
        "data": "2025-11-09",
        "longitude": -49.2648
    }

    response = await http_client.post(f"{url_prefix}", json=payload)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_select_documentos_com_latitude_longitude(http_client: AsyncClient):

    query_params = {
        "busca": "moto",
        "latitude": -16.6869,
        "longitude": -49.2648,
    }
    
    response = await http_client.get(f"{url_prefix}", params=query_params)
    data = response.json()
    print(data)

    assert response.status_code == 200
    for documento in data:
        assert "id" in documento
        assert "titulo" in documento
        assert "conteudo" in documento
        assert "autor" in documento
        assert "data" in documento
        assert "latitude" in documento
        assert "longitude" in documento

@pytest.mark.asyncio
async def test_select_documentos_sem_latitude_longitude(http_client: AsyncClient):
    
    query_params = {
        "busca": "moto"
    }

    response = await http_client.get(f"{url_prefix}", params=query_params)
    data = response.json()
    print(data)

    assert response.status_code == 200
    for documento in data:
        assert "id" in documento
        assert "titulo" in documento
        assert "conteudo" in documento
        assert "autor" in documento
        assert "data" in documento
        assert "latitude" in documento
        assert "longitude" in documento