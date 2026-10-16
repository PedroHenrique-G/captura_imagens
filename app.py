import cv2

def capturar_e_salvar():

    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return # early return

    fonte = cv2.FONT_HERSHEY_TRIPLEX
    escala = 0.6
    cor_texto = (255, 0, 0)
    espessura = 1

    while True: # do-while
        status, frame = webcam.read() # desempacotamento

        if not status:
            print("Falha ao receber o frame da webcam.")
            break

        frame_limpo = frame.copy()

        cv2.rectangle(frame, (10, 10), (320, 75), (0, 0, 0), -1)
        cv2.putText(frame, "[ESPAÇO] Salvar foto", (20, 35), fonte, escala, cor_texto, espessura)
        cv2.putText(frame, "[ESCAPE] Sair", (20, 60), fonte, escala, cor_texto, espessura)
        
        cv2.imshow("Captura da Webcam local", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == 32:
            cv2.imwrite("foto.jpg", frame_limpo)
            print("Foto salva: foto.jpg")

            foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("foto_cinza.jpg", foto_cinza)

            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)

            foto_hulk = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2HLS_FULL)
            cv2.imwrite("foto_hulk.jpg", foto_hulk)

            foto_inferno = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2HSV_FULL)
            cv2.imwrite("foto_inferno.jpg", foto_inferno)

        elif tecla == 27:
            print("Encerrando câmera...")
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capturar_e_salvar()