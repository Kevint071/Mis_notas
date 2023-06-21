from iqoptionapi.stable_api import IQ_Option
error_password = """{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""
Iq = IQ_Option("kevintorrecilla1307@gmail.com", "Torrecilla.14")
check, reason = Iq.connect()

if check:
    while True:
        modo_cuenta = int(input("""
Selecciona el tipo de cuenta:

(1) Real
(2) Práctica
        
Elige entre cuenta real o de práctica: """))

        if modo_cuenta == 1:
            Iq.change_balance("REAL")
            break
        elif modo_cuenta == 2:
            Iq.change_balance("PRACTICE")
            break
        else:
            print("Opción incorrecta")

    print(f"\nMoneda: {Iq.get_currency()}")
    print(f"Balance de cuenta: $ {Iq.get_balance()}")

    activos_binarios = []
    activos_turbo = []
    activos_digitales = []

    ALL_Asset = Iq.get_all_open_time()
    for tipo in ["binary", "turbo", "digital"]:
        for activo in ALL_Asset[tipo].keys():
            for open in ALL_Asset[tipo][activo].values():
                if open and tipo == "binary":
                    activos_binarios.append(activo)
                elif open and tipo == "turbo":
                    activos_turbo.append(activo)
                elif open and tipo == "digital":
                    activos_digitales.append(activo)
    
    print(f"\nActivos binarios: {activos_binarios}")
    print(f"Activos turbo: {activos_turbo}")
    print(f"Activos digitales: {activos_digitales}")

    while True:
        if Iq.check_connect() == False:  # Detecta si el websocket ha sido cerrado
            print("Probando a reconectar")
            check, reason = Iq.connect()
            if check:
                print("Reconectado con éxito")
            else:
                if reason == error_password:
                    print("Contraseña incorrecta")
                else:
                    print("No hay conexión")
else:
    if reason == "[Errno -2] Nombre or servicio no conocido":
        print("No hay conexión")
    elif reason == error_password:
        print("Error en la Contraseña")

estado_coneccion = Iq.check_connect()
