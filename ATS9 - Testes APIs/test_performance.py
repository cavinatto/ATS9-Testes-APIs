import asyncio
import time

import httpx
import pytest
import pytest_asyncio
from httpx import ASGITransport

from api_pagamentos import app

@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
@pytest.mark.parametrize("num_requisicoes", [5, 20, 50])
async def test_performance_pagamentos(async_client, num_requisicoes):
    """
    Dispara `num_requisicoes` chamadas simultâneas ao endpoint /processar
    e verifica que:
      - Todas retornam HTTP 200.
      - O tempo total de execução é menor que 3.5 segundos,
        provando que o processamento é realmente assíncrono/concorrente.
    """

    async def requisitar():
        return await async_client.get("/processar")

    inicio = time.monotonic()

    respostas = await asyncio.gather(*[requisitar() for _ in range(num_requisicoes)])

    tempo_total = time.monotonic() - inicio


    status_codes = [r.status_code for r in respostas]
    assert all(code == 200 for code in status_codes), (
        f"Respostas com falha encontradas: "
        f"{[c for c in status_codes if c != 200]}"
    )

    for resposta in respostas:
        assert resposta.json() == {"status": "pagamento_aprovado"}, (
            f"Corpo inesperado: {resposta.json()}"
        )

    assert tempo_total < 3.5, (
        f"Tempo total ({tempo_total:.2f}s) excedeu o limite de 3.5s "
        f"para {num_requisicoes} requisições simultâneas."
    )

    print(
        f"\n✅ {num_requisicoes} requisições simultâneas concluídas "
        f"em {tempo_total:.2f}s"
    )
