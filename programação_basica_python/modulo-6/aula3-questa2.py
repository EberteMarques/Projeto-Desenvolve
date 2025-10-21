urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

print(f"URLs originais: {urls}")

dominios = [url[4:-4] for url in urls]

print(f"Nomes principais dos domínios: {dominios}")