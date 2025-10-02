import sys
import re

titulo = re.compile(r"^(# |## |### )(.*)$")
negrito = re.compile(r"\*\*(.+?)\*\*")
italico = re.compile(r"\*(.+?)\*")
listanumerada = re.compile(r"^\d+\. (.+)$")
url = re.compile(r"\[([^\]]*)\]\((.*?)\)")
imagem = re.compile(r"!\[([^\]]*)\]\((.*?)\)")

counter=0

for linha in sys.stdin:
    counter2=1
    if(listanumerada.match(linha)!=None):
        p=listanumerada.match(linha)
        if counter==0:
            print("<ol>")
            linha=f"<li>{p.group(1)}</li>\n"
            counter+=1
        else:
            linha=f"<li>{p.group(1)}</li>\n"
        counter2=0

    if(titulo.match(linha)!=None):
        p=titulo.match(linha)
        numero = len(p.group(1))-1
        linha = f"<h{numero}>{p.group(2)}</h{numero}>\n"

    linha = re.sub(negrito,r"<b>\1</b>",linha)
    linha = re.sub(italico,r"<i>\1</i>",linha)
    linha = re.sub(imagem,r"<img src=\"\2\" alt=\"\1\"/>",linha)
    linha = re.sub(url,r"<a href=\"\2\">\1</a>",linha)

    if counter2 == 1 and counter==1:
        print("</ol>")
        counter-=1

    print(linha, end="")


