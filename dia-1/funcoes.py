def concat_like_tuple(*args):
    final_string = ""
    print(args) #('Cris', 'Wallace', 'Carol')
    for index, name in enumerate(args, 1):
        final_string += f"O nome da pessoa {index} é {name}.\n"
    return final_string


def concat_like_dict(**kwargs):
    print(kwargs) #{'nome': 'Felipe', 'sobrenome': 'Silva', 'idade': 25}
    final_string = (
        f'{kwargs["nome"]} {kwargs["sobrenome"]} tem {kwargs["idade"]} anos.\n'
    )
    return final_string


concat_like_tuple("Cris", "Wallace", "Carol")
# saída:
# O nome da pessoa 1 é Cris.
# O nome da pessoa 2 é Wallace.
# O nome da pessoa 3 é Carol.
# Os *args são recebidos assim: ('Cris', 'Wallace', 'Carol')

concat_like_dict(nome="Felipe", sobrenome="Silva", idade=25)
# saída:
# Felipe Silva tem 25 anos.
# Os *kwargs são recebidos assim: {'nome': 'Felipe', 'sobrenome': 'Silva', 'idade': 25}
