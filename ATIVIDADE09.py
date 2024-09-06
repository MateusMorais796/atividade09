# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).
km_percorridos = float(input("Quantidade de km percorridos "))
l_consumidos = float(input("Quantidade de litros consumidos "))

c_medio = km_percorridos/l_consumidos

print(f"O consumo medio é de {c_medio} km por litros")