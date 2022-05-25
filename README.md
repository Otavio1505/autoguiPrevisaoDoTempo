# autoguiPrevisaoDoTempo
Automação capaz de receber/enviar por Whatsapp, áudio da previsão do tempo da localidade que desejar.

# Sobre o Projeto
A ideia deste projeto surgiu de um desafio pessoal, após aprendizados da biblioteca PyAutoGUI, minha ideia era fazer uma automação capaz de gravar e enviar áudios com alguma finalidade, desta forma surgiu a ideia deste projeto, que será capaz de enviar um aúdio por Whatsapp (é necessário a abertura automática na conta do usuário), além de algumas informações adicionais a respeito da previsão do tempo de uma determinada localidade, especificada pelo usuário. As mensagens enviadas pela automação será através do Whatsapp Web, as mensagens podem ser enviadas para qualquer contato, mas a princípio, esta automação foi criada para uso próprio, onde as mensagens serão enviadas para o próprio número do usuário. Porém é possível haver adaptações nos códigos para que seja enviado também para qualquer contato na lista de contatos do Whatsapp.

# Como funciona?
Primeiramente é preciso da importação da biblioteca PyAutoGUI, responsável por toda a automação do programa. Antes da automação ser iniciada, é aberto 2 inputs para o usuário na qual ele precisará informar o nome da localidade que ele deseja saber a previsão do tempo e o número de contato em que serão enviado as mensagens, para esta automação é recomendado o uso do próprio número de Whatsapp do usuário para que seja enviado as mensagens para ele mesmo.

![a](https://user-images.githubusercontent.com/84475339/170361591-7cf80cb2-6d80-4d05-9d1f-74bc436d94ad.png)

Após a confirmação das informações a automação será iniciada e passará pelos seguintes passos.

1. Abertura do Navegador, neste caso, será usado o Microsoft Edge
2. Abertura do Site: https://web.whatsapp.com/
3. Com o Whatsapp Web aberto, é pesquisado pelo número de contato informado no segundo input, neste caso, o próprio número do usuário e a conversa quando localizada é aberta logo em seguida 

![a](https://user-images.githubusercontent.com/84475339/170361423-15221d9a-43ef-467a-94cd-29020d3c7a21.png)

4. É feita a pesquisa no Google em busca de informações sobre a previsão do tempo da localidade informada no primeiro input. 

![a](https://user-images.githubusercontent.com/84475339/170360393-e9e09e08-777c-4897-a82c-de713bab2f7e.png)

5. O mouse de forma automática irá selecionar a temperatura em graus C° e executará a leitura do texto selecionado em voz alta.

![a](https://user-images.githubusercontent.com/84475339/170360185-a590142f-2a97-49ed-9d29-350328ec6eea.png)

6. De forma rápida o mouse voltará para a guia do Whatsapp e abrirá o áudio e esperará a leitura em voz alta da temperatura encerre. 

![a](https://user-images.githubusercontent.com/84475339/170359591-b47bfd3e-0d8e-4a5f-a87f-a1f07e8390c7.png)

7. Após 5 segundos o áudio se encerrará e enviado logo em seguida. 

![a](https://user-images.githubusercontent.com/84475339/170359241-fba3a65d-6975-4a1f-9232-e3fa75e19d5a.png)

8. Após o envio do áudio o mouse voltará para a guia do Google e copiará a URL do site em que foram retirados as informações da previsão do tempo e os colará na conversa e enviará logo em seguida. 

![a](https://user-images.githubusercontent.com/84475339/170358965-eb950e5f-f8f9-4dc0-93d8-9bc7d80f1c73.png)

9. Como última ação da automação é feito uma captura de tela dinâmica das informações a respeito da previsão do tempo da localidade e será enviado na conversa.

![a](https://user-images.githubusercontent.com/84475339/170358769-d2b02ccb-11e6-4945-80f9-498a04894c0c.png)

Fim da automação.

# Autor
Otávio Moraes Braga
