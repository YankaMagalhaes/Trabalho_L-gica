# função declarada
def loginUsuario (perfil) :
# lower utilizado para verificar se o texto digitado pelo usuário é minúsculo ou maiúsculo.
#if e else utilizados para verificar se o texto digitado pelo user se trata ou não de letras maiúsculas e minúsculas
    if perfil.lower () == 'admin' :
        print ('Bem-vindo, Administrador.')
    else:
        print ('Bem-vindo, Usuário')
# print imprime o texto conforme o texto digitado
# funções chamadas para verificar com diferentes tipos se o texto digitado corresponde ao armázenado
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')