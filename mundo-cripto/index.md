# Mundo Cripto


[Binance](https://www.binance.com/en)

Exchange que permite retirar fondos hacia Polygon (Matic)
[Ascendex](https://ascendex.com/en/global-digital-asset-platform)

Polygon

Quiero llevar fondos a una billetera en Polygon. Voy a enviar USDT desde Binance
hacia una billetera externa y usar XPollinate como puente.

Los USDT se pueden enviar por la red BSC con el protocolo BEP20 hacia la Wallet
externa, voy a probar con 50.8 USDT porque la comisión es fija de 0.8 USDT. En
principio pensé en enviar 10 USDT pero estoy bastante seguro de que va a
funcionar, así que la hago de una suma más grande porque no creo que sea
riesgoso. Dice que tiene un período de 60 minutos para la transacción. Sin
embargo a los 3 minutos la operación aparece como Succesful y me llega mail
de confirmación. Los USDT no aparecían en la Wallet, pero había importado un
token USDT que no era. Como los 50 USDT aparecían en la página de la Wallet de
BSCScan, saqué de ahí el contrato y lo importé, y ahí aparecieron en la wallet.

Si trato de hacer el puente en XPollinate con 50 USDT la comisión es de 0.025
USDT. Como es mi primer uso y la comisión es proporcional al monto, lo voy a
hacer con el mínimo de 1 USDT y la comisión es de 0.0005 USDT.

Cuando hago la transacción se me abre una ventana de Metamask que me dice "Give
permission to access your USDT?" y me cobra 0.12 USDT, lo cual entiendo que es
por única vez, así que le doy a Confirmar. Tarda algunos segundos y confirma.
Sin embargo todavía no se realizó el Swap de los USDT de una red a la otra. Lo
que veo antes de hacer la transacción es que la cuenta destino (de los USDT en
Polygon) tiene la misma dirección que la de origen. Al darle a confirmar,
Metamask me dice esto: "Se detectó una dirección nueva. Haga clic aquí para
agregarla a la libreta de direcciones." Me cobra un gas de 0.000647BNB. Se abre
una pantalla que pide no ser cerrada en la cual se muestra la evolución de la
transacción: "Transaction in progress Please do not close this tab while the
transaction is in progress. If you do, you will need to open up xpollinate again
to manually claim your transaction. Your transfer will automatically end up at
your destination address once it is picked up and propagated by Connext's
network. You can track its progress above or onConnextScan." Finalmente aparece
un botón de "Sign to Claim Funds". Lo apreto y me aparece una ventana de
Metamask que tengo que firmar. Finalmente, tras un corto tiempo se confirma
todo. En la Wallet de origen me quedan 49 USDT y pasé de tener 0.0195 a 0.0187
BNB, es decir 0.0008 = 0.434928 USDT (según CoinGecko). 

En Metamask no veo ninguna nueva billetera y en la wallet de BSC (de origen) no
aparece nada, pero porque no tengo los tokens de USDT importados. Sin embargo
puedo ver en
[PolygonScan](https://polygonscan.com/address/0xd7870303e3eb750f2502aae8c77cd326bcff8afa)
que tengo 1 USDT. Tomo de ahí el contrato para importar el token en la billetera
y finalmente me muestra que tengo 0.999 USDT en esa misma dirección. 

Parto ahora con los 49 USDT que tengo en la billetera en la BSC. Uso XPollinate
para hacer el puente a la red de Polygon. La comisión es de 0.490374 USDT y
tendría que recibir 48.51 USDT según me dice la pantalla. Recordar que tengo
0.0187 BNB en la misma wallet. Me cobra de nuevo 0.12 USDT para darle acceso a
mis fondos. La transacción de otorgar el permiso se confirma a los pocos
segundos. Luego hay que volver a confirmar y aparece el mensaje del gas, esta
vez son 0.00064696 BNB = 0.3512 USD. Tarda un poco más y luego aparece el botón
de Sign to Claim Funds, Metamask abre la pantalla de solicitud de firma y la
pantalla sigue activa (no terminó la transacción) por un ratito más. Finalmente
los fondos llegan a la billetera de destino y tengo 49.504 USDT. En la cuenta
original me quedan 0.018 BNB y 0 USDT. 

Estuve batallando un rato largo porque no podía entrar a [la web de la wallet de
Polygon](https://wallet.polygon.technology/) porque se quedaba en la pantalla de
login tras elegir la billetera Metamask. El problema fue que no tenía
adecuadamente seteada la hora del sistema y por eso no me dejaba loguear.





