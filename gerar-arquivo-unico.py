# Gera prime-estetica-arquivo-unico.html com as imagens da pasta img/ embutidas,
# para enviar o site como um único arquivo. Uso: python gerar-arquivo-unico.py
import base64, mimetypes, pathlib, re

base = pathlib.Path(__file__).parent
html = (base / "index.html").read_text(encoding="utf-8")

def embutir(m):
    caminho = base / m.group(2)
    tipo = mimetypes.guess_type(caminho.name)[0]
    dados = base64.b64encode(caminho.read_bytes()).decode()
    return f'{m.group(1)}data:{tipo};base64,{dados}"'

saida = re.sub(r'(src=")(img/[^"]+)"', embutir, html)
destino = base / "prime-estetica-arquivo-unico.html"
destino.write_text(saida, encoding="utf-8")
print(f"{destino.name}: {destino.stat().st_size // 1024} KB")
