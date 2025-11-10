from httpx import AsyncClient

dados = [

{
         "titulo":"A evolucão das motocicletas elétricas",
         "conteudo":"As motos elétricas estão ganhando espaco no mercado brasileiro, com modelos mais potentes e acessíveis.",
         "autor":"Mariana Souza",
         "data":"2025-11-09",
         "latitude":-23.5505,
         "longitude":-46.6333
      },
      {
         "titulo":"Dicas para iniciantes no motociclismo",
         "conteudo":"Conheca os principais cuidados e equipamentos essenciais para quem está comecando a pilotar.",
         "autor":"Carlos Mendes",
         "data":"2025-11-09",
         "latitude":-22.9068,
         "longitude":-43.1729
      },
      {
         "titulo":"Viagem de moto pela Serra do Rio do Rastro",
         "conteudo":"Um roteiro incrível para motociclistas que buscam aventura e paisagens deslumbrantes em Santa Catarina.",
         "autor":"Fernanda Lima",
         "data":"2025-11-09",
         "latitude":-28.3881,
         "longitude":-49.5522
      },
      {
         "titulo":"Comparativo: naked vs. esportiva",
         "conteudo":"Entenda as diferencas entre os estilos de motocicletas e qual se adapta melhor ao seu perfil.",
         "autor":"João Ricardo",
         "data":"2025-11-09",
         "latitude":-19.9167,
         "longitude":-43.9345
      },
      {
         "titulo":"Motociclistas e seguranca no trânsito",
         "conteudo":"Estudo aponta que o uso correto de equipamentos reduz em até 60% os riscos de acidentes graves.",
         "autor":"Luciana Prado",
         "data":"2025-11-09",
         "latitude":-30.0346,
         "longitude":-51.2177
      },
      {
         "titulo":"Customizacão de motos: estilo e personalidade",
         "conteudo":"Saiba como transformar sua moto em uma verdadeira extensão do seu estilo pessoal.",
         "autor":"Eduardo Tavares",
         "data":"2025-11-09",
         "latitude":-3.7172,
         "longitude":-38.5433
      },
      {
         "titulo":"Top 5 motos para uso urbano em 2025",
         "conteudo":"Selecionamos os melhores modelos para quem busca agilidade e economia nas cidades.",
         "autor":"Patrícia Gomes",
         "data":"2025-11-09",
         "latitude":-15.7942,
         "longitude":-47.8822
      },
      {
         "titulo":"Mototurismo no Brasil: destinos imperdíveis",
         "conteudo":"Descubra os melhores roteiros para explorar o país sobre duas rodas.",
         "autor":"Rafael Costa",
         "data":"2025-11-09",
         "latitude":-25.4284,
         "longitude":-49.2733
      },
      {
         "titulo":"Manutencão preventiva para motocicletas",
         "conteudo":"Evite dores de cabeca com dicas práticas de manutencão básica para sua moto.",
         "autor":"Ana Beatriz",
         "data":"2025-11-09",
         "latitude":-12.9718,
         "longitude":-38.5011
      },
      {
         "titulo":"O impacto das motos no meio ambiente",
         "conteudo":"Análise sobre emissões, consumo de combustível e alternativas sustentáveis no setor de duas rodas.",
         "autor":"Thiago Martins",
         "data":"2025-11-09",
         "latitude":-1.4558,
         "longitude":-48.4902
      },
      {
         "titulo":"Motocross: adrenalina e técnica nas trilhas",
         "conteudo":"O motocross exige preparo físico e domínio técnico para enfrentar terrenos desafiadores.",
         "autor":"Bruno Ferreira",
         "data":"2025-11-09",
         "latitude":-20.3155,
         "longitude":-40.3128
      },
      {
         "titulo":"Como escolher o capacete ideal",
         "conteudo":"Saiba quais critérios considerar na hora de comprar um capacete seguro e confortável.",
         "autor":"Juliana Rocha",
         "data":"2025-11-09",
         "latitude":-8.0476,
         "longitude":-34.8770
      },
      {
         "titulo":"Mulheres no motociclismo: espaco e representatividade",
         "conteudo":"Cada vez mais mulheres estão conquistando espaco nas pistas e nas estradas.",
         "autor":"Renata Carvalho",
         "data":"2025-11-09",
         "latitude":-10.9472,
         "longitude":-37.0731
      },
      {
         "titulo":"Economia com motos: vale a pena substituir o carro?",
         "conteudo":"Comparativo entre custos de manutencão, consumo e impostos entre motos e carros.",
         "autor":"Fábio Almeida",
         "data":"2025-11-09",
         "latitude":-22.1207,
         "longitude":-51.3925
      },
      {
         "titulo":"Motocicletas e tecnologia: conectividade sobre duas rodas",
         "conteudo":"Modelos modernos oferecem integracão com smartphones, GPS e sistemas de seguranca.",
         "autor":"Camila Duarte",
         "data":"2025-11-09",
         "latitude":-5.7945,
         "longitude":-35.2110
      },
      {
         "titulo":"Roteiro de moto pelo litoral nordestino",
         "conteudo":"Explore praias paradisíacas e cultura vibrante em uma viagem de moto inesquecível.",
         "autor":"Diego Nascimento",
         "data":"2025-11-09",
         "latitude":-9.6658,
         "longitude":-35.7350
      },
      {
         "titulo":"Motos clássicas: estilo que atravessa geracões",
         "conteudo":"Conheca os modelos que marcaram época e ainda fazem sucesso entre colecionadores.",
         "autor":"Sérgio Oliveira",
         "data":"2025-11-09",
         "latitude":-29.7174,
         "longitude":-53.7170
      },
      {
         "titulo":"Cuidados com a moto na temporada de chuvas",
         "conteudo":"Dicas para manter a seguranca e preservar sua moto durante o período chuvoso.",
         "autor":"Isabela Farias",
         "data":"2025-11-09",
         "latitude":-3.1190,
         "longitude":-60.0217
      },
      {
         "titulo":"Motos e cultura urbana: expressão sobre rodas",
         "conteudo":"A influência das motocicletas na arte, moda e comportamento das cidades.",
         "autor":"Leandro Silva",
         "data":"2025-11-09",
         "latitude":-22.8375,
         "longitude":-47.6066
      },
      {
         "titulo":"Como preparar sua moto para longas viagens",
         "conteudo":"Checklist completo para garantir conforto e seguranca em trajetos de longa distância.",
         "autor":"Vanessa Ribeiro",
         "data":"2025-11-09",
         "latitude":-16.6869,
         "longitude":-49.2648
      }
]

async def criar_documentos():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        for documento in dados:
            response = await client.post("/documentos/", json=documento)
            print(f"Status: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(criar_documentos())