from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ImagemPlus",
    version="0.0.1",
    author="Maria Mariz",
    author_email="my_email",
    description="Criar um programa que aplique filtros básicos em imagens, como preto e branco, sépia ou ajuste de brilho e contraste dando beleza e simplicidade.",
    long_description=page_description,
    long_description_content_type="ImagemPlus é um pacote Python projetado para aplicar filtros básicos de imagem de forma simples e eficiente. Com ImagemPlus, você pode transformar suas fotos com filtros clássicos como branco e preto, sépia, azul, entre outros. Ideal para quem busca uma maneira rápida e prática de adicionar um toque especial às suas imagens,mas tendo a sutileza da simplicidade.",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
